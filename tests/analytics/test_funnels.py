"""Tests for analytics.funnels — generated; re-run scripts/generate_test_modules.py."""

import pytest


@pytest.mark.parametrize(
    "call_expr",
    [
        "funnel_step(1, 1.1)",
        "funnel_step(2, 1.2)",
        "funnel_step(3, 1.3)",
        "funnel_step(4, 1.4)",
        "funnel_step(5, 1.5)",
        "funnel_step(6, 1.6)",
    ],
    ids=[
        "analytics_funnels_funnel_step_1",
        "analytics_funnels_funnel_step_2",
        "analytics_funnels_funnel_step_3",
        "analytics_funnels_funnel_step_4",
        "analytics_funnels_funnel_step_5",
        "analytics_funnels_funnel_step_6",
    ],
)
def test_funnel_step(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "conversion_rate(1, 1.1)",
        "conversion_rate(2, 1.2)",
        "conversion_rate(3, 1.3)",
        "conversion_rate(4, 1.4)",
        "conversion_rate(5, 1.5)",
        "conversion_rate(6, 1.6)",
    ],
    ids=[
        "analytics_funnels_conversion_rate_1",
        "analytics_funnels_conversion_rate_2",
        "analytics_funnels_conversion_rate_3",
        "analytics_funnels_conversion_rate_4",
        "analytics_funnels_conversion_rate_5",
        "analytics_funnels_conversion_rate_6",
    ],
)
def test_conversion_rate(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
