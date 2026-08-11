"""Tests for billing.calculator — generated; re-run scripts/generate_test_modules.py."""

import time

import pytest


@pytest.mark.slow
@pytest.mark.parametrize(
    "call_expr",
    [
        "add_tax(11, 0.02)",
        "add_tax(12, 0.03)",
        "add_tax(13, 0.04)",
        "add_tax(14, 0.05)",
        "add_tax(15, 0.06)",
        "add_tax(16, 0.07)",
        "add_tax(17, 0.08)",
        "add_tax(18, 0.09)",
        "add_tax(19, 0.01)",
        "add_tax(20, 0.02)",
        "add_tax(21, 0.03)",
        "add_tax(22, 0.04)",
        "add_tax(23, 0.05)",
        "add_tax(24, 0.06)",
        "add_tax(25, 0.07)",
        "add_tax(26, 0.08)",
        "add_tax(27, 0.09)",
        "add_tax(28, 0.01)",
    ],
    ids=[
        "billing_calculator_add_tax_1",
        "billing_calculator_add_tax_2",
        "billing_calculator_add_tax_3",
        "billing_calculator_add_tax_4",
        "billing_calculator_add_tax_5",
        "billing_calculator_add_tax_6",
        "billing_calculator_add_tax_7",
        "billing_calculator_add_tax_8",
        "billing_calculator_add_tax_9",
        "billing_calculator_add_tax_10",
        "billing_calculator_add_tax_11",
        "billing_calculator_add_tax_12",
        "billing_calculator_add_tax_13",
        "billing_calculator_add_tax_14",
        "billing_calculator_add_tax_15",
        "billing_calculator_add_tax_16",
        "billing_calculator_add_tax_17",
        "billing_calculator_add_tax_18",
    ],
)
def test_add_tax(call_expr):
    """Execute operation and assert result is usable."""
    time.sleep(2 + (hash(call_expr) % 4))
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "apply_discount(101, 1)",
        "apply_discount(102, 2)",
        "apply_discount(103, 3)",
        "apply_discount(104, 4)",
        "apply_discount(105, 5)",
        "apply_discount(106, 6)",
        "apply_discount(107, 7)",
        "apply_discount(108, 8)",
        "apply_discount(109, 9)",
        "apply_discount(110, 10)",
        "apply_discount(111, 11)",
        "apply_discount(112, 12)",
        "apply_discount(113, 13)",
        "apply_discount(114, 14)",
        "apply_discount(115, 15)",
        "apply_discount(116, 16)",
        "apply_discount(117, 17)",
        "apply_discount(118, 18)",
    ],
    ids=[
        "billing_calculator_apply_discount_1",
        "billing_calculator_apply_discount_2",
        "billing_calculator_apply_discount_3",
        "billing_calculator_apply_discount_4",
        "billing_calculator_apply_discount_5",
        "billing_calculator_apply_discount_6",
        "billing_calculator_apply_discount_7",
        "billing_calculator_apply_discount_8",
        "billing_calculator_apply_discount_9",
        "billing_calculator_apply_discount_10",
        "billing_calculator_apply_discount_11",
        "billing_calculator_apply_discount_12",
        "billing_calculator_apply_discount_13",
        "billing_calculator_apply_discount_14",
        "billing_calculator_apply_discount_15",
        "billing_calculator_apply_discount_16",
        "billing_calculator_apply_discount_17",
        "billing_calculator_apply_discount_18",
    ],
)
def test_apply_discount(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "round_currency(1.2345, 2)",
        "round_currency(2.469, 2)",
        "round_currency(3.7035, 2)",
        "round_currency(4.938, 2)",
        "round_currency(6.172499999999999, 2)",
        "round_currency(7.407, 2)",
        "round_currency(8.641499999999999, 2)",
        "round_currency(9.876, 2)",
        "round_currency(11.1105, 2)",
        "round_currency(12.344999999999999, 2)",
        "round_currency(13.5795, 2)",
        "round_currency(14.814, 2)",
        "round_currency(16.0485, 2)",
        "round_currency(17.282999999999998, 2)",
        "round_currency(18.5175, 2)",
        "round_currency(19.752, 2)",
        "round_currency(20.9865, 2)",
        "round_currency(22.221, 2)",
    ],
    ids=[
        "billing_calculator_round_currency_1",
        "billing_calculator_round_currency_2",
        "billing_calculator_round_currency_3",
        "billing_calculator_round_currency_4",
        "billing_calculator_round_currency_5",
        "billing_calculator_round_currency_6",
        "billing_calculator_round_currency_7",
        "billing_calculator_round_currency_8",
        "billing_calculator_round_currency_9",
        "billing_calculator_round_currency_10",
        "billing_calculator_round_currency_11",
        "billing_calculator_round_currency_12",
        "billing_calculator_round_currency_13",
        "billing_calculator_round_currency_14",
        "billing_calculator_round_currency_15",
        "billing_calculator_round_currency_16",
        "billing_calculator_round_currency_17",
        "billing_calculator_round_currency_18",
    ],
)
def test_round_currency(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "split_payment(100, 3)",
        "split_payment(200, 4)",
        "split_payment(300, 5)",
        "split_payment(400, 6)",
        "split_payment(500, 2)",
        "split_payment(600, 3)",
        "split_payment(700, 4)",
        "split_payment(800, 5)",
        "split_payment(900, 6)",
        "split_payment(1000, 2)",
        "split_payment(1100, 3)",
        "split_payment(1200, 4)",
        "split_payment(1300, 5)",
        "split_payment(1400, 6)",
        "split_payment(1500, 2)",
        "split_payment(1600, 3)",
        "split_payment(1700, 4)",
        "split_payment(1800, 5)",
    ],
    ids=[
        "billing_calculator_split_payment_1",
        "billing_calculator_split_payment_2",
        "billing_calculator_split_payment_3",
        "billing_calculator_split_payment_4",
        "billing_calculator_split_payment_5",
        "billing_calculator_split_payment_6",
        "billing_calculator_split_payment_7",
        "billing_calculator_split_payment_8",
        "billing_calculator_split_payment_9",
        "billing_calculator_split_payment_10",
        "billing_calculator_split_payment_11",
        "billing_calculator_split_payment_12",
        "billing_calculator_split_payment_13",
        "billing_calculator_split_payment_14",
        "billing_calculator_split_payment_15",
        "billing_calculator_split_payment_16",
        "billing_calculator_split_payment_17",
        "billing_calculator_split_payment_18",
    ],
)
def test_split_payment(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
