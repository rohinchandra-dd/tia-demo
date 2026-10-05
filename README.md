# Datadog CI/CD + Test Optimization Demo

A Python/pytest demo repository showcasing **CI Pipeline Visibility**, **Test Impact Analysis**, **Test Parallelization**, **Auto Test Retries**, and **Flaky Test Management** in Datadog.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Regenerate domain tests after editing scripts/domain_spec.json.
# The generator emits unformatted code, so always format afterwards or the
# PR Validation lint job fails and the diff looks far larger than it is.
python scripts/generate_test_modules.py && ruff format src tests scripts
# ...then re-seed Datadog, or both demos degrade silently:
scripts/seed_preprod.sh 3

# Run tests locally (skip slow tests for speed)
pytest -m "not slow" -q

# Run full suite
pytest -q
```

## Repository structure

| Path | Purpose |
| --- | --- |
| `src/` | 10 domain packages, ~40 pure-function modules |
| `tests/` | 972 tests: 960 parametrized domain + 5 integration + 7 flaky demos |
| `tests/flaky/` | Controlled flaky tests for retry/detection demos |
| `scripts/generate_test_modules.py` | Regenerates src + tests from `domain_spec.json` |
| `.github/workflows/` | 13 GitHub Actions pipelines (+ seed orchestrator, + preflight) |
| `scripts/seed_preprod.sh` | Re-seeds TIA coverage + ddtest p50 timings on `preprod` |
| `scripts/measure_job_overhead.py` | Measures real per-runner cost, to set `CI_JOB_OVERHEAD` from evidence |
| `scripts/cost_summary.py` | Renders the per-leg runners / wall / billed-minutes table |

## CI pipelines

Each workflow appears as a separate pipeline in [Datadog CI Visibility](https://app.datadoghq.com/ci/pipelines).

| Pipeline | Workflow | Trigger | Demo focus |
| --- | --- | --- | --- |
| Quick Smoke | `ci-quick-smoke.yml` | push to `main`, manual | Fast feedback (~1 min), populates Datadog quickly |
| PR Validation | `ci-pr-validation.yml` | PRs into `main` | Job DAG, TIA on PRs, smoke tests |
| Main Build | `ci-main-build.yml` | push to `main` | Sequential stages, deploy gate, auto retries |
| Nightly Regression | `ci-nightly-regression.yml` | cron + manual | Scheduled CI, ddtest parallelization |
| Hotfix Fast Path | `ci-hotfix-fast-path.yml` | manual | TIA + parallel on demand |
| **Seed Datadog Data** | `ci-seed-datadog.yml` | manual | **One-click: triggers all seed workflows** |
| Test Baseline | `test-baseline.yml` | manual / `demo/**` | _Seeding only_ — superseded as a demo by TIA PR Demo |
| Test Impact Analysis | `test-impact-analysis.yml` | manual / `demo/**` | _Seeding only_ — superseded as a demo by TIA PR Demo |
| Test Parallelization | `test-parallelization.yml` | manual / `demo/**` | ddtest matrix only |
| Test Optimized | `test-optimized.yml` | manual / `demo/**` | TIA + parallel combined |
| **TIA PR Demo** | `tia-pr-demo.yml` | PRs into `preprod` touching `src/{analytics,catalog,inventory,shared}/**` | **Baseline vs TIA across 4 nodes (8 checks)** — demo bars 1 and 2 |
| **Parallel PR Demo** | `parallel-pr-demo.yml` | PRs into `preprod` touching `src/{auth,compliance,notifications,shipping}/**` | **Naive 4 fixed runners vs TIA + ddtest right-sizing to 2** — demo bar 3, and the cost argument (9 billed minutes → 5) |
| **Demo Preflight** | `demo-preflight.yml` | manual | **GO/NO-GO check before a live demo** — runs no tests |

The two `paths` filters are deliberately disjoint so the two demo PRs never cross-trigger.
Because GitHub evaluates `paths` on a pull request against the three-dot diff, an **empty
commit** on either branch re-fires the whole demo — that is the live trigger.

### Test services (`DD_SERVICE`)

Each pipeline reports to a distinct test service for clean Datadog filtering:

- `demo-quick-smoke`, `demo-pr-validation`, `demo-main-build`, `demo-nightly`, `demo-hotfix`
- `demo-baseline`, `demo-tia`, `demo-parallel`, `demo-optimized`
- `demo-parallel-naive`, `demo-parallel-smart` (Parallel PR Demo legs)

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
| Test Impact Analysis | Enabled; exclude `main` **and `preprod`** (see DEMO.md B0) |
| Tracked files | `requirements.txt`, `pyproject.toml`, `scripts/generate_test_modules.py` — a PR touching any of these forces a full run |
| Auto Test Retries | Enabled for `demo-main-build`, `demo-pr-validation` |
| Early Flake Detection | Enabled for `demo-pr-validation` |

### 4. Seeding before a live demo

**For the TIA / Parallel PR demos (required after any `domain_spec.json` change):**

```bash
scripts/seed_preprod.sh 3      # lands 3 full runs on preprod, serially
gh workflow run demo-preflight.yml --ref preprod
```

Regenerating test files invalidates their per-test coverage and p50 timings, and both demos
**fail softly** when that data is cold — the TIA bar comes out level with the baseline bar and
`ddtest` falls back to weighting every suite at one second per test. Neither shows up as a failed run, so always
confirm **Demo Preflight** reports GO.

**Everything else — automated:** Actions → **CI - Seed Datadog Data** → Run workflow

Default options dispatch Quick Smoke, Main Build ×3, Nightly, Hotfix, PR Validation, Parallelization, and create `demo/seed-automation` for TIA/optimized test workflows.

Optional: enable slow baseline (~20 min), adjust main build repeat count.

See [DEMO.md](DEMO.md) for step-by-step demo scripts.

## Test suite highlights

- **972 tests**: 960 parametrized across 40 domain test files, 5 integration, 7 flaky.
  Demo workflows pass `--ignore=tests/flaky`, so they run **965** (regenerate for more via `domain_spec.json`)
- **TIA mapping**: `tests/billing/test_calculator.py` ↔ `src/billing/calculator.py`
- **Slow tests**: `@pytest.mark.slow` on 8 heavy modules; per-file budgets set by `sleep_seconds` in `domain_spec.json` (344s total, deterministic) — 30s on each `analytics` and `compliance` file, 40s on `billing.calculator` and `billing.discounts`, 1s on the 24 light modules. Duration is independent of test count: `heavy` controls how many tests a module emits, `sleep_seconds` how long they take
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
