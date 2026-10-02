# Live Demo Script

Step-by-step scenarios for demonstrating Datadog CI/CD Optimization and Test Optimization.

## Prerequisites

- [ ] `DD_API_KEY` configured as GitHub secret
- [ ] GitHub App installed with CI Visibility enabled
- [ ] Test Impact Analysis enabled (exclude `main` **and `preprod`** — see B0)
- [ ] Auto Test Retries enabled for `demo-main-build`
- [ ] Early Flake Detection enabled for `demo-pr-validation`
- [ ] Run **CI - Seed Datadog Data** workflow (or manual steps below)

---

## Part A: CI Pipeline fundamentals (~10 min)

### A1 — PR Validation pipeline

1. Create branch `demo/pr-validation`
2. Make a small change to `src/billing/calculator.py`
3. Open a pull request
4. In Datadog **CI Pipeline Executions**, open `CI - PR Validation`
5. Show the job DAG: `lint` → `unit-tests` + `integration-smoke` in parallel

**Talking points**: required checks, fan-out parallelism, separate job responsibilities.

### A2 — Main Build pipeline

1. Merge the PR to `main`
2. Open `CI - Main Build` in Datadog
3. Show sequential flow: `lint` → `test` → `deploy-staging`
4. Point out the `staging` environment gate on deploy

**Talking points**: default-branch pipeline, deployment gate, total pipeline duration.

### A3 — Nightly Regression

1. Trigger **CI - Nightly Regression** via `workflow_dispatch`
2. Show `dd_plan` → artifact → matrix `dd_test` jobs
3. Compare wall-clock vs single-node baseline

**Talking points**: scheduled CI, artifact sharing, dynamic matrix sizing.

### A4 — Hotfix Fast Path

1. Trigger **CI - Hotfix Fast Path** with branch `main`
2. Show TIA + parallelization combined under urgency

**Talking points**: manual dispatch, branch input, optimized path for incidents.

---

## Part B: Test Optimization (~10 min)

### B0 — Test Impact Analysis across 4 nodes (primary TIA demo)

> **The commit message must NOT contain `ITR:NoSkip`.** That flag forces the full suite and
> would disable the very skipping this demo exists to show. (The parallelization demo in B1
> needs the opposite — the two are easy to mix up.)

One PR, 8 checks. Both legs run the identical 965-test suite, split across the same 4 nodes by
the same naive file-count shard. The only difference is `DD_CIVISIBILITY_ITR_ENABLED`.

| Leg | node 0 | node 1 | node 2 | node 3 | Slowest | Total compute |
| --- | --- | --- | --- | --- | --- | --- |
| `baseline` | 300 passed **70.0s** | 240 passed 33.5s | 173 passed 16.7s | 252 passed 33.9s | **70.0s** | 154s |
| `tia` | 72 passed, 228 skipped **38.0s** | 240 skipped **1.4s** | 5 passed, 168 skipped **1.2s** | 12 passed, 240 skipped **1.4s** | **38.0s** | 42s |

Measured on PR #6, run 37056345192. Quote **test time**, not job time — both legs pay ~25s of
fixed setup (checkout, pip, Datadog agent).

**The two things to say:**

1. *"TIA skipped 876 of 965 tests. Wall-clock went from 70 seconds to 38, and total compute from
   154 seconds to 42 — we are paying for a quarter of the machine time."*
2. *"But look at the distribution. One node is doing all 38 seconds while three finish in about
   a second. TIA removed the work; it did nothing about how the remainder is spread."*

That second point is the setup for B1, which fixes exactly that.

