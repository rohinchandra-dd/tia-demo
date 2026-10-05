# Live Demo Script

Step-by-step scenarios for demonstrating Datadog CI/CD Optimization and Test Optimization.

## Prerequisites

- [ ] `DD_API_KEY` configured as GitHub secret
- [ ] GitHub App installed with CI Visibility enabled
- [ ] Test Impact Analysis enabled (exclude `main` **and `preprod`** — see B0)
- [ ] Auto Test Retries enabled for `demo-main-build`
- [ ] Early Flake Detection enabled for `demo-pr-validation`
- [ ] Run `scripts/seed_preprod.sh 3` — required after ANY `scripts/domain_spec.json` change
- [ ] Run the **Demo Preflight** workflow and confirm it reports **GO** (see B1)
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

### B0 — Test Impact Analysis across 4 nodes (bars 1 and 2)

> **The commit message must NOT contain `ITR:NoSkip`.** That flag forces the full suite and
> would disable the very skipping this demo exists to show.

One PR (#6), 8 checks. Both legs run the identical 965-test suite, split across the same 4
nodes by the same naive file-count shard. The only difference is `DD_CIVISIBILITY_ITR_ENABLED`.

| Leg | node 0 | node 1 | node 2 | node 3 | Slowest | Total compute |
| --- | --- | --- | --- | --- | --- | --- |
| `baseline` | 240 passed **204s** | 240 passed 124s | 173 passed 8s | 312 passed 8s | **204s** | 344s |
| `tia` | 48 passed, 192 skipped **120s** | 48 passed, 192 skipped **4s** | 53 passed, 120 skipped **4s** | 48 passed, 264 skipped **4s** | **120s** | 132s |

> These are **modelled** from `scripts/domain_spec.json`, not measured — the budgets were
> retuned and the suite has not been re-run since. Replace this table with real numbers from
> the first green run, and quote **test time**, not job time: both legs pay ~25s of fixed
> setup (checkout, pip, Datadog agent).

**The two things to say:**

1. *"TIA skipped 768 of 965 tests. The slowest node went from 204 seconds to 120, and total
   compute from 344 to 132 — we are paying for a third of the machine time."*
2. *"But look at the distribution. Every node is running the same **number** of tests — 48 —
   and node 0 takes two minutes while the other three take four seconds. TIA removed the work;
   it did nothing about how the remainder is spread."*

That second point is the entire setup for B1, and it is engineered: the PR touches one domain
per shard, so the counts come out identical and only `analytics` (30s per file) carries
duration.

**Re-run the demo (PR #6 already exists — this is the normal path):**
```bash
git checkout tia/add-tax-fix && git pull
git commit --allow-empty -m "Trigger TIA demo" && git push
```

**The edit must touch `src/{analytics,catalog,inventory,shared}/**`** — one file in each. That
is both what the workflow is path-filtered on and what produces the equal-count/unequal-duration
picture. `analytics` is the load-bearing one: it is the only selected domain with a real
`sleep_seconds` budget, and it sits in shard 0. Drop it and every node finishes in about a
second, which reads as "nothing happened".

What TIA *removes* from node 0 is `billing.calculator` + `billing.discounts`, 40s each. Those
two files are the entire visible saving on the hot node, so they must stay out of the PR.

**If a `tia` node runs materially more than the count in the table, the data is stale, not the
spec.** Datadog cannot skip a test whose per-test coverage it does not have, and regenerating
test files invalidates that coverage. Observed on run 37068525851: `billing` and `compliance`
both ran in full on a PR touching neither, right after a `domain_spec.json` retune, and the TIA
bar came out level with the baseline bar. Fix with `scripts/seed_preprod.sh 3` — never by
retuning the spec.

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
`sleep_seconds` (344s total: 30s on each of the 4 `analytics` and 4 `compliance` files, 40s on
each of `billing.calculator` and `billing.discounts`, 1s on the 24 light modules). Change those,
then run `python scripts/generate_test_modules.py && ruff format src tests scripts`, **then
`scripts/seed_preprod.sh 3`**. Never hand-edit the generated test files — the next regeneration
reverts them.

### B1 — TIA + Test Parallelization (bar 3)

Picks up exactly where B0 left off: B0 ended with one node doing all the work. PR #7, same
suite, same 4-node naive split on the `naive` leg. The `tia-parallel` leg runs the **same kind
of TIA-selected set** (132s of work, mirrored against B0's) but lets `ddtest` decide which files
go on which node, by measured duration instead of by count.

| Leg | Split by | Nodes | Node test times | Slowest | Plan overhead |
| --- | --- | --- | --- | --- | --- |
| `naive` | file **count**, all 965 tests | 4 (fixed) | 204 / 124 / 8 / 8 | **204s** | — |
| `tia-parallel` | **duration**, TIA-selected set | 4 (ddtest chose) | ~33 / 33 / 33 / 33 | **~33s** | ~40s sequential `plan` job |

> Also modelled. 132s of selected work over 4 nodes, floor set by the largest single selected
> file (one `compliance` module at 30s), so ~33s per node is the honest optimum.

**The story**: *"Same PR, same selected tests. The only thing that changed is which node each
file landed on — and now all four finish together instead of one carrying everything. We pay
about 40 seconds up front for the planning job, and still come out well ahead."*

**"Why not just add more nodes?"** `MAX_PARALLELISM` is capped at 4 on purpose. Splitting is per
*file*, and one compliance file is 30s — that is the floor. Left at 8, ddtest picks 6 and two
nodes finish in ~4s, which costs compute and undercuts the point. Good question to invite.

**Re-run the demo (PR #7 already exists — this is the normal path):**
```bash
git checkout parallel/typing-cleanup && git pull
git commit --allow-empty -m "Trigger parallelization demo" && git push
```

**The edit must stay inside `src/{auth,compliance,notifications,shipping}/**`** — the workflow is
path-filtered to those four so it cannot fire on B0's PR, and they are deliberately disjoint
from B0's four. `compliance` is the load-bearing one (30s per file). Edit elsewhere and
**nothing runs at all**; recover with `gh workflow run parallel-pr-demo.yml`.

**Quote test time, not job time.** The `plan` job is sequential and costs ~40s on top of the
node time. Worth saying out loud: planning costs roughly that much regardless of suite size —
a third of this toy suite, noise on a 40-minute one.

#### ⚠️ Known issue: `Backend durations used: 0 suites`

`ddtest` splits on Datadog p50 timings and falls back to **file-size** weights without them.
File size is uncorrelated with this suite's artificial sleeps, so the fallback produces a split
no better than naive — measured on run 37066726705 as 29/27/141/141s — and it still reports as a
**green, successful run**. Nothing about the Actions UI tells you it happened.

There are two candidate causes and they have **different fixes**:

1. **Cold or stale timings.** Regenerating test files invalidates p50s for
   `demo-parallel-smart`. Fix: `scripts/seed_preprod.sh 3`.
2. **TIA skipping suppresses the durations lookup.** Measured earlier in this repo's history:

   ```
   without ITR:NoSkip   tiaSkippableTestsCount=677  ->  Backend durations used: 0  / Default: 41
   with ITR:NoSkip      tiaSkippableTestsCount=0    ->  Backend durations used: 41 / Default: 0
   ```

   If this is the real cause, no amount of seeding fixes it, and the choice is between a
   *duration-balanced* bar 3 (add `ITR:NoSkip`, full suite, parallelization only) and a
   *TIA-selected* bar 3 (leave it, accept a worse split). The current workflow leaves TIA on.

**Settle it before the webinar:** Actions → **Demo Preflight** → Run workflow. It runs the same
`ddtest plan` the demo will run and answers GO / NO-GO on exactly this, without running a single
test. The `tia-parallel (plan)` job in the demo itself only *warns* about this — deliberately,
since a red X mid-webinar is worse than a degraded bar.

**Why `DD_CIVISIBILITY_ITR_ENABLED` is not used here.** It is a `ddtrace` setting and has no
effect once `ddtest` drives the run — `ddtest` queries Datadog for skippable tests and deselects
them before pytest starts. Measured: a leg with that variable set to `"false"` still ran only 288
of 965 tests. `ITR:NoSkip` works because it acts on the API `ddtest` queries.

### B2 — Combined optimization (manual, single pipeline)

1. Same analytics/catalog/inventory/shared change as B0
2. Run **Test - Optimized**
3. Show minimal tests + minimal nodes → ~1–2 min total

Superseded as a demo by B1's `tia-parallel` leg, which shows the same thing against a visible
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
