"""Intermittent flaky tests — probabilistic failures for Flaky Test Management demos."""

from __future__ import annotations

import pytest

from src.inventory.stock import check_stock, stock_level
from src.notifications.email import validate_recipient
from src.shipping.tracking import track_status
from tests.flaky.conftest import maybe_flake


@pytest.mark.flaky_demo
def test_inventory_cache_race():
    maybe_flake(0.35, "Simulated inventory cache race condition")
    assert check_stock(100, 10) is True


@pytest.mark.flaky_demo
def test_email_delivery_timing():
    maybe_flake(0.35, "Simulated SMTP timing flake")
    assert validate_recipient(1, 1.0) > 0


@pytest.mark.flaky_demo
def test_tracking_webhook_delay():
    maybe_flake(0.35, "Simulated carrier webhook delay")
    assert track_status("shipped") == "shipped"


@pytest.mark.flaky_demo
def test_stock_level_threshold_jitter():
    maybe_flake(0.35, "Simulated stock threshold jitter")
    assert stock_level(5, 10) == "low"
