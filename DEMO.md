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

| Leg | node 0 | node 1 | node 2 | node 3 | Slowest job |
| --- | --- | --- | --- | --- | --- |
| `baseline` | 240 passed **204s** | 240 passed 131s | 173 passed 7s | 312 passed 10s | **232s** |
| `tia` | 48 passed, 192 skipped **120.9s** | 48 passed, 192 skipped **5.3s** | 53 passed, 120 skipped **5.0s** | 48 passed, 264 skipped **4.8s** | **146s** |

> Measured on PR #6, run 37250036732 (2026-10-05). Test times in the cells, slowest **job**
> time in the last column — both legs pay ~25s of fixed setup (checkout, pip, Datadog agent).
> Quote whichever you use consistently; the job times are what the Actions UI shows.

**The two things to say:**

1. *"TIA skipped 768 of 965 tests. The slowest node went from 204 seconds to 121, and total
   compute from 344 to 136 — we are paying for a third of the machine time."*
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

| Leg | Split by | Runners | Node **job** times | Wall | Billed minutes |
| --- | --- | --- | --- | --- | --- |
| `naive` | file **count**, all 965 tests | 4 (fixed) | 230 / 153 / 31 / 30 | **230s** | **9** |
| `tia-parallel` | TIA-selected set, 17 of 41 files | **2** (ddtest chose) | 100 / 101 | **133s** | **5** |

> Measured on PR #7, run 37329187588 (2026-10-05). The `tia-parallel` wall and bill include
> its 29s sequential `plan` job. The planner was allowed 4 runners and **chose 2**, and the
> two nodes land within **1 second** of each other.

This is the bar that carries the **cost** argument, so lead with the last column.

**The story**: *"The planner was allowed four runners and decided it only needed two. Same
selected tests, both nodes finish within a second of each other, and we come in at 133 seconds
against the naive split's 230 — on half the machines. The bill goes from nine minutes to
five."*

**Do not skip the cost line — it is the one an exec remembers.** The `cost summary` job at the
bottom of every run prints it automatically:

| leg | runners | wall clock | runner-seconds | billed minutes |
| --- | --- | --- | --- | --- |
| `naive` | 4 | 230s | 444s | **9** |
| `tia-parallel` | **2** | 133s | 230s | **5** |

#### Why it chose 2, and why that is the cost story

`ddtest` scores every candidate as `wall + runners x CI_JOB_OVERHEAD` and takes the minimum,
so `CI_JOB_OVERHEAD` is where you tell it what a runner costs you. From this run's plan log:

```
  2 runners: wall 1m48s, overhead 2m0s, score 3m48s, selected
  3 runners: wall 1m12s, overhead 3m0s, score 4m12s
```

We set it to **60s**, and that number is derived, not chosen to look good:

- `scripts/measure_job_overhead.py` measures real per-runner waste as
  `queue + job wall - pytest time`. Pooled over 13 runner jobs across 4 runs: **p50 30s**.
- But raw seconds are not the bill. **GitHub bills each job separately and rounds every one up
  to a whole minute**, so a runner's marginal cost never falls below 60s however briefly it
  runs.

That rounding is the whole point. Before this change, at 4 runners, `tia-parallel` billed
**9 minutes — exactly what `naive` billed** — while running a fifth of the tests. Every second
saved was handed straight back as per-job rounding. Two runners cuts it to 5.

If someone asks whether 60s is a fudge: the honest stopwatch number, 30s, selects **3**
runners, by only 6s over 2 — inside the noise of the measurement. Say so. It is the billing
model, not the stopwatch, that makes the decision stable.

`MAX_PARALLELISM` stays at 4 so this is like-for-like with the `naive` leg beside it. The cap
is not what reduced the runner count.

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

#### Resolved: why the plan reports `Backend durations used: 0 suites`

**TIA skipping suppresses the duration lookup.** Measured on the same commit, 2026-10-05:

| Run | Test skipping | TIA skippables returned | Backend durations |
| --- | --- | --- | --- |
| preprod push (37249726282) | disabled (excluded branch) | — | **41 suites** |
| PR #7 (37250040102) | enabled | 764 tests | **0 suites** / Default: 41 |

So on a demo PR this is **expected and permanent** — re-seeding cannot change it, and the
`plan` job says so rather than sending you to `seed_preprod.sh`. It is only a real problem when
skipping is *off* and durations are still 0, which means the service is genuinely cold.

**What it falls back to is one second per test** — not file size, which earlier versions of
these docs claimed. From the same plan log:

```
test_calculator.py  (72 tests, heavy)  ->  historical duration 1m12s = 72s
tests/auth/test_mfa.py  (12 tests)     ->  historical duration   12s = 12s
```

So on a demo PR the planner sees the selected set as **17 identical 12s suites**, and its
candidate walls are exactly `ceil(17/n) x 12` = 204 / 108 / 72 / 60. Two things follow, and
both matter:

- **Our `sleep_seconds` budgets are invisible to the planner.** Retuning durations cannot
  change how many runners it picks, or how it distributes files. Only `CI_JOB_OVERHEAD` and
  the number of selected files can.
- **The node balance is not guaranteed.** The 4-node run came out at 61/62/61/64s because the
  four 30s `compliance` files landed on separate nodes — an artifact of the planner's
  distribution order over equal-weight files, not something it reasoned about. Re-check the
  node times whenever the runner count or the selected set changes.

**Seeding still matters, for the `naive` bar and for Datadog's p50s.** Those lag several runs
behind: immediately after the retune the planner still quoted `test_cohorts.py` at 24.227s and
`test_calculator.py` at 27.868s — values from *two* retunes earlier. Three seeding rounds moved
`test_calculator` to 36.874s and the planner's imbalance estimate from 14.8s to 5.0s. Run
`scripts/seed_preprod.sh 3` after any `domain_spec.json` change, then **Demo Preflight**.

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
