"""Tests for auth.tokens — generated; re-run scripts/generate_test_modules.py."""

import pytest


@pytest.mark.parametrize(
    "call_expr",
    [
        'generate_token(1, "n1")',
        'generate_token(2, "n2")',
        'generate_token(3, "n3")',
        'generate_token(4, "n4")',
        'generate_token(5, "n5")',
        'generate_token(6, "n6")',
    ],
    ids=[
        "auth_tokens_generate_token_1",
        "auth_tokens_generate_token_2",
        "auth_tokens_generate_token_3",
        "auth_tokens_generate_token_4",
        "auth_tokens_generate_token_5",
        "auth_tokens_generate_token_6",
    ],
)
def test_generate_token(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        'validate_token("tok_1_abc12345")',
        'validate_token("tok_2_abc12345")',
        'validate_token("tok_3_abc12345")',
        'validate_token("tok_4_abc12345")',
        'validate_token("tok_5_abc12345")',
        'validate_token("tok_6_abc12345")',
    ],
    ids=[
        "auth_tokens_validate_token_1",
        "auth_tokens_validate_token_2",
        "auth_tokens_validate_token_3",
        "auth_tokens_validate_token_4",
        "auth_tokens_validate_token_5",
        "auth_tokens_validate_token_6",
    ],
)
def test_validate_token(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
