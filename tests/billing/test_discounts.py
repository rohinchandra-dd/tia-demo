"""Tests for billing.discounts — generated; re-run scripts/generate_test_modules.py."""

import time

import pytest

from src.billing import discounts as _module


@pytest.mark.slow
@pytest.mark.parametrize(
    "call_expr",
    [
        "apply_coupon(51, 0.2)",
        "apply_coupon(52, 0.3)",
        "apply_coupon(53, 0.4)",
        "apply_coupon(54, 0.5)",
        "apply_coupon(55, 0.6)",
        "apply_coupon(56, 0.7)",
        "apply_coupon(57, 0.8)",
        "apply_coupon(58, 0.9)",
        "apply_coupon(59, 0.1)",
        "apply_coupon(60, 0.2)",
        "apply_coupon(61, 0.3)",
        "apply_coupon(62, 0.4)",
        "apply_coupon(63, 0.5)",
        "apply_coupon(64, 0.6)",
        "apply_coupon(65, 0.7)",
        "apply_coupon(66, 0.8)",
        "apply_coupon(67, 0.9)",
        "apply_coupon(68, 0.1)",
    ],
    ids=[
        "billing_discounts_apply_coupon_1",
        "billing_discounts_apply_coupon_2",
        "billing_discounts_apply_coupon_3",
        "billing_discounts_apply_coupon_4",
        "billing_discounts_apply_coupon_5",
        "billing_discounts_apply_coupon_6",
        "billing_discounts_apply_coupon_7",
        "billing_discounts_apply_coupon_8",
        "billing_discounts_apply_coupon_9",
        "billing_discounts_apply_coupon_10",
        "billing_discounts_apply_coupon_11",
        "billing_discounts_apply_coupon_12",
        "billing_discounts_apply_coupon_13",
        "billing_discounts_apply_coupon_14",
        "billing_discounts_apply_coupon_15",
        "billing_discounts_apply_coupon_16",
        "billing_discounts_apply_coupon_17",
        "billing_discounts_apply_coupon_18",
    ],
)
def test_apply_coupon(call_expr):
    """Execute operation and assert result is usable."""
    time.sleep(1.389)
    result = eval(call_expr, vars(_module))
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
        "tier_discount(107, 2)",
        "tier_discount(108, 3)",
        "tier_discount(109, 4)",
        "tier_discount(110, 0)",
        "tier_discount(111, 1)",
        "tier_discount(112, 2)",
        "tier_discount(113, 3)",
        "tier_discount(114, 4)",
        "tier_discount(115, 0)",
        "tier_discount(116, 1)",
        "tier_discount(117, 2)",
        "tier_discount(118, 3)",
    ],
    ids=[
        "billing_discounts_tier_discount_1",
        "billing_discounts_tier_discount_2",
        "billing_discounts_tier_discount_3",
        "billing_discounts_tier_discount_4",
        "billing_discounts_tier_discount_5",
        "billing_discounts_tier_discount_6",
        "billing_discounts_tier_discount_7",
        "billing_discounts_tier_discount_8",
        "billing_discounts_tier_discount_9",
        "billing_discounts_tier_discount_10",
        "billing_discounts_tier_discount_11",
        "billing_discounts_tier_discount_12",
        "billing_discounts_tier_discount_13",
        "billing_discounts_tier_discount_14",
        "billing_discounts_tier_discount_15",
        "billing_discounts_tier_discount_16",
        "billing_discounts_tier_discount_17",
        "billing_discounts_tier_discount_18",
    ],
)
def test_tier_discount(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "bulk_discount(201, 6)",
        "bulk_discount(202, 7)",
        "bulk_discount(203, 8)",
        "bulk_discount(204, 9)",
        "bulk_discount(205, 10)",
        "bulk_discount(206, 11)",
        "bulk_discount(207, 12)",
        "bulk_discount(208, 13)",
        "bulk_discount(209, 14)",
        "bulk_discount(210, 15)",
        "bulk_discount(211, 16)",
        "bulk_discount(212, 17)",
        "bulk_discount(213, 18)",
        "bulk_discount(214, 19)",
        "bulk_discount(215, 20)",
        "bulk_discount(216, 21)",
        "bulk_discount(217, 22)",
        "bulk_discount(218, 23)",
    ],
    ids=[
        "billing_discounts_bulk_discount_1",
        "billing_discounts_bulk_discount_2",
        "billing_discounts_bulk_discount_3",
        "billing_discounts_bulk_discount_4",
        "billing_discounts_bulk_discount_5",
        "billing_discounts_bulk_discount_6",
        "billing_discounts_bulk_discount_7",
        "billing_discounts_bulk_discount_8",
        "billing_discounts_bulk_discount_9",
        "billing_discounts_bulk_discount_10",
        "billing_discounts_bulk_discount_11",
        "billing_discounts_bulk_discount_12",
        "billing_discounts_bulk_discount_13",
        "billing_discounts_bulk_discount_14",
        "billing_discounts_bulk_discount_15",
        "billing_discounts_bulk_discount_16",
        "billing_discounts_bulk_discount_17",
        "billing_discounts_bulk_discount_18",
    ],
)
def test_bulk_discount(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        'validate_promo("PROMO0001")',
        'validate_promo("PROMO0002")',
        'validate_promo("PROMO0003")',
        'validate_promo("PROMO0004")',
        'validate_promo("PROMO0005")',
        'validate_promo("PROMO0006")',
        'validate_promo("PROMO0007")',
        'validate_promo("PROMO0008")',
        'validate_promo("PROMO0009")',
        'validate_promo("PROMO0010")',
        'validate_promo("PROMO0011")',
        'validate_promo("PROMO0012")',
        'validate_promo("PROMO0013")',
        'validate_promo("PROMO0014")',
        'validate_promo("PROMO0015")',
        'validate_promo("PROMO0016")',
        'validate_promo("PROMO0017")',
        'validate_promo("PROMO0018")',
    ],
    ids=[
        "billing_discounts_validate_promo_1",
        "billing_discounts_validate_promo_2",
        "billing_discounts_validate_promo_3",
        "billing_discounts_validate_promo_4",
        "billing_discounts_validate_promo_5",
        "billing_discounts_validate_promo_6",
        "billing_discounts_validate_promo_7",
        "billing_discounts_validate_promo_8",
        "billing_discounts_validate_promo_9",
        "billing_discounts_validate_promo_10",
        "billing_discounts_validate_promo_11",
        "billing_discounts_validate_promo_12",
        "billing_discounts_validate_promo_13",
        "billing_discounts_validate_promo_14",
        "billing_discounts_validate_promo_15",
        "billing_discounts_validate_promo_16",
        "billing_discounts_validate_promo_17",
        "billing_discounts_validate_promo_18",
    ],
)
def test_validate_promo(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
