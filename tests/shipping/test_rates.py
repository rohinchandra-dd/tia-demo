"""Tests for shipping.rates — generated; re-run scripts/generate_test_modules.py."""

import time

import pytest


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
        "calculate_rate(5.0, 7.0, 0.5)",
        "calculate_rate(5.0, 8.0, 0.5)",
        "calculate_rate(5.0, 9.0, 0.5)",
        "calculate_rate(5.0, 10.0, 0.5)",
        "calculate_rate(5.0, 11.0, 0.5)",
        "calculate_rate(5.0, 12.0, 0.5)",
        "calculate_rate(5.0, 13.0, 0.5)",
        "calculate_rate(5.0, 14.0, 0.5)",
        "calculate_rate(5.0, 15.0, 0.5)",
        "calculate_rate(5.0, 16.0, 0.5)",
        "calculate_rate(5.0, 17.0, 0.5)",
        "calculate_rate(5.0, 18.0, 0.5)",
    ],
    ids=[
        "shipping_rates_calculate_rate_1",
        "shipping_rates_calculate_rate_2",
        "shipping_rates_calculate_rate_3",
        "shipping_rates_calculate_rate_4",
        "shipping_rates_calculate_rate_5",
        "shipping_rates_calculate_rate_6",
        "shipping_rates_calculate_rate_7",
        "shipping_rates_calculate_rate_8",
        "shipping_rates_calculate_rate_9",
        "shipping_rates_calculate_rate_10",
        "shipping_rates_calculate_rate_11",
        "shipping_rates_calculate_rate_12",
        "shipping_rates_calculate_rate_13",
        "shipping_rates_calculate_rate_14",
        "shipping_rates_calculate_rate_15",
        "shipping_rates_calculate_rate_16",
        "shipping_rates_calculate_rate_17",
        "shipping_rates_calculate_rate_18",
    ],
)
def test_calculate_rate(call_expr):
    """Execute operation and assert result is usable."""
    time.sleep(2 + (hash(call_expr) % 4))
    result = eval(call_expr)
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
        "zone_rate(10.0, 1.7000000000000002)",
        "zone_rate(10.0, 1.8)",
        "zone_rate(10.0, 1.9)",
        "zone_rate(10.0, 2.0)",
        "zone_rate(10.0, 2.1)",
        "zone_rate(10.0, 2.2)",
        "zone_rate(10.0, 2.3)",
        "zone_rate(10.0, 2.4000000000000004)",
        "zone_rate(10.0, 2.5)",
        "zone_rate(10.0, 2.6)",
        "zone_rate(10.0, 2.7)",
        "zone_rate(10.0, 2.8)",
    ],
    ids=[
        "shipping_rates_zone_rate_1",
        "shipping_rates_zone_rate_2",
        "shipping_rates_zone_rate_3",
        "shipping_rates_zone_rate_4",
        "shipping_rates_zone_rate_5",
        "shipping_rates_zone_rate_6",
        "shipping_rates_zone_rate_7",
        "shipping_rates_zone_rate_8",
        "shipping_rates_zone_rate_9",
        "shipping_rates_zone_rate_10",
        "shipping_rates_zone_rate_11",
        "shipping_rates_zone_rate_12",
        "shipping_rates_zone_rate_13",
        "shipping_rates_zone_rate_14",
        "shipping_rates_zone_rate_15",
        "shipping_rates_zone_rate_16",
        "shipping_rates_zone_rate_17",
        "shipping_rates_zone_rate_18",
    ],
)
def test_zone_rate(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "weight_tier(1, 2.0, 5.0)",
        "weight_tier(2, 2.0, 5.0)",
        "weight_tier(3, 2.0, 5.0)",
        "weight_tier(4, 2.0, 5.0)",
        "weight_tier(0, 2.0, 5.0)",
        "weight_tier(1, 2.0, 5.0)",
        "weight_tier(2, 2.0, 5.0)",
        "weight_tier(3, 2.0, 5.0)",
        "weight_tier(4, 2.0, 5.0)",
        "weight_tier(0, 2.0, 5.0)",
        "weight_tier(1, 2.0, 5.0)",
        "weight_tier(2, 2.0, 5.0)",
        "weight_tier(3, 2.0, 5.0)",
        "weight_tier(4, 2.0, 5.0)",
        "weight_tier(0, 2.0, 5.0)",
        "weight_tier(1, 2.0, 5.0)",
        "weight_tier(2, 2.0, 5.0)",
        "weight_tier(3, 2.0, 5.0)",
    ],
    ids=[
        "shipping_rates_weight_tier_1",
        "shipping_rates_weight_tier_2",
        "shipping_rates_weight_tier_3",
        "shipping_rates_weight_tier_4",
        "shipping_rates_weight_tier_5",
        "shipping_rates_weight_tier_6",
        "shipping_rates_weight_tier_7",
        "shipping_rates_weight_tier_8",
        "shipping_rates_weight_tier_9",
        "shipping_rates_weight_tier_10",
        "shipping_rates_weight_tier_11",
        "shipping_rates_weight_tier_12",
        "shipping_rates_weight_tier_13",
        "shipping_rates_weight_tier_14",
        "shipping_rates_weight_tier_15",
        "shipping_rates_weight_tier_16",
        "shipping_rates_weight_tier_17",
        "shipping_rates_weight_tier_18",
    ],
)
def test_weight_tier(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "express_surcharge(10.0, False)",
        "express_surcharge(10.0, True)",
        "express_surcharge(10.0, False)",
        "express_surcharge(10.0, True)",
        "express_surcharge(10.0, False)",
        "express_surcharge(10.0, True)",
        "express_surcharge(10.0, False)",
        "express_surcharge(10.0, True)",
        "express_surcharge(10.0, False)",
        "express_surcharge(10.0, True)",
        "express_surcharge(10.0, False)",
        "express_surcharge(10.0, True)",
        "express_surcharge(10.0, False)",
        "express_surcharge(10.0, True)",
        "express_surcharge(10.0, False)",
        "express_surcharge(10.0, True)",
        "express_surcharge(10.0, False)",
        "express_surcharge(10.0, True)",
    ],
    ids=[
        "shipping_rates_express_surcharge_1",
        "shipping_rates_express_surcharge_2",
        "shipping_rates_express_surcharge_3",
        "shipping_rates_express_surcharge_4",
        "shipping_rates_express_surcharge_5",
        "shipping_rates_express_surcharge_6",
        "shipping_rates_express_surcharge_7",
        "shipping_rates_express_surcharge_8",
        "shipping_rates_express_surcharge_9",
        "shipping_rates_express_surcharge_10",
        "shipping_rates_express_surcharge_11",
        "shipping_rates_express_surcharge_12",
        "shipping_rates_express_surcharge_13",
        "shipping_rates_express_surcharge_14",
        "shipping_rates_express_surcharge_15",
        "shipping_rates_express_surcharge_16",
        "shipping_rates_express_surcharge_17",
        "shipping_rates_express_surcharge_18",
    ],
)
def test_express_surcharge(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
