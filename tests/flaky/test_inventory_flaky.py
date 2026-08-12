"""Inventory-domain flaky tests — TIA runs these when src/inventory/ changes."""

from __future__ import annotations

import pytest

from src.inventory.reorder import reorder_point, suggest_quantity
from src.inventory.stock import check_stock, reserve_stock
from src.inventory.warehouse import warehouse_capacity
from tests.flaky.conftest import fail_once, maybe_flake

pytestmark = pytest.mark.flaky_demo


def test_inventory_reservation_timeout():
    fail_once("inventory_reserve", "Simulated stock reservation timeout")
    assert reserve_stock(100, 10) == 90


def test_inventory_reorder_calculation_retry():
    fail_once("inventory_reorder", "Simulated reorder calculation failure")
    assert reorder_point(5.0, 7, 10) > 0


def test_inventory_stock_check_race():
    maybe_flake(0.35, "Simulated stock check race")
    assert check_stock(50, 10) is True


def test_inventory_warehouse_capacity_jitter():
    maybe_flake(0.35, "Simulated warehouse capacity jitter")
    assert warehouse_capacity(1000, 200) == 800


def test_inventory_suggest_quantity_intermittent():
    maybe_flake(0.35, "Simulated suggest quantity flake")
    assert suggest_quantity(100, 40) == 60
