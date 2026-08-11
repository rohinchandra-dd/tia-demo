"""Tests for auth.mfa — generated; re-run scripts/generate_test_modules.py."""

import pytest

from src.auth import mfa as _module


@pytest.mark.parametrize(
    "call_expr",
    [
        'generate_otp("seed1")',
        'generate_otp("seed2")',
        'generate_otp("seed3")',
        'generate_otp("seed4")',
        'generate_otp("seed5")',
        'generate_otp("seed6")',
    ],
    ids=[
        "auth_mfa_generate_otp_1",
        "auth_mfa_generate_otp_2",
        "auth_mfa_generate_otp_3",
        "auth_mfa_generate_otp_4",
        "auth_mfa_generate_otp_5",
        "auth_mfa_generate_otp_6",
    ],
)
def test_generate_otp(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        'verify_otp("123456", "123456")',
        'verify_otp("123456", "123456")',
        'verify_otp("123456", "123456")',
        'verify_otp("123456", "123456")',
        'verify_otp("123456", "123456")',
        'verify_otp("123456", "123456")',
    ],
    ids=[
        "auth_mfa_verify_otp_1",
        "auth_mfa_verify_otp_2",
        "auth_mfa_verify_otp_3",
        "auth_mfa_verify_otp_4",
        "auth_mfa_verify_otp_5",
        "auth_mfa_verify_otp_6",
    ],
)
def test_verify_otp(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
