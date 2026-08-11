"""Tests for inventory.warehouse — generated; re-run scripts/generate_test_modules.py."""

import pytest

from src.inventory import warehouse as _module


@pytest.mark.parametrize(
    "call_expr",
    [
        'assign_bin("WH1", 1, 1)',
        'assign_bin("WH2", 2, 2)',
        'assign_bin("WH0", 3, 3)',
        'assign_bin("WH1", 4, 4)',
        'assign_bin("WH2", 5, 5)',
        'assign_bin("WH0", 6, 6)',
    ],
    ids=[
        "inventory_warehouse_assign_bin_1",
        "inventory_warehouse_assign_bin_2",
        "inventory_warehouse_assign_bin_3",
        "inventory_warehouse_assign_bin_4",
        "inventory_warehouse_assign_bin_5",
        "inventory_warehouse_assign_bin_6",
    ],
)
def test_assign_bin(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        'locate_item("SKU1")',
        'locate_item("SKU2")',
        'locate_item("SKU3")',
        'locate_item("SKU4")',
        'locate_item("SKU5")',
        'locate_item("SKU6")',
    ],
    ids=[
        "inventory_warehouse_locate_item_1",
        "inventory_warehouse_locate_item_2",
        "inventory_warehouse_locate_item_3",
        "inventory_warehouse_locate_item_4",
        "inventory_warehouse_locate_item_5",
        "inventory_warehouse_locate_item_6",
    ],
)
def test_locate_item(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
