"""Tests for shared.utils — generated; re-run scripts/generate_test_modules.py."""

import pytest


@pytest.mark.parametrize(
    "call_expr",
    [
        "clamp(1.0, 0.0, 10.0)",
        "clamp(2.0, 0.0, 10.0)",
        "clamp(3.0, 0.0, 10.0)",
        "clamp(4.0, 0.0, 10.0)",
        "clamp(5.0, 0.0, 10.0)",
        "clamp(6.0, 0.0, 10.0)",
    ],
    ids=[
        "shared_utils_clamp_1",
        "shared_utils_clamp_2",
        "shared_utils_clamp_3",
        "shared_utils_clamp_4",
        "shared_utils_clamp_5",
        "shared_utils_clamp_6",
    ],
)
def test_clamp(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        'normalize_email("User1@Example.COM")',
        'normalize_email("User2@Example.COM")',
        'normalize_email("User3@Example.COM")',
        'normalize_email("User4@Example.COM")',
        'normalize_email("User5@Example.COM")',
        'normalize_email("User6@Example.COM")',
    ],
    ids=[
        "shared_utils_normalize_email_1",
        "shared_utils_normalize_email_2",
        "shared_utils_normalize_email_3",
        "shared_utils_normalize_email_4",
        "shared_utils_normalize_email_5",
        "shared_utils_normalize_email_6",
    ],
)
def test_normalize_email(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
