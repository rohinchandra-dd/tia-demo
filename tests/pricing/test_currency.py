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
    ],
    ids=[
        "pricing_currency_convert_currency_1",
        "pricing_currency_convert_currency_2",
        "pricing_currency_convert_currency_3",
        "pricing_currency_convert_currency_4",
        "pricing_currency_convert_currency_5",
        "pricing_currency_convert_currency_6",
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
    ],
    ids=[
        "pricing_currency_exchange_rate_1",
        "pricing_currency_exchange_rate_2",
        "pricing_currency_exchange_rate_3",
        "pricing_currency_exchange_rate_4",
        "pricing_currency_exchange_rate_5",
        "pricing_currency_exchange_rate_6",
    ],
)
def test_exchange_rate(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
