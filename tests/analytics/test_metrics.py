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
        "aggregate_sum(7, 1.7000000000000002)",
        "aggregate_sum(8, 1.8)",
        "aggregate_sum(9, 1.9)",
        "aggregate_sum(10, 2.0)",
        "aggregate_sum(11, 2.1)",
        "aggregate_sum(12, 2.2)",
        "aggregate_sum(13, 2.3)",
        "aggregate_sum(14, 2.4000000000000004)",
        "aggregate_sum(15, 2.5)",
        "aggregate_sum(16, 2.6)",
        "aggregate_sum(17, 2.7)",
        "aggregate_sum(18, 2.8)",
    ],
    ids=[
        "analytics_metrics_aggregate_sum_1",
        "analytics_metrics_aggregate_sum_2",
        "analytics_metrics_aggregate_sum_3",
        "analytics_metrics_aggregate_sum_4",
        "analytics_metrics_aggregate_sum_5",
        "analytics_metrics_aggregate_sum_6",
        "analytics_metrics_aggregate_sum_7",
        "analytics_metrics_aggregate_sum_8",
        "analytics_metrics_aggregate_sum_9",
        "analytics_metrics_aggregate_sum_10",
        "analytics_metrics_aggregate_sum_11",
        "analytics_metrics_aggregate_sum_12",
        "analytics_metrics_aggregate_sum_13",
        "analytics_metrics_aggregate_sum_14",
        "analytics_metrics_aggregate_sum_15",
        "analytics_metrics_aggregate_sum_16",
        "analytics_metrics_aggregate_sum_17",
        "analytics_metrics_aggregate_sum_18",
    ],
)
def test_aggregate_sum(call_expr):
    """Execute operation and assert result is usable."""
    time.sleep(2 + (hash(call_expr) % 4))
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
        "aggregate_avg(7, 1.7000000000000002)",
        "aggregate_avg(8, 1.8)",
        "aggregate_avg(9, 1.9)",
        "aggregate_avg(10, 2.0)",
        "aggregate_avg(11, 2.1)",
        "aggregate_avg(12, 2.2)",
        "aggregate_avg(13, 2.3)",
        "aggregate_avg(14, 2.4000000000000004)",
        "aggregate_avg(15, 2.5)",
        "aggregate_avg(16, 2.6)",
        "aggregate_avg(17, 2.7)",
        "aggregate_avg(18, 2.8)",
    ],
    ids=[
        "analytics_metrics_aggregate_avg_1",
        "analytics_metrics_aggregate_avg_2",
        "analytics_metrics_aggregate_avg_3",
        "analytics_metrics_aggregate_avg_4",
        "analytics_metrics_aggregate_avg_5",
        "analytics_metrics_aggregate_avg_6",
        "analytics_metrics_aggregate_avg_7",
        "analytics_metrics_aggregate_avg_8",
        "analytics_metrics_aggregate_avg_9",
        "analytics_metrics_aggregate_avg_10",
        "analytics_metrics_aggregate_avg_11",
        "analytics_metrics_aggregate_avg_12",
        "analytics_metrics_aggregate_avg_13",
        "analytics_metrics_aggregate_avg_14",
        "analytics_metrics_aggregate_avg_15",
        "analytics_metrics_aggregate_avg_16",
        "analytics_metrics_aggregate_avg_17",
        "analytics_metrics_aggregate_avg_18",
    ],
)
def test_aggregate_avg(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "percentile(1, 1.1)",
        "percentile(2, 1.2)",
        "percentile(3, 1.3)",
        "percentile(4, 1.4)",
        "percentile(5, 1.5)",
        "percentile(6, 1.6)",
        "percentile(7, 1.7000000000000002)",
        "percentile(8, 1.8)",
        "percentile(9, 1.9)",
        "percentile(10, 2.0)",
        "percentile(11, 2.1)",
        "percentile(12, 2.2)",
        "percentile(13, 2.3)",
        "percentile(14, 2.4000000000000004)",
        "percentile(15, 2.5)",
        "percentile(16, 2.6)",
        "percentile(17, 2.7)",
        "percentile(18, 2.8)",
    ],
    ids=[
        "analytics_metrics_percentile_1",
        "analytics_metrics_percentile_2",
        "analytics_metrics_percentile_3",
        "analytics_metrics_percentile_4",
        "analytics_metrics_percentile_5",
        "analytics_metrics_percentile_6",
        "analytics_metrics_percentile_7",
        "analytics_metrics_percentile_8",
        "analytics_metrics_percentile_9",
        "analytics_metrics_percentile_10",
        "analytics_metrics_percentile_11",
        "analytics_metrics_percentile_12",
        "analytics_metrics_percentile_13",
        "analytics_metrics_percentile_14",
        "analytics_metrics_percentile_15",
        "analytics_metrics_percentile_16",
        "analytics_metrics_percentile_17",
        "analytics_metrics_percentile_18",
    ],
)
def test_percentile(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "growth_rate(1, 1.1)",
        "growth_rate(2, 1.2)",
        "growth_rate(3, 1.3)",
        "growth_rate(4, 1.4)",
        "growth_rate(5, 1.5)",
        "growth_rate(6, 1.6)",
        "growth_rate(7, 1.7000000000000002)",
        "growth_rate(8, 1.8)",
        "growth_rate(9, 1.9)",
        "growth_rate(10, 2.0)",
        "growth_rate(11, 2.1)",
        "growth_rate(12, 2.2)",
        "growth_rate(13, 2.3)",
        "growth_rate(14, 2.4000000000000004)",
        "growth_rate(15, 2.5)",
        "growth_rate(16, 2.6)",
        "growth_rate(17, 2.7)",
        "growth_rate(18, 2.8)",
    ],
    ids=[
        "analytics_metrics_growth_rate_1",
        "analytics_metrics_growth_rate_2",
        "analytics_metrics_growth_rate_3",
        "analytics_metrics_growth_rate_4",
        "analytics_metrics_growth_rate_5",
        "analytics_metrics_growth_rate_6",
        "analytics_metrics_growth_rate_7",
        "analytics_metrics_growth_rate_8",
        "analytics_metrics_growth_rate_9",
        "analytics_metrics_growth_rate_10",
        "analytics_metrics_growth_rate_11",
        "analytics_metrics_growth_rate_12",
        "analytics_metrics_growth_rate_13",
        "analytics_metrics_growth_rate_14",
        "analytics_metrics_growth_rate_15",
        "analytics_metrics_growth_rate_16",
        "analytics_metrics_growth_rate_17",
        "analytics_metrics_growth_rate_18",
    ],
)
def test_growth_rate(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
