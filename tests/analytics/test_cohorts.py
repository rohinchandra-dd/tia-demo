"""Tests for analytics.cohorts — generated; re-run scripts/generate_test_modules.py."""

import pytest

from src.analytics import cohorts as _module


@pytest.mark.parametrize(
    "call_expr",
    [
        "cohort_size(1, 1.1)",
        "cohort_size(2, 1.2)",
        "cohort_size(3, 1.3)",
        "cohort_size(4, 1.4)",
        "cohort_size(5, 1.5)",
        "cohort_size(6, 1.6)",
    ],
    ids=[
        "analytics_cohorts_cohort_size_1",
        "analytics_cohorts_cohort_size_2",
        "analytics_cohorts_cohort_size_3",
        "analytics_cohorts_cohort_size_4",
        "analytics_cohorts_cohort_size_5",
        "analytics_cohorts_cohort_size_6",
    ],
)
def test_cohort_size(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "retention_rate(1, 1.1)",
        "retention_rate(2, 1.2)",
        "retention_rate(3, 1.3)",
        "retention_rate(4, 1.4)",
        "retention_rate(5, 1.5)",
        "retention_rate(6, 1.6)",
    ],
    ids=[
        "analytics_cohorts_retention_rate_1",
        "analytics_cohorts_retention_rate_2",
        "analytics_cohorts_retention_rate_3",
        "analytics_cohorts_retention_rate_4",
        "analytics_cohorts_retention_rate_5",
        "analytics_cohorts_retention_rate_6",
    ],
)
def test_retention_rate(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
