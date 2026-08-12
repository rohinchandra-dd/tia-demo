"""New flaky tests for Early Flake Detection — added in PR demo/expand-flaky-tests-pr.

Datadog treats these as @test.is_new and retries them up to 10 times when EFD is enabled
on the demo-pr-validation service.
"""

from __future__ import annotations

import pytest

from src.catalog.products import product_sku
from src.notifications.sms import format_sms
from src.pricing.engine import base_price
from tests.flaky.conftest import efd_alternate

pytestmark = pytest.mark.flaky_demo


def test_new_checkout_payment_step():
    efd_alternate("efd_checkout_payment", "Simulated new checkout payment race (EFD)")
    assert product_sku(1001, "SKU") == "SKU-001001"


def test_new_checkout_confirmation_email():
    efd_alternate("efd_checkout_email", "Simulated new checkout email timing (EFD)")
    assert format_sms(1, 1.0) > 0


def test_new_subscription_renewal_pricing():
    efd_alternate("efd_subscription", "Simulated new subscription pricing flake (EFD)")
    assert base_price(100, 1.1) > 0


def test_new_cart_abandonment_tracker():
    efd_alternate("efd_cart_abandon", "Simulated new cart tracker race (EFD)")
    assert product_sku(42) == "SKU-000042"


def test_new_loyalty_points_accrual():
    efd_alternate("efd_loyalty", "Simulated new loyalty accrual flake (EFD)")
    assert base_price(50, 2.0) > 0


def test_new_sms_order_confirmation():
    efd_alternate("efd_sms_order", "Simulated new SMS confirmation timing (EFD)")
    assert format_sms(7, 1.5) > 0


def test_new_product_variant_selector():
    efd_alternate("efd_variant", "Simulated new variant selector race (EFD)")
    assert product_sku(7, "VAR") == "VAR-000007"


def test_new_dynamic_pricing_engine():
    efd_alternate("efd_dynamic_price", "Simulated new dynamic pricing flake (EFD)")
    assert base_price(200, 0.9) > 0
