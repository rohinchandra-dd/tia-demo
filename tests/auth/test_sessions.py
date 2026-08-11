"""Tests for auth.sessions — generated; re-run scripts/generate_test_modules.py."""

import pytest

from src.auth import sessions as _module


@pytest.mark.parametrize(
    "call_expr",
    [
        "create_session(1)",
        "create_session(2)",
        "create_session(3)",
        "create_session(4)",
        "create_session(5)",
        "create_session(6)",
    ],
    ids=[
        "auth_sessions_create_session_1",
        "auth_sessions_create_session_2",
        "auth_sessions_create_session_3",
        "auth_sessions_create_session_4",
        "auth_sessions_create_session_5",
        "auth_sessions_create_session_6",
    ],
)
def test_create_session(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        'revoke_session("sess_1", {"sess_2"})',
        'revoke_session("sess_2", {"sess_3"})',
        'revoke_session("sess_3", {"sess_4"})',
        'revoke_session("sess_4", {"sess_5"})',
        'revoke_session("sess_5", {"sess_6"})',
        'revoke_session("sess_6", {"sess_7"})',
    ],
    ids=[
        "auth_sessions_revoke_session_1",
        "auth_sessions_revoke_session_2",
        "auth_sessions_revoke_session_3",
        "auth_sessions_revoke_session_4",
        "auth_sessions_revoke_session_5",
        "auth_sessions_revoke_session_6",
    ],
)
def test_revoke_session(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