**Re-run the demo (PR #6 already exists — this is the normal path):**
```bash
git checkout tia/add-tax-fix && git pull
git commit --allow-empty -m "Trigger TIA demo" && git push
```

**Build it from scratch instead:**
```bash
git checkout preprod && git pull
git checkout -b tia/add-tax-fix          # must NOT match demo/** or 4 extra workflows fire
# change one line inside add_tax() in src/billing/calculator.py
git commit -am "fix: billing tax rounding"
git push -u origin tia/add-tax-fix
gh pr create --base preprod
```

**The edit must be to `src/billing/calculator.py`.** It is the only 37s file, and it lands in
shard 0 — that is what produces the one-hot-node picture. Editing a module with no
`sleep_seconds` budget (anything outside the 8 heavy modules) makes every node finish in about a
second, which reads as "nothing happened".

**Expect the test count to drift.** The run above selected 89 tests; an earlier run selected 77.
TIA re-evaluates against whatever per-test coverage currently exists, so a file occasionally
joins or leaves the selected set. The shape — one hot node, three idle — is stable; the exact
count is not. Quote it from the run on screen rather than from this table.

**Why this leg must stay on plain `pytest`.** `DD_CIVISIBILITY_ITR_ENABLED` is a `ddtrace`
setting. It works here because pytest runs directly. It has **no effect** when `ddtest` drives
the run (as in B1), because `ddtest` deselects skippable tests before pytest starts. Do not
introduce `ddtest` into this workflow.

**Setup (once):** `preprod` must be in the Test Impact Analysis **excluded branches** list in
CI/CD Settings -> Repositories. Excluded branches still collect per-test coverage but never
skip, which is what makes `preprod` a valid seeding branch — Datadog does not backfill coverage
for Python. Symptom if missing: a push to `preprod` logs something like `5 passed, 960 skipped`
instead of re-seeding, and later demo PRs gradually stop skipping.

**Retuning durations**: the per-file budgets live in `scripts/domain_spec.json` as
`sleep_seconds` (150s total; 37s of it on `billing.calculator`). Change those and re-run
`python scripts/generate_test_modules.py && ruff format src tests scripts`. Never hand-edit
the generated test files — the next regeneration reverts them.

### B1 — Test Parallelization across 4-5 nodes (primary parallelization demo)

> **Every commit driving this demo must start with `ITR:NoSkip`**, including the empty ones used
> to re-trigger it. Without it the demo silently stops being a full-suite comparison *and* the
> split degrades to file-size guesswork. The `smart (plan)` job fails loudly if you forget.
> (B0 needs the exact opposite — never put `ITR:NoSkip` on the TIA demo.)

Picks up where B0 left off: B0 ended with one node doing all the work. Same 965-test suite, same
commit, the only difference is **how the files are distributed**.

| Leg | Split by | Nodes | Node test times | Slowest | Total compute |
| --- | --- | --- | --- | --- | --- |
| `naive` | file **count** | 4 (fixed) | 70.1 / 34.4 / 33.5 / 16.6 | **70.1s** | 154.6s |
| `smart` | **duration**, `ddtest` | 5 (ddtest chose) | 37.7 / 32.9 / 32.8 / 32.5 / 18.0 | **37.7s** | 153.8s |

Measured on PR #7, run 37056722490. Both legs ran all 965 tests.

**The story**: identical work, identical total compute — the slowest node drops from 70s to 38s
purely by deciding *which* files go where. `ddtest` put `test_calculator.py` on a node by itself
(72 tests, 37.7s) and packed 461 fast tests onto another that finished in 18s. The naive split
had no idea any of that mattered.

**"Why not just add more nodes?"** It chose 5 out of a permitted 8, and a 6th cannot help:
splitting is per *file*, and `test_calculator.py` alone is 37s. That is the floor, and it is why
node 0 sits at 37.7s. Good question to invite.

**Re-run the demo (PR #7 already exists — this is the normal path):**
```bash
git checkout parallel/typing-cleanup && git pull
git commit --allow-empty -m "ITR:NoSkip trigger parallelization demo" && git push
```

**Build it from scratch instead:**
```bash
git checkout preprod && git pull
git checkout -b parallel/typing-cleanup   # must NOT match demo/** or 4 extra workflows fire
# touch one line in each of src/analytics/metrics.py, src/auth/permissions.py,
#                          src/catalog/products.py, src/inventory/stock.py
git commit -am "ITR:NoSkip chore: tidy up domain helpers"
git push -u origin parallel/typing-cleanup
gh pr create --base preprod
```

**The edit must stay inside those four domains** — the workflow is path-filtered to
`src/{analytics,auth,catalog,inventory}/**` so it cannot fire on B0's PR. Edit elsewhere and
**nothing runs at all**; recover with `gh workflow run parallel-pr-demo.yml`.

**Quote test time, not job time.** Both `smart` jobs pay a sequential ~30s `plan` job on top, so
end to end `smart` is not much faster than `naive` here. Worth saying out loud: planning costs
~30s regardless of suite size — 20% of this 2.5-minute toy suite, noise on a 40-minute one.

**Required setup — seeding.** `ddtest` splits on Datadog p50 timings and falls back to file-size
weights without them, which are uncorrelated with this suite's artificial sleeps. Push to
`preprod` a few times first; the plan log should read `Backend durations used: 41 suites`. If it
reads `0 suites`, the plan job fails on purpose rather than showing a bad split.

**Why `DD_CIVISIBILITY_ITR_ENABLED` is not used here.** It is a `ddtrace` setting and has no
effect once `ddtest` drives the run — `ddtest` queries Datadog for skippable tests and deselects
them before pytest starts. Measured: a leg with that variable set to `"false"` still ran only 288
of 965 tests. `ITR:NoSkip` works because it acts on the API `ddtest` queries, and it clears both
problems at once:

```
without ITR:NoSkip   tiaSkippableTestsCount=677  ->  Backend durations used: 0  / Default: 41
with ITR:NoSkip      tiaSkippableTestsCount=0    ->  Backend durations used: 41 / Default: 0
```

### B2 — Combined optimization (manual, single pipeline)

1. Same billing change as B0
2. Run **Test - Optimized**
3. Show minimal tests + minimal nodes → ~1–2 min total

Superseded as a demo by B1's `tia-smart` leg, which shows the same thing against a visible
baseline. Kept for seeding `demo-optimized`.

---

## Part C: Flaky tests (~10 min)

### C1 — Auto Test Retries

1. Run **CI - Main Build** on `main`
2. Find a retry-recoverable test in `tests/flaky/test_retry_recoverable.py`
3. In Test Optimization Explorer, filter `@test.is_retry:true`
4. Show build passed despite initial failure

**Talking points**: `DD_CIVISIBILITY_FLAKY_RETRY_COUNT`, in-process retry, no pipeline re-run needed.

### C2 — Flaky test detection

1. Re-run **CI - Main Build** on the **same commit** 3–4 times (GitHub → Re-run all jobs)
2. Open **Flaky Tests** for the repository
3. Show intermittent tests from `tests/flaky/test_intermittent.py`: failure rate, first/last flaked

### C3 — Known flaky filter

1. Go to **Test Runs** → facet **Known Flaky: true**
2. Show failed runs tagged as known flaky vs new failures

### C4 — Early Flake Detection

1. Create branch `demo/introduce-flaky-test`
2. Copy the template: `cp tests/flaky/_template_test_new_flaky_efd.py tests/flaky/test_new_flaky_efd.py`
3. Open PR → **CI - PR Validation** runs
3. Find `@test.is_new:true` and EFD retries on the new test
4. Optionally configure a PR Gate to block merge

### C5 — TIA reduces flaky exposure

1. On a PR changing only `src/analytics/metrics.py`
2. Show flaky inventory/shipping tests are **skipped** by TIA
3. Unrelated flakes don't block the PR

---

## Demo branch recipes

```bash
# TIA demo — small targeted change
git checkout -b demo/tia-billing-fix
# edit src/billing/calculator.py (one line)
git commit -am "fix: billing tax rounding"
git push -u origin demo/tia-billing-fix

# EFD demo — copy template to create a genuinely new test
git checkout -b demo/introduce-flaky-test
cp tests/flaky/_template_test_new_flaky_efd.py tests/flaky/test_new_flaky_efd.py
git add tests/flaky/test_new_flaky_efd.py
git commit -m "feat: add checkout flow test"
git push -u origin demo/introduce-flaky-test

# Force full suite (escape hatch)
git commit -am "ITR:NoSkip chore: run all tests"
```

---

## Datadog links (US1)

- [CI Pipelines](https://app.datadoghq.com/ci/pipelines)
- [Test Runs](https://app.datadoghq.com/ci/test-runs)
- [Flaky Tests](https://app.datadoghq.com/ci/test-runs?query=test_level:test)
- [CI/CD Settings](https://app.datadoghq.com/ci/settings/ci-cd/repositories)
- [Test Impact Analysis Dashboard](https://app.datadoghq.com/dash/integration/30941/ci-visibility-intelligent-test-runner)
