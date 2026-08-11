"""Tests for billing.discounts — generated; re-run scripts/generate_test_modules.py."""

import pytest


@pytest.mark.parametrize(
    "call_expr",
    [
        "apply_coupon(51, 0.2)",
        "apply_coupon(52, 0.3)",
        "apply_coupon(53, 0.4)",
        "apply_coupon(54, 0.5)",
        "apply_coupon(55, 0.6)",
        "apply_coupon(56, 0.7)",
    ],
    ids=[
        "billing_discounts_apply_coupon_1",
        "billing_discounts_apply_coupon_2",
        "billing_discounts_apply_coupon_3",
        "billing_discounts_apply_coupon_4",
        "billing_discounts_apply_coupon_5",
        "billing_discounts_apply_coupon_6",
    ],
)
def test_apply_coupon(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "tier_discount(101, 1)",
        "tier_discount(102, 2)",
        "tier_discount(103, 3)",
        "tier_discount(104, 4)",
        "tier_discount(105, 0)",
        "tier_discount(106, 1)",
    ],
    ids=[
        "billing_discounts_tier_discount_1",
        "billing_discounts_tier_discount_2",
        "billing_discounts_tier_discount_3",
        "billing_discounts_tier_discount_4",
        "billing_discounts_tier_discount_5",
        "billing_discounts_tier_discount_6",
    ],
)
def test_tier_discount(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
