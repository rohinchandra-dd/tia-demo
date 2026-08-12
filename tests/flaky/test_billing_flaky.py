"""Billing-domain flaky tests — TIA runs these when src/billing/ changes."""

from __future__ import annotations

import pytest

from src.billing.calculator import add_tax, apply_discount
from src.billing.invoicing import sum_line_items, validate_invoice
from tests.flaky.conftest import fail_once, maybe_flake

pytestmark = pytest.mark.flaky_demo


def test_billing_tax_service_timeout():
    fail_once("billing_tax", "Simulated billing tax service timeout")
    assert add_tax(100.0, 0.08) > 100.0


def test_billing_discount_api_retry():
    fail_once("billing_discount", "Simulated discount API unavailable")
    assert apply_discount(50.0, 5.0) == 45.0


def test_billing_invoice_validation_race():
    maybe_flake(0.35, "Simulated invoice validation race")
    assert validate_invoice(100.0, [{"amount": 50}, {"amount": 50}]) is True


def test_billing_line_items_aggregation_jitter():
    maybe_flake(0.35, "Simulated line item aggregation jitter")
    items = [{"amount": 10}, {"amount": 20}, {"amount": 30}]
    assert sum_line_items(items) == 60


def test_billing_rounding_intermittent():
    maybe_flake(0.35, "Simulated currency rounding flake")
    assert add_tax(19.99, 0.07) > 19.99
