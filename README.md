# Datadog CI/CD + Test Optimization Demo

A Python/pytest demo repository showcasing **CI Pipeline Visibility**, **Test Impact Analysis**, **Test Parallelization**, **Auto Test Retries**, and **Flaky Test Management** in Datadog.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Regenerate domain tests after editing scripts/domain_spec.json
python scripts/generate_test_modules.py

# Run tests locally (skip slow tests for speed)
pytest -m "not slow" -q

# Run full suite
pytest -q
```

## Repository structure

| Path | Purpose |
| --- | --- |
| `src/` | 10 domain packages, ~40 pure-function modules |
| `tests/` | ~970 parametrized tests + integration + flaky demos |
| `tests/flaky/` | Controlled flaky tests for retry/detection demos |
| `scripts/generate_test_modules.py` | Regenerates src + tests from `domain_spec.json` |
| `.github/workflows/` | 10 GitHub Actions pipelines (+ seed orchestrator) |

## CI pipelines

Each workflow appears as a separate pipeline in [Datadog CI Visibility](https://app.datadoghq.com/ci/pipelines).

| Pipeline | Workflow | Trigger | Demo focus |
| --- | --- | --- | --- |
| Quick Smoke | `ci-quick-smoke.yml` | push to `main`, manual | Fast feedback (~1 min), populates Datadog quickly |
| PR Validation | `ci-pr-validation.yml` | `pull_request` | Job DAG, TIA on PRs, smoke tests |
| Main Build | `ci-main-build.yml` | push to `main` | Sequential stages, deploy gate, auto retries |
| Nightly Regression | `ci-nightly-regression.yml` | cron + manual | Scheduled CI, ddtest parallelization |
| Hotfix Fast Path | `ci-hotfix-fast-path.yml` | manual | TIA + parallel on demand |
| **Seed Datadog Data** | `ci-seed-datadog.yml` | manual | **One-click: triggers all seed workflows** |
| Test Baseline | `test-baseline.yml` | manual / `demo/**` | Full suite, no optimization |
| Test Impact Analysis | `test-impact-analysis.yml` | manual / `demo/**` | TIA only |
| Test Parallelization | `test-parallelization.yml` | manual / `demo/**` | ddtest matrix only |
| Test Optimized | `test-optimized.yml` | manual / `demo/**` | TIA + parallel combined |

### Test services (`DD_SERVICE`)

Each pipeline reports to a distinct test service for clean Datadog filtering:

- `demo-quick-smoke`, `demo-pr-validation`, `demo-main-build`, `demo-nightly`, `demo-hotfix`
- `demo-baseline`, `demo-tia`, `demo-parallel`, `demo-optimized`

## Datadog setup

### 1. GitHub secret

Add `DD_API_KEY` in **Settings → Secrets and variables → Actions**.

### 2. GitHub App (CI Pipeline Visibility)

You have `DD_API_KEY`; enable pipeline visibility via the GitHub App:

1. [GitHub integration](https://app.datadoghq.com/integrations/github/) → **Create GitHub App**
2. Permissions: **Actions: Read** + **Software Delivery: Collect Pull Request Information**
3. Install the app on this repository
4. [Enable CI Visibility](https://app.datadoghq.com/ci/setup/pipeline?provider=github) for the repo

### 3. Test Optimization settings

In [CI/CD Optimization → Settings → Repositories](https://app.datadoghq.com/ci/settings/ci-cd/repositories):

| Setting | Recommended value |
| --- | --- |
| Test Impact Analysis | Enabled; exclude `main` |
| Tracked files | `requirements.txt`, `pyproject.toml`, `scripts/generate_test_modules.py` |
| Auto Test Retries | Enabled for `demo-main-build`, `demo-pr-validation` |
| Early Flake Detection | Enabled for `demo-pr-validation` |

### 4. Seeding before a live demo

**Automated (recommended):** Actions → **CI - Seed Datadog Data** → Run workflow

Default options dispatch Quick Smoke, Main Build ×3, Nightly, Hotfix, PR Validation, Parallelization, and create `demo/seed-automation` for TIA/optimized test workflows.

Optional: enable slow baseline (~20 min), adjust main build repeat count.

See [DEMO.md](DEMO.md) for step-by-step demo scripts.

## Test suite highlights

- **~970 tests** across 40 domain test files (regenerate for more via `domain_spec.json`)
- **TIA mapping**: `tests/billing/test_calculator.py` ↔ `src/billing/calculator.py`
- **Slow tests**: `@pytest.mark.slow` on heavy modules (~2–6s each) for parallelization demos
- **Unskippable**: `tests/integration/test_data_driven.py` reads `fixtures/`
- **Flaky demos**: `tests/flaky/` — retry-recoverable, intermittent, and EFD scenarios

## Key constraints

- Do **not** use `pytest-cov` or `pytest-xdist` (incompatible with TIA coverage)
- Checkout uses `fetch-depth: 0` for TIA and flaky git history
- `.testoptimization/` is gitignored — generated per CI run by `ddtest`

## References

- [Test Impact Analysis](https://docs.datadoghq.com/tests/test_impact_analysis/)
- [Test Parallelization](https://docs.datadoghq.com/tests/test_parallelization/)
- [Auto Test Retries](https://docs.datadoghq.com/tests/flaky_tests/auto_test_retries/?tab=python)
- [Flaky Test Management](https://docs.datadoghq.com/tests/flaky_tests/)
- [GitHub Actions CI Visibility](https://docs.datadoghq.com/continuous_integration/pipelines/github/)
