# Live Demo Script

Step-by-step scenarios for demonstrating Datadog CI/CD Optimization and Test Optimization.

## Prerequisites

- [ ] `DD_API_KEY` configured as GitHub secret
- [ ] GitHub App installed with CI Visibility enabled
- [ ] Test Impact Analysis enabled (exclude `main` **and `preprod`** — see B0)
- [ ] Auto Test Retries enabled for `demo-main-build` and `demo-flake-prevention`
- [ ] PR Comments enabled for the repository (CI/CD Settings → Repositories → General)
- [ ] Early Flake Detection enabled for `demo-flake-prevention` — **after** the Flake Prevention
      workflow has run on `preprod` once (see C4)
- [ ] New Flaky Test PR Gate rule created and scoped to this repository (see C6)
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

**Do not skip the cost line — it is the one an exec remembers.** The runner count is visible
in the Actions UI (two `tia-parallel (node N)` jobs against four `naive` ones); the billed
minutes are not, so quote them from here:

| leg | runners | wall clock | runner-seconds | billed minutes |
| --- | --- | --- | --- | --- |
| `naive` | 4 | 230s | 444s | **9** |
| `tia-parallel` | **2** | 133s | 230s | **5** |

To regenerate that table for any run — worth doing once before the webinar so the numbers on
screen are the ones you quote:

```bash
gh api "repos/rohinchandra-dd/tia-demo/actions/runs/<RUN_ID>/jobs" --paginate \
  --jq '.jobs[] | {name, started_at, completed_at}' | python3 scripts/cost_summary.py
```

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

## Part C: Flaky tests (~15 min)

Parts A and B are about *seeing* the problem. Part C is about the three features that stop it:
retries absorb a known flake, Early Flake Detection catches an unknown one, and the PR Gate
refuses to let it reach the trunk.

Everything from C1 on reports to `demo-flake-prevention` and runs through
`flake-prevention-pr-demo.yml`, the only workflow that runs `tests/flaky/` on a pull request.

### C1 — Auto Test Retries

1. Open the flake-prevention PR and its **`flaky-suite`** check. It is **green**.
2. Open `tests/flaky/test_retry_recoverable.py` and read the mechanism out loud: a module-level
   counter, `if _attempts["payment"] == 1: pytest.fail(...)`. It fails its **first attempt, every
   single run**. A green check is only possible because something retried it in-process.
3. Datadog's **PR comment** on the PR lists the retried tests and their error messages.
4. Test Runs → `@test.retry_reason:auto_test_retry` → the failed first attempt and the passing
   retry, same commit, same process.

**Talking points**: `DD_CIVISIBILITY_FLAKY_RETRY_COUNT` (5 here), in-process, no pipeline re-run,
no `pytest-rerunfailures` — the tracer does it. Contrast with `test-baseline.yml`, which sets
`DD_CIVISIBILITY_FLAKY_RETRY_ENABLED: "false"` and therefore has to `--ignore=tests/flaky`
entirely.

### C2 — Flaky test detection

1. Re-run **Flake Prevention PR Demo** on the **same commit** 3–4 times.
2. Open **Flaky Tests** for the repository.
3. `tests/flaky/test_intermittent.py` — four tests at a 35% failure rate — shows failure rate and
   first/last flaked. These are *known* flakes: Datadog has watched them fail before.

### C3 — Known flaky filter

1. Test Runs → facet **Known Flaky: true**.
2. The point of the facet: a failure that is already understood is noise, and the ones that are
   not are the signal. C4 is about the second kind.

### C4 — Early Flake Detection

The PR adds exactly one file, `tests/flaky/test_checkout_timing.py`, and nothing else. It reads
like an ordinary feature PR; nobody labelled the test as risky.

1. Show the diff — one new test, `test_checkout_total_recalculation_latency`. It is deliberately written
   the way a real test would be: the alternating module-level counter is the only thing odd
   about it, and nobody reviewing the PR flagged it. (The template it was copied from is
   `tests/flaky/_template_test_new_flaky_efd.py`, underscore-prefixed so pytest skips it.)
2. Test Runs → `@test.is_new:true` on this commit. Datadog has never seen this test, because it is
   absent from the known-tests baseline it keeps for `demo-flake-prevention`.
3. The job log names the reason in plain text — and it is a *different* reason from every other
   test in the same run:

   ```
   test_checkout_total_recalculation_latency RETRY FAILED (Early Flake Detection)
   test_checkout_total_recalculation_latency RETRY PASSED (Early Flake Detection)
   test_checkout_total_recalculation_latency FLAKY
   test_payment_gateway_timeout              RETRY FAILED (Auto Test Retries)
   test_payment_gateway_timeout              RETRY PASSED (Auto Test Retries)
   test_payment_gateway_timeout              PASSED
   ```

   EFD is budgeted for up to ten attempts but stops as soon as the answer is settled: one fail
   and one pass is already a mixed result, so it marks the test **FLAKY** and moves on. Contrast
   the verdicts — the known flake ends `PASSED` (retries did their job), the new one ends `FLAKY`.
