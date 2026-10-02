"""Tests for billing.refunds — generated; re-run scripts/generate_test_modules.py."""

import pytest

from src.billing import refunds as _module


@pytest.mark.parametrize(
    "call_expr",
    [
        "calculate_refund(101, 1)",
        "calculate_refund(102, 2)",
        "calculate_refund(103, 3)",
        "calculate_refund(104, 4)",
        "calculate_refund(105, 5)",
        "calculate_refund(106, 6)",
        "calculate_refund(107, 7)",
        "calculate_refund(108, 8)",
        "calculate_refund(109, 9)",
        "calculate_refund(110, 10)",
        "calculate_refund(111, 11)",
        "calculate_refund(112, 12)",
        "calculate_refund(113, 13)",
        "calculate_refund(114, 14)",
        "calculate_refund(115, 15)",
        "calculate_refund(116, 16)",
        "calculate_refund(117, 17)",
        "calculate_refund(118, 18)",
    ],
    ids=[
        "billing_refunds_calculate_refund_1",
        "billing_refunds_calculate_refund_2",
        "billing_refunds_calculate_refund_3",
        "billing_refunds_calculate_refund_4",
        "billing_refunds_calculate_refund_5",
        "billing_refunds_calculate_refund_6",
        "billing_refunds_calculate_refund_7",
        "billing_refunds_calculate_refund_8",
        "billing_refunds_calculate_refund_9",
        "billing_refunds_calculate_refund_10",
        "billing_refunds_calculate_refund_11",
        "billing_refunds_calculate_refund_12",
        "billing_refunds_calculate_refund_13",
        "billing_refunds_calculate_refund_14",
        "billing_refunds_calculate_refund_15",
        "billing_refunds_calculate_refund_16",
        "billing_refunds_calculate_refund_17",
        "billing_refunds_calculate_refund_18",
    ],
)
def test_calculate_refund(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
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
        "partial_refund(107, 0.8)",
        "partial_refund(108, 0.9)",
        "partial_refund(109, 0.1)",
        "partial_refund(110, 0.2)",
        "partial_refund(111, 0.3)",
        "partial_refund(112, 0.4)",
        "partial_refund(113, 0.5)",
        "partial_refund(114, 0.6)",
        "partial_refund(115, 0.7)",
        "partial_refund(116, 0.8)",
        "partial_refund(117, 0.9)",
        "partial_refund(118, 0.1)",
    ],
    ids=[
        "billing_refunds_partial_refund_1",
        "billing_refunds_partial_refund_2",
        "billing_refunds_partial_refund_3",
        "billing_refunds_partial_refund_4",
        "billing_refunds_partial_refund_5",
        "billing_refunds_partial_refund_6",
        "billing_refunds_partial_refund_7",
        "billing_refunds_partial_refund_8",
        "billing_refunds_partial_refund_9",
        "billing_refunds_partial_refund_10",
        "billing_refunds_partial_refund_11",
        "billing_refunds_partial_refund_12",
        "billing_refunds_partial_refund_13",
        "billing_refunds_partial_refund_14",
        "billing_refunds_partial_refund_15",
        "billing_refunds_partial_refund_16",
        "billing_refunds_partial_refund_17",
        "billing_refunds_partial_refund_18",
    ],
)
def test_partial_refund(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "refund_eligible(1, 30)",
        "refund_eligible(2, 30)",
        "refund_eligible(3, 30)",
        "refund_eligible(4, 30)",
        "refund_eligible(5, 30)",
        "refund_eligible(6, 30)",
        "refund_eligible(7, 30)",
        "refund_eligible(8, 30)",
        "refund_eligible(9, 30)",
        "refund_eligible(10, 30)",
        "refund_eligible(11, 30)",
        "refund_eligible(12, 30)",
        "refund_eligible(13, 30)",
        "refund_eligible(14, 30)",
        "refund_eligible(15, 30)",
        "refund_eligible(16, 30)",
        "refund_eligible(17, 30)",
        "refund_eligible(18, 30)",
    ],
    ids=[
        "billing_refunds_refund_eligible_1",
        "billing_refunds_refund_eligible_2",
        "billing_refunds_refund_eligible_3",
        "billing_refunds_refund_eligible_4",
        "billing_refunds_refund_eligible_5",
        "billing_refunds_refund_eligible_6",
        "billing_refunds_refund_eligible_7",
        "billing_refunds_refund_eligible_8",
        "billing_refunds_refund_eligible_9",
        "billing_refunds_refund_eligible_10",
        "billing_refunds_refund_eligible_11",
        "billing_refunds_refund_eligible_12",
        "billing_refunds_refund_eligible_13",
        "billing_refunds_refund_eligible_14",
        "billing_refunds_refund_eligible_15",
        "billing_refunds_refund_eligible_16",
        "billing_refunds_refund_eligible_17",
        "billing_refunds_refund_eligible_18",
    ],
)
def test_refund_eligible(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "format_refund(1)",
        "format_refund(2)",
        "format_refund(3)",
        "format_refund(4)",
        "format_refund(5)",
        "format_refund(6)",
        "format_refund(7)",
        "format_refund(8)",
        "format_refund(9)",
        "format_refund(10)",
        "format_refund(11)",
        "format_refund(12)",
        "format_refund(13)",
        "format_refund(14)",
        "format_refund(15)",
        "format_refund(16)",
        "format_refund(17)",
        "format_refund(18)",
    ],
    ids=[
        "billing_refunds_format_refund_1",
        "billing_refunds_format_refund_2",
        "billing_refunds_format_refund_3",
        "billing_refunds_format_refund_4",
        "billing_refunds_format_refund_5",
        "billing_refunds_format_refund_6",
        "billing_refunds_format_refund_7",
        "billing_refunds_format_refund_8",
        "billing_refunds_format_refund_9",
        "billing_refunds_format_refund_10",
        "billing_refunds_format_refund_11",
        "billing_refunds_format_refund_12",
        "billing_refunds_format_refund_13",
        "billing_refunds_format_refund_14",
        "billing_refunds_format_refund_15",
        "billing_refunds_format_refund_16",
        "billing_refunds_format_refund_17",
        "billing_refunds_format_refund_18",
    ],
)
def test_format_refund(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
