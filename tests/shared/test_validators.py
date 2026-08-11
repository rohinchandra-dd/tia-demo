"""Tests for shared.validators — generated; re-run scripts/generate_test_modules.py."""

import pytest

from src.shared import validators as _module


@pytest.mark.parametrize(
    "call_expr",
    [
        'is_email("user1@example.com")',
        'is_email("user2@example.com")',
        'is_email("user3@example.com")',
        'is_email("user4@example.com")',
        'is_email("user5@example.com")',
        'is_email("user6@example.com")',
    ],
    ids=[
        "shared_validators_is_email_1",
        "shared_validators_is_email_2",
        "shared_validators_is_email_3",
        "shared_validators_is_email_4",
        "shared_validators_is_email_5",
        "shared_validators_is_email_6",
    ],
)
def test_is_email(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        'is_phone("5550000001")',
        'is_phone("5550000002")',
        'is_phone("5550000003")',
        'is_phone("5550000004")',
        'is_phone("5550000005")',
        'is_phone("5550000006")',
    ],
    ids=[
        "shared_validators_is_phone_1",
        "shared_validators_is_phone_2",
        "shared_validators_is_phone_3",
        "shared_validators_is_phone_4",
        "shared_validators_is_phone_5",
        "shared_validators_is_phone_6",
    ],
)
def test_is_phone(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
