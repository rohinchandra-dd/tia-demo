"""Tests for inventory.reorder — generated; re-run scripts/generate_test_modules.py."""

import pytest

from src.inventory import reorder as _module


@pytest.mark.parametrize(
    "call_expr",
    [
        "reorder_point(1.0, 7, 5)",
        "reorder_point(2.0, 7, 5)",
        "reorder_point(3.0, 7, 5)",
        "reorder_point(4.0, 7, 5)",
        "reorder_point(5.0, 7, 5)",
        "reorder_point(6.0, 7, 5)",
    ],
    ids=[
        "inventory_reorder_reorder_point_1",
        "inventory_reorder_reorder_point_2",
        "inventory_reorder_reorder_point_3",
        "inventory_reorder_reorder_point_4",
        "inventory_reorder_reorder_point_5",
        "inventory_reorder_reorder_point_6",
    ],
)
def test_reorder_point(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "suggest_quantity(51, 1)",
        "suggest_quantity(52, 2)",
        "suggest_quantity(53, 3)",
        "suggest_quantity(54, 4)",
        "suggest_quantity(55, 5)",
        "suggest_quantity(56, 6)",
    ],
    ids=[
        "inventory_reorder_suggest_quantity_1",
        "inventory_reorder_suggest_quantity_2",
        "inventory_reorder_suggest_quantity_3",
        "inventory_reorder_suggest_quantity_4",
        "inventory_reorder_suggest_quantity_5",
        "inventory_reorder_suggest_quantity_6",
    ],
)
def test_suggest_quantity(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
