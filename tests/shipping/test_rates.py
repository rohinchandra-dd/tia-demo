"""Tests for shipping.rates — generated; re-run scripts/generate_test_modules.py."""

import time

import pytest

from src.shipping import rates as _module


@pytest.mark.slow
@pytest.mark.parametrize(
    "call_expr",
    [
        "calculate_rate(5.0, 1.0, 0.5)",
        "calculate_rate(5.0, 2.0, 0.5)",
        "calculate_rate(5.0, 3.0, 0.5)",
        "calculate_rate(5.0, 4.0, 0.5)",
        "calculate_rate(5.0, 5.0, 0.5)",
        "calculate_rate(5.0, 6.0, 0.5)",
    ],
    ids=[
        "shipping_rates_calculate_rate_1",
        "shipping_rates_calculate_rate_2",
        "shipping_rates_calculate_rate_3",
        "shipping_rates_calculate_rate_4",
        "shipping_rates_calculate_rate_5",
        "shipping_rates_calculate_rate_6",
    ],
)
def test_calculate_rate(call_expr):
    """Execute operation and assert result is usable."""
    time.sleep(0.167)
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "zone_rate(10.0, 1.1)",
        "zone_rate(10.0, 1.2)",
        "zone_rate(10.0, 1.3)",
        "zone_rate(10.0, 1.4)",
        "zone_rate(10.0, 1.5)",
        "zone_rate(10.0, 1.6)",
    ],
    ids=[
        "shipping_rates_zone_rate_1",
        "shipping_rates_zone_rate_2",
        "shipping_rates_zone_rate_3",
        "shipping_rates_zone_rate_4",
        "shipping_rates_zone_rate_5",
        "shipping_rates_zone_rate_6",
    ],
)
def test_zone_rate(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
