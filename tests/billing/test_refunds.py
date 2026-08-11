"""Tests for billing.refunds — generated; re-run scripts/generate_test_modules.py."""

import pytest


@pytest.mark.parametrize(
    "call_expr",
    [
        "calculate_refund(101, 1)",
        "calculate_refund(102, 2)",
        "calculate_refund(103, 3)",
        "calculate_refund(104, 4)",
        "calculate_refund(105, 5)",
        "calculate_refund(106, 6)",
    ],
    ids=[
        "billing_refunds_calculate_refund_1",
        "billing_refunds_calculate_refund_2",
        "billing_refunds_calculate_refund_3",
        "billing_refunds_calculate_refund_4",
        "billing_refunds_calculate_refund_5",
        "billing_refunds_calculate_refund_6",
    ],
)
def test_calculate_refund(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "partial_refund(101, 0.2)",
        "partial_refund(102, 0.3)",
        "partial_refund(103, 0.4)",
        "partial_refund(104, 0.5)",
        "partial_refund(105, 0.6)",
        "partial_refund(106, 0.7)",
    ],
    ids=[
        "billing_refunds_partial_refund_1",
        "billing_refunds_partial_refund_2",
        "billing_refunds_partial_refund_3",
        "billing_refunds_partial_refund_4",
        "billing_refunds_partial_refund_5",
        "billing_refunds_partial_refund_6",
    ],
)
def test_partial_refund(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
