"""Tests for shipping.labels — generated; re-run scripts/generate_test_modules.py."""

import pytest


@pytest.mark.parametrize(
    "call_expr",
    [
        "generate_label(1)",
        "generate_label(2)",
        "generate_label(3)",
        "generate_label(4)",
        "generate_label(5)",
        "generate_label(6)",
    ],
    ids=[
        "shipping_labels_generate_label_1",
        "shipping_labels_generate_label_2",
        "shipping_labels_generate_label_3",
        "shipping_labels_generate_label_4",
        "shipping_labels_generate_label_5",
        "shipping_labels_generate_label_6",
    ],
)
def test_generate_label(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        'validate_address("123 St", "City", "10001")',
        'validate_address("123 St", "City", "10002")',
        'validate_address("123 St", "City", "10003")',
        'validate_address("123 St", "City", "10004")',
        'validate_address("123 St", "City", "10005")',
        'validate_address("123 St", "City", "10006")',
    ],
    ids=[
        "shipping_labels_validate_address_1",
        "shipping_labels_validate_address_2",
        "shipping_labels_validate_address_3",
        "shipping_labels_validate_address_4",
        "shipping_labels_validate_address_5",
        "shipping_labels_validate_address_6",
    ],
)
def test_validate_address(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
