"""Shipping-domain flaky tests — TIA runs these when src/shipping/ changes."""

from __future__ import annotations

import pytest

from src.shipping.rates import calculate_rate, zone_rate
from src.shipping.tracking import eta_estimate, format_tracking_id
from tests.flaky.conftest import fail_once, maybe_flake

pytestmark = pytest.mark.flaky_demo


def test_shipping_rate_quote_timeout():
    fail_once("shipping_rate_quote", "Simulated carrier rate quote timeout")
    assert calculate_rate(5.0, 10.0, 0.5) > 0


def test_shipping_zone_lookup_retry():
    fail_once("shipping_zone", "Simulated zone lookup failure")
    assert zone_rate(10.0, 1.2) > 10.0


def test_shipping_eta_calculation_jitter():
    maybe_flake(0.35, "Simulated ETA calculation jitter")
    assert eta_estimate(3, 2) == 5


def test_shipping_tracking_id_format_race():
    maybe_flake(0.35, "Simulated tracking ID format race")
    assert format_tracking_id("abc123").startswith("TRK-")


def test_shipping_rate_cache_intermittent():
    maybe_flake(0.35, "Simulated shipping rate cache miss")
    assert calculate_rate(8.0, 5.0, 0.75) > 8.0
