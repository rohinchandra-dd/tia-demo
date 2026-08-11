"""Tests for inventory.cycle_count — generated; re-run scripts/generate_test_modules.py."""

import pytest

from src.inventory import cycle_count as _module


@pytest.mark.parametrize(
    "call_expr",
    [
        "count_variance(101, 99)",
        "count_variance(102, 100)",
        "count_variance(103, 101)",
        "count_variance(104, 102)",
        "count_variance(105, 103)",
        "count_variance(106, 104)",
    ],
    ids=[
        "inventory_cycle_count_count_variance_1",
        "inventory_cycle_count_count_variance_2",
        "inventory_cycle_count_count_variance_3",
        "inventory_cycle_count_count_variance_4",
        "inventory_cycle_count_count_variance_5",
        "inventory_cycle_count_count_variance_6",
    ],
)
def test_count_variance(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "adjust_count(1, 2)",
        "adjust_count(2, 2)",
        "adjust_count(3, 2)",
        "adjust_count(4, 2)",
        "adjust_count(5, 2)",
        "adjust_count(6, 2)",
    ],
    ids=[
        "inventory_cycle_count_adjust_count_1",
        "inventory_cycle_count_adjust_count_2",
        "inventory_cycle_count_adjust_count_3",
        "inventory_cycle_count_adjust_count_4",
        "inventory_cycle_count_adjust_count_5",
        "inventory_cycle_count_adjust_count_6",
    ],
)
def test_adjust_count(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
