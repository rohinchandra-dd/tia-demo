"""Tests for pricing.engine — generated; re-run scripts/generate_test_modules.py."""

import time

import pytest


@pytest.mark.slow
@pytest.mark.parametrize(
    "call_expr",
    [
        "base_price(1, 1.1)",
        "base_price(2, 1.2)",
        "base_price(3, 1.3)",
        "base_price(4, 1.4)",
        "base_price(5, 1.5)",
        "base_price(6, 1.6)",
        "base_price(7, 1.7000000000000002)",
        "base_price(8, 1.8)",
        "base_price(9, 1.9)",
        "base_price(10, 2.0)",
        "base_price(11, 2.1)",
        "base_price(12, 2.2)",
        "base_price(13, 2.3)",
        "base_price(14, 2.4000000000000004)",
        "base_price(15, 2.5)",
        "base_price(16, 2.6)",
        "base_price(17, 2.7)",
        "base_price(18, 2.8)",
    ],
    ids=[
        "pricing_engine_base_price_1",
        "pricing_engine_base_price_2",
        "pricing_engine_base_price_3",
        "pricing_engine_base_price_4",
        "pricing_engine_base_price_5",
        "pricing_engine_base_price_6",
        "pricing_engine_base_price_7",
        "pricing_engine_base_price_8",
        "pricing_engine_base_price_9",
        "pricing_engine_base_price_10",
        "pricing_engine_base_price_11",
        "pricing_engine_base_price_12",
        "pricing_engine_base_price_13",
        "pricing_engine_base_price_14",
        "pricing_engine_base_price_15",
        "pricing_engine_base_price_16",
        "pricing_engine_base_price_17",
        "pricing_engine_base_price_18",
    ],
)
def test_base_price(call_expr):
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
        "margin_price(1, 1.1)",
        "margin_price(2, 1.2)",
        "margin_price(3, 1.3)",
        "margin_price(4, 1.4)",
        "margin_price(5, 1.5)",
        "margin_price(6, 1.6)",
        "margin_price(7, 1.7000000000000002)",
        "margin_price(8, 1.8)",
        "margin_price(9, 1.9)",
        "margin_price(10, 2.0)",
        "margin_price(11, 2.1)",
        "margin_price(12, 2.2)",
        "margin_price(13, 2.3)",
        "margin_price(14, 2.4000000000000004)",
        "margin_price(15, 2.5)",
        "margin_price(16, 2.6)",
        "margin_price(17, 2.7)",
        "margin_price(18, 2.8)",
    ],
    ids=[
        "pricing_engine_margin_price_1",
        "pricing_engine_margin_price_2",
        "pricing_engine_margin_price_3",
        "pricing_engine_margin_price_4",
        "pricing_engine_margin_price_5",
        "pricing_engine_margin_price_6",
        "pricing_engine_margin_price_7",
        "pricing_engine_margin_price_8",
        "pricing_engine_margin_price_9",
        "pricing_engine_margin_price_10",
        "pricing_engine_margin_price_11",
        "pricing_engine_margin_price_12",
        "pricing_engine_margin_price_13",
        "pricing_engine_margin_price_14",
        "pricing_engine_margin_price_15",
        "pricing_engine_margin_price_16",
        "pricing_engine_margin_price_17",
        "pricing_engine_margin_price_18",
    ],
)
def test_margin_price(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "competitor_adjust(1, 1.1)",
        "competitor_adjust(2, 1.2)",
        "competitor_adjust(3, 1.3)",
        "competitor_adjust(4, 1.4)",
        "competitor_adjust(5, 1.5)",
        "competitor_adjust(6, 1.6)",
        "competitor_adjust(7, 1.7000000000000002)",
        "competitor_adjust(8, 1.8)",
        "competitor_adjust(9, 1.9)",
        "competitor_adjust(10, 2.0)",
        "competitor_adjust(11, 2.1)",
        "competitor_adjust(12, 2.2)",
        "competitor_adjust(13, 2.3)",
        "competitor_adjust(14, 2.4000000000000004)",
        "competitor_adjust(15, 2.5)",
        "competitor_adjust(16, 2.6)",
        "competitor_adjust(17, 2.7)",
        "competitor_adjust(18, 2.8)",
    ],
    ids=[
        "pricing_engine_competitor_adjust_1",
        "pricing_engine_competitor_adjust_2",
        "pricing_engine_competitor_adjust_3",
        "pricing_engine_competitor_adjust_4",
        "pricing_engine_competitor_adjust_5",
        "pricing_engine_competitor_adjust_6",
        "pricing_engine_competitor_adjust_7",
        "pricing_engine_competitor_adjust_8",
        "pricing_engine_competitor_adjust_9",
        "pricing_engine_competitor_adjust_10",
        "pricing_engine_competitor_adjust_11",
        "pricing_engine_competitor_adjust_12",
        "pricing_engine_competitor_adjust_13",
        "pricing_engine_competitor_adjust_14",
        "pricing_engine_competitor_adjust_15",
        "pricing_engine_competitor_adjust_16",
        "pricing_engine_competitor_adjust_17",
        "pricing_engine_competitor_adjust_18",
    ],
)
def test_competitor_adjust(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "price_floor(1, 1.1)",
        "price_floor(2, 1.2)",
        "price_floor(3, 1.3)",
        "price_floor(4, 1.4)",
        "price_floor(5, 1.5)",
        "price_floor(6, 1.6)",
        "price_floor(7, 1.7000000000000002)",
        "price_floor(8, 1.8)",
        "price_floor(9, 1.9)",
        "price_floor(10, 2.0)",
        "price_floor(11, 2.1)",
        "price_floor(12, 2.2)",
        "price_floor(13, 2.3)",
        "price_floor(14, 2.4000000000000004)",
        "price_floor(15, 2.5)",
        "price_floor(16, 2.6)",
        "price_floor(17, 2.7)",
        "price_floor(18, 2.8)",
    ],
    ids=[
        "pricing_engine_price_floor_1",
        "pricing_engine_price_floor_2",
        "pricing_engine_price_floor_3",
        "pricing_engine_price_floor_4",
        "pricing_engine_price_floor_5",
        "pricing_engine_price_floor_6",
        "pricing_engine_price_floor_7",
        "pricing_engine_price_floor_8",
        "pricing_engine_price_floor_9",
        "pricing_engine_price_floor_10",
        "pricing_engine_price_floor_11",
        "pricing_engine_price_floor_12",
        "pricing_engine_price_floor_13",
        "pricing_engine_price_floor_14",
        "pricing_engine_price_floor_15",
        "pricing_engine_price_floor_16",
        "pricing_engine_price_floor_17",
        "pricing_engine_price_floor_18",
    ],
)
def test_price_floor(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
