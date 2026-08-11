# Live Demo Script

Step-by-step scenarios for demonstrating Datadog CI/CD Optimization and Test Optimization.

## Prerequisites

- [ ] `DD_API_KEY` configured as GitHub secret
- [ ] GitHub App installed with CI Visibility enabled
- [ ] Test Impact Analysis enabled (exclude `main`)
- [ ] Auto Test Retries enabled for `demo-main-build`
- [ ] Early Flake Detection enabled for `demo-pr-validation`
- [ ] 3+ full runs on `main` completed (seeds coverage + flaky history)

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

### B1 — Baseline pain

1. Run **Test - Baseline** (`workflow_dispatch`)
2. Open Test Runs for service `demo-baseline`
3. Note ~970 tests, ~15–25 min duration, no purple TIA savings bar

### B2 — Test Impact Analysis

1. On branch `demo/tia-billing-fix`, change one line in `src/billing/calculator.py`
2. Run **Test - Impact Analysis** or push to `demo/tia-billing-fix`
3. Show ~60 tests run (calculator file only), purple savings in Test Runs

**Optional**: Add `ITR:NoSkip` to commit message to force full suite.

### B3 — Test Parallelization

1. Run **Test - Parallelization** on `main`
2. Show 4–8 parallel matrix jobs
3. Compare total wall-clock to baseline

### B4 — Combined optimization

1. Same billing change as B2
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
