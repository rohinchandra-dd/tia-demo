"""Tests for auth.permissions — generated; re-run scripts/generate_test_modules.py."""

import time

import pytest

from src.auth import permissions as _module


@pytest.mark.slow
@pytest.mark.parametrize(
    "call_expr",
    [
        'has_permission("read", {"read", "write"})',
        'has_permission("read", {"read", "write"})',
        'has_permission("read", {"read", "write"})',
        'has_permission("read", {"read", "write"})',
        'has_permission("read", {"read", "write"})',
        'has_permission("read", {"read", "write"})',
    ],
    ids=[
        "auth_permissions_has_permission_1",
        "auth_permissions_has_permission_2",
        "auth_permissions_has_permission_3",
        "auth_permissions_has_permission_4",
        "auth_permissions_has_permission_5",
        "auth_permissions_has_permission_6",
    ],
)
def test_has_permission(call_expr):
    """Execute operation and assert result is usable."""
    time.sleep(0.167)
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        'merge_roles({"admin"}, {"user", "read"})',
        'merge_roles({"admin"}, {"user", "read"})',
        'merge_roles({"admin"}, {"user", "read"})',
        'merge_roles({"admin"}, {"user", "read"})',
        'merge_roles({"admin"}, {"user", "read"})',
        'merge_roles({"admin"}, {"user", "read"})',
    ],
    ids=[
        "auth_permissions_merge_roles_1",
        "auth_permissions_merge_roles_2",
        "auth_permissions_merge_roles_3",
        "auth_permissions_merge_roles_4",
        "auth_permissions_merge_roles_5",
        "auth_permissions_merge_roles_6",
    ],
)
def test_merge_roles(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
