"""Data-driven integration tests — unskippable for Test Impact Analysis demos."""

from __future__ import annotations

import pytest

from src.billing.calculator import add_tax, apply_discount
from src.pricing.engine import base_price


@pytest.mark.smoke
@pytest.mark.skipif(False, reason="datadog_itr_unskippable")
def test_orders_fixture_loaded(sample_orders):
    assert len(sample_orders) >= 3
    assert all("order_id" in order for order in sample_orders)


@pytest.mark.smoke
@pytest.mark.skipif(False, reason="datadog_itr_unskippable")
def test_pricing_rules_from_csv(pricing_rules):
    assert len(pricing_rules) >= 3
    assert pricing_rules[0]["rule_id"].startswith("R")


@pytest.mark.skipif(False, reason="datadog_itr_unskippable")
def test_order_tax_calculation(sample_orders):
    order = sample_orders[0]
    taxed = add_tax(order["amount"], 0.08)
    assert taxed > order["amount"]


@pytest.mark.skipif(False, reason="datadog_itr_unskippable")
def test_order_discount_pipeline(sample_orders):
    order = sample_orders[1]
    discounted = apply_discount(order["amount"], 10.0)
    assert discounted < order["amount"]


@pytest.mark.smoke
@pytest.mark.skipif(False, reason="datadog_itr_unskippable")
def test_base_price_from_catalog_rules(pricing_rules):
    rule = pricing_rules[0]
    price = base_price(100, float(rule["discount_pct"]))
    assert price > 0
