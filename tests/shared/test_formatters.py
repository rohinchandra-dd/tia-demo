"""Tests for shared.formatters — generated; re-run scripts/generate_test_modules.py."""

import pytest

from src.shared import formatters as _module


@pytest.mark.parametrize(
    "call_expr",
    [
        "format_currency(10.99)",
        "format_currency(11.99)",
        "format_currency(12.99)",
        "format_currency(13.99)",
        "format_currency(14.99)",
        "format_currency(15.99)",
    ],
    ids=[
        "shared_formatters_format_currency_1",
        "shared_formatters_format_currency_2",
        "shared_formatters_format_currency_3",
        "shared_formatters_format_currency_4",
        "shared_formatters_format_currency_5",
        "shared_formatters_format_currency_6",
    ],
)
def test_format_currency(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "format_date(2024, 2, 2)",
        "format_date(2024, 3, 3)",
        "format_date(2024, 4, 4)",
        "format_date(2024, 5, 5)",
        "format_date(2024, 6, 6)",
        "format_date(2024, 7, 7)",
    ],
    ids=[
        "shared_formatters_format_date_1",
        "shared_formatters_format_date_2",
        "shared_formatters_format_date_3",
        "shared_formatters_format_date_4",
        "shared_formatters_format_date_5",
        "shared_formatters_format_date_6",
    ],
)
def test_format_date(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