4. `@test.retry_reason:early_flake_detection` isolates those attempts; the test is tagged
   `@test.test_management.is_new_flaky:true`.

**The ordering that makes this work**: EFD's "is this new?" question is answered against a baseline
kept **per test service**. `demo-flake-prevention` is a new service, so the Flake Prevention
workflow must run on `preprod` (its push leg) *before* EFD is switched on — otherwise all seven
pre-existing flaky tests are new too and the demo loses its point.

> [!IMPORTANT]
> **Pick a test name Datadog has not seen, every time you rebuild this demo.** The baseline is
> keyed on the test's name, and it records a test the first time it *runs* — whether or not EFD
> was enabled at the time. So a dry run on the branch before switching EFD on silently burns the
> name: the next run retries it under Auto Test Retries (3 attempts, `retry_reason:auto_test_retry`)
> instead of EFD (10 attempts, `retry_reason:early_flake_detection`), and the gate never fires.
>
> Check before pushing — if this returns anything, choose another name:
> ```
> @test.service:demo-flake-prevention @test.name:<your_test_name>
> ```
> Names already burned on this service: `test_new_checkout_flow_timing`,
> `test_checkout_total_recalculation_timing`, `test_checkout_total_recalculation_latency`.

### C5 — The New Flaky Test PR Gate

1. Back to the PR's checks — there are exactly two:

   | check | result |
   | --- | --- |
   | `flaky-suite` | **pass** |
   | `Datadog PR Gates / No new flaky tests` | **fail** |

   **Green build, red gate.**
   That contrast is the whole argument. Retries did their job — the build is not broken — and the
   gate still caught the flake being introduced.
2. Click the red check → the gate detail in Datadog names `test_new_checkout_flow_timing`.
3. If the gate is a required check on `preprod`, GitHub will not let the PR merge.

**Talking points**: the gate is authored by the Datadog GitHub App from a UI rule — there is no
`datadog-ci` call and no extra credential in `flake-prevention-pr-demo.yml`. It is advisory until
someone marks it required in branch protection. Re-running the GitHub check does **not** re-evaluate
the rule; a new commit does.

### C6 — Clearing the gate

The check stays red until the test is marked **Fixed** in Flaky Tests Management. Two routes:

- **Attempt To Fix** (the one to show): open the test → **Actions → Link commit to fix** → copy the
  `DD_`-prefixed key → push a fix with that key in the commit body. The library reruns the test and
  verifies the fix.
- Or set the state from Active to Fixed by hand.

Leave the demo PR red. It is the artifact.

### C7 — TIA reduces flaky exposure

1. On a PR changing only `src/analytics/metrics.py` (the B0 PR).
2. Flaky inventory/shipping tests are **skipped** by TIA — unrelated flakes don't block the PR.
3. This is the cheap half of the story and worth naming as such: TIA reduces *exposure* to flakes.
   It does not detect them. C4 and C5 do.

---

## Demo branch recipes

```bash
# TIA demo — small targeted change
git checkout -b demo/tia-billing-fix
# edit src/billing/calculator.py (one line)
git commit -am "fix: billing tax rounding"
git push -u origin demo/tia-billing-fix

# EFD / PR Gate demo — copy template to create a genuinely new test.
# Base on preprod: the `tests/flaky/**` path filter on flake-prevention-pr-demo.yml
# makes `flaky-suite` the only check, and no other demo PR is disturbed.
# RENAME THE TEST FUNCTION to something this service has never run (see C4) --
# a name already in the known-tests baseline is not new, and EFD will skip it.
git checkout -b demo/introduce-flaky-test origin/preprod
cp tests/flaky/_template_test_new_flaky_efd.py tests/flaky/test_checkout_timing.py
$EDITOR tests/flaky/test_checkout_timing.py   # rename test_checkout_flow_timing_RENAME_ME
git add tests/flaky/test_checkout_timing.py
git commit -m "feat: add checkout flow test"
git push -u origin demo/introduce-flaky-test
gh pr create --base preprod --title "feat: add checkout flow timing test"

# The branch name matches `demo/**`, which the four seeding workflows also watch.
# They carry `paths-ignore: tests/flaky/**` so they stay off this branch and the
# PR shows the single `flaky-suite` check.

# Re-fire the whole flake demo (three-dot diff still matches tests/flaky/**)
git commit --allow-empty -m demo && git push

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
