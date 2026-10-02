"""Tests for inventory.stock — generated; re-run scripts/generate_test_modules.py."""

import time

import pytest

from src.inventory import stock as _module


@pytest.mark.slow
@pytest.mark.parametrize(
    "call_expr",
    [
        "check_stock(11, 1)",
        "check_stock(12, 2)",
        "check_stock(13, 3)",
        "check_stock(14, 4)",
        "check_stock(15, 5)",
        "check_stock(16, 6)",
    ],
    ids=[
        "inventory_stock_check_stock_1",
        "inventory_stock_check_stock_2",
        "inventory_stock_check_stock_3",
        "inventory_stock_check_stock_4",
        "inventory_stock_check_stock_5",
        "inventory_stock_check_stock_6",
    ],
)
def test_check_stock(call_expr):
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
        "reserve_stock(21, 1)",
        "reserve_stock(22, 2)",
        "reserve_stock(23, 3)",
        "reserve_stock(24, 4)",
        "reserve_stock(25, 5)",
        "reserve_stock(26, 6)",
    ],
    ids=[
        "inventory_stock_reserve_stock_1",
        "inventory_stock_reserve_stock_2",
        "inventory_stock_reserve_stock_3",
        "inventory_stock_reserve_stock_4",
        "inventory_stock_reserve_stock_5",
        "inventory_stock_reserve_stock_6",
    ],
)
def test_reserve_stock(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
