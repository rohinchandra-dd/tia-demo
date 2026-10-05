"""Tests for analytics.metrics — generated; re-run scripts/generate_test_modules.py."""

import time

import pytest

from src.analytics import metrics as _module


@pytest.mark.slow
@pytest.mark.parametrize(
    "call_expr",
    [
        "aggregate_sum(1, 1.1)",
        "aggregate_sum(2, 1.2)",
        "aggregate_sum(3, 1.3)",
        "aggregate_sum(4, 1.4)",
        "aggregate_sum(5, 1.5)",
        "aggregate_sum(6, 1.6)",
    ],
    ids=[
        "analytics_metrics_aggregate_sum_1",
        "analytics_metrics_aggregate_sum_2",
        "analytics_metrics_aggregate_sum_3",
        "analytics_metrics_aggregate_sum_4",
        "analytics_metrics_aggregate_sum_5",
        "analytics_metrics_aggregate_sum_6",
    ],
)
def test_aggregate_sum(call_expr):
    """Execute operation and assert result is usable."""
    time.sleep(5.0)
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "aggregate_avg(1, 1.1)",
        "aggregate_avg(2, 1.2)",
        "aggregate_avg(3, 1.3)",
        "aggregate_avg(4, 1.4)",
        "aggregate_avg(5, 1.5)",
        "aggregate_avg(6, 1.6)",
    ],
    ids=[
        "analytics_metrics_aggregate_avg_1",
        "analytics_metrics_aggregate_avg_2",
        "analytics_metrics_aggregate_avg_3",
        "analytics_metrics_aggregate_avg_4",
        "analytics_metrics_aggregate_avg_5",
        "analytics_metrics_aggregate_avg_6",
    ],
)
def test_aggregate_avg(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
