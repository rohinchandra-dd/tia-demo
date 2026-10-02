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

### B0 — TIA side by side on a single PR (primary TIA demo)

One PR, exactly two checks, both running the same suite — 965 tests (972 minus the 7
flaky demo tests, which both legs `--ignore`):

| Job | TIA | Tests run | Test time | Job time |
| --- | --- | --- | --- | --- |
| `baseline` | disabled | 965 | 2m 32s | ~3m 00s |
| `tia` | enabled | 77 (888 skipped) | 39.7s | ~1m 15s |

Measured on PR #6. Job time includes ~35s of fixed setup (checkout, pip install, Datadog
agent config) on both legs, so quote the **test time** — that is what Datadog displays and it
is where the 3.8x difference actually lives.

**Setup (once):**
1. `preprod` branch exists and is **not** protected — this is what keeps the PR Signals
   required checks (`fast-test-job`, `slow-build-job`) off this PR.
2. **Required.** In CI/CD Settings -> Repositories, add `preprod` to the Test Impact Analysis
   **excluded branches** list. Excluded branches still collect per-test coverage but never
   skip, which is what makes `preprod` a valid seeding branch. Datadog does not backfill
   coverage for Python, so coverage only exists where a full run produced it.

   **Symptom if this is not set:** a push to `preprod` logs something like
   `5 passed, 960 skipped in 2.54s` — it skipped instead of re-seeding, so coverage goes
   stale and later demo PRs gradually stop skipping. A correct seed run logs
   `965 passed in ~2m32s`.
3. Push to `preprod` once and let `TIA PR Demo` run. That run executes the full suite and
   seeds coverage. **Do not demo on this run** — it correctly skips nothing.

**Re-run the demo (PR #6 already exists — this is the normal path):**
```bash
git checkout tia/add-tax-fix && git pull
git commit --allow-empty -m "Trigger TIA demo" && git push
```
Both jobs re-run on every push. Verified: `baseline` 965 passed in 152.55s,
`tia` 77 passed / 888 skipped in 38.42s. Repeat as often as you like.

**Build it from scratch instead:**
```bash
git checkout preprod && git pull
git checkout -b tia/add-tax-fix          # must NOT match demo/** or 4 extra workflows fire
# change one line inside add_tax() in src/billing/calculator.py
git commit -am "fix: billing tax rounding"
git push -u origin tia/add-tax-fix
gh pr create --base preprod
```

**Talking points**: both jobs run the identical pytest command on the identical commit — the
only difference is `DD_CIVISIBILITY_ITR_ENABLED`. TIA selected the 72 tests covering
`billing/calculator.py` plus the 5 unskippable integration tests, and skipped the other 888. Compare `demo-baseline` and `demo-tia` in Test Runs for the purple savings bar.

**The edit must be to `add_tax`.** TIA selects the whole `test_calculator.py` file either way,
but only `test_add_tax` carries the 37s of sleep, so the timing works regardless of which
function you touch in that file. Editing a module with no `sleep_seconds` budget (anything
outside the 8 heavy modules) drops the `tia` leg to a few seconds, which reads as "it did
nothing" rather than "it was fast".

**Optional**: add `ITR:NoSkip` to the commit message to force the full suite even on the
`tia` leg — useful for showing that the skipping is opt-out, not magic.

**Retuning durations**: the per-file budgets live in `scripts/domain_spec.json` as
`sleep_seconds` (150s total; 37s of it on `billing.calculator`). Change those and re-run
`python scripts/generate_test_modules.py && ruff format src tests scripts`. Never hand-edit
the generated test files — the next regeneration reverts them.

### B1 — Test Parallelization

1. Run **Test - Parallelization** on `main`
2. Show 4–8 parallel matrix jobs
3. Compare total wall-clock to baseline

### B2 — Combined optimization

1. Same billing change as B0
2. Run **Test - Optimized**
3. Show minimal tests + minimal nodes → ~1–2 min total

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
