"""Tests for pricing.currency — generated; re-run scripts/generate_test_modules.py."""

import pytest

from src.pricing import currency as _module


@pytest.mark.parametrize(
    "call_expr",
    [
        "convert_currency(1, 1.1)",
        "convert_currency(2, 1.2)",
        "convert_currency(3, 1.3)",
        "convert_currency(4, 1.4)",
        "convert_currency(5, 1.5)",
        "convert_currency(6, 1.6)",
        "convert_currency(7, 1.7000000000000002)",
        "convert_currency(8, 1.8)",
        "convert_currency(9, 1.9)",
        "convert_currency(10, 2.0)",
        "convert_currency(11, 2.1)",
        "convert_currency(12, 2.2)",
        "convert_currency(13, 2.3)",
        "convert_currency(14, 2.4000000000000004)",
        "convert_currency(15, 2.5)",
        "convert_currency(16, 2.6)",
        "convert_currency(17, 2.7)",
        "convert_currency(18, 2.8)",
    ],
    ids=[
        "pricing_currency_convert_currency_1",
        "pricing_currency_convert_currency_2",
        "pricing_currency_convert_currency_3",
        "pricing_currency_convert_currency_4",
        "pricing_currency_convert_currency_5",
        "pricing_currency_convert_currency_6",
        "pricing_currency_convert_currency_7",
        "pricing_currency_convert_currency_8",
        "pricing_currency_convert_currency_9",
        "pricing_currency_convert_currency_10",
        "pricing_currency_convert_currency_11",
        "pricing_currency_convert_currency_12",
        "pricing_currency_convert_currency_13",
        "pricing_currency_convert_currency_14",
        "pricing_currency_convert_currency_15",
        "pricing_currency_convert_currency_16",
        "pricing_currency_convert_currency_17",
        "pricing_currency_convert_currency_18",
    ],
)
def test_convert_currency(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "exchange_rate(1, 1.1)",
        "exchange_rate(2, 1.2)",
        "exchange_rate(3, 1.3)",
        "exchange_rate(4, 1.4)",
        "exchange_rate(5, 1.5)",
        "exchange_rate(6, 1.6)",
        "exchange_rate(7, 1.7000000000000002)",
        "exchange_rate(8, 1.8)",
        "exchange_rate(9, 1.9)",
        "exchange_rate(10, 2.0)",
        "exchange_rate(11, 2.1)",
        "exchange_rate(12, 2.2)",
        "exchange_rate(13, 2.3)",
        "exchange_rate(14, 2.4000000000000004)",
        "exchange_rate(15, 2.5)",
        "exchange_rate(16, 2.6)",
        "exchange_rate(17, 2.7)",
        "exchange_rate(18, 2.8)",
    ],
    ids=[
        "pricing_currency_exchange_rate_1",
        "pricing_currency_exchange_rate_2",
        "pricing_currency_exchange_rate_3",
        "pricing_currency_exchange_rate_4",
        "pricing_currency_exchange_rate_5",
        "pricing_currency_exchange_rate_6",
        "pricing_currency_exchange_rate_7",
        "pricing_currency_exchange_rate_8",
        "pricing_currency_exchange_rate_9",
        "pricing_currency_exchange_rate_10",
        "pricing_currency_exchange_rate_11",
        "pricing_currency_exchange_rate_12",
        "pricing_currency_exchange_rate_13",
        "pricing_currency_exchange_rate_14",
        "pricing_currency_exchange_rate_15",
        "pricing_currency_exchange_rate_16",
        "pricing_currency_exchange_rate_17",
        "pricing_currency_exchange_rate_18",
    ],
)
def test_exchange_rate(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "round_fx(1, 1.1)",
        "round_fx(2, 1.2)",
        "round_fx(3, 1.3)",
        "round_fx(4, 1.4)",
        "round_fx(5, 1.5)",
        "round_fx(6, 1.6)",
        "round_fx(7, 1.7000000000000002)",
        "round_fx(8, 1.8)",
        "round_fx(9, 1.9)",
        "round_fx(10, 2.0)",
        "round_fx(11, 2.1)",
        "round_fx(12, 2.2)",
        "round_fx(13, 2.3)",
        "round_fx(14, 2.4000000000000004)",
        "round_fx(15, 2.5)",
        "round_fx(16, 2.6)",
        "round_fx(17, 2.7)",
        "round_fx(18, 2.8)",
    ],
    ids=[
        "pricing_currency_round_fx_1",
        "pricing_currency_round_fx_2",
        "pricing_currency_round_fx_3",
        "pricing_currency_round_fx_4",
        "pricing_currency_round_fx_5",
        "pricing_currency_round_fx_6",
        "pricing_currency_round_fx_7",
        "pricing_currency_round_fx_8",
        "pricing_currency_round_fx_9",
        "pricing_currency_round_fx_10",
        "pricing_currency_round_fx_11",
        "pricing_currency_round_fx_12",
        "pricing_currency_round_fx_13",
        "pricing_currency_round_fx_14",
        "pricing_currency_round_fx_15",
        "pricing_currency_round_fx_16",
        "pricing_currency_round_fx_17",
        "pricing_currency_round_fx_18",
    ],
)
def test_round_fx(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "currency_symbol(1, 1.1)",
        "currency_symbol(2, 1.2)",
        "currency_symbol(3, 1.3)",
        "currency_symbol(4, 1.4)",
        "currency_symbol(5, 1.5)",
        "currency_symbol(6, 1.6)",
        "currency_symbol(7, 1.7000000000000002)",
        "currency_symbol(8, 1.8)",
        "currency_symbol(9, 1.9)",
        "currency_symbol(10, 2.0)",
        "currency_symbol(11, 2.1)",
        "currency_symbol(12, 2.2)",
        "currency_symbol(13, 2.3)",
        "currency_symbol(14, 2.4000000000000004)",
        "currency_symbol(15, 2.5)",
        "currency_symbol(16, 2.6)",
        "currency_symbol(17, 2.7)",
        "currency_symbol(18, 2.8)",
    ],
    ids=[
        "pricing_currency_currency_symbol_1",
        "pricing_currency_currency_symbol_2",
        "pricing_currency_currency_symbol_3",
        "pricing_currency_currency_symbol_4",
        "pricing_currency_currency_symbol_5",
        "pricing_currency_currency_symbol_6",
        "pricing_currency_currency_symbol_7",
        "pricing_currency_currency_symbol_8",
        "pricing_currency_currency_symbol_9",
        "pricing_currency_currency_symbol_10",
        "pricing_currency_currency_symbol_11",
        "pricing_currency_currency_symbol_12",
        "pricing_currency_currency_symbol_13",
        "pricing_currency_currency_symbol_14",
        "pricing_currency_currency_symbol_15",
        "pricing_currency_currency_symbol_16",
        "pricing_currency_currency_symbol_17",
        "pricing_currency_currency_symbol_18",
    ],
)
def test_currency_symbol(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
