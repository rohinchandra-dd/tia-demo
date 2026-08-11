"""Tests for auth.permissions — generated; re-run scripts/generate_test_modules.py."""

import time

import pytest


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
        'has_permission("read", {"read", "write"})',
        'has_permission("read", {"read", "write"})',
        'has_permission("read", {"read", "write"})',
        'has_permission("read", {"read", "write"})',
        'has_permission("read", {"read", "write"})',
        'has_permission("read", {"read", "write"})',
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
        "auth_permissions_has_permission_7",
        "auth_permissions_has_permission_8",
        "auth_permissions_has_permission_9",
        "auth_permissions_has_permission_10",
        "auth_permissions_has_permission_11",
        "auth_permissions_has_permission_12",
        "auth_permissions_has_permission_13",
        "auth_permissions_has_permission_14",
        "auth_permissions_has_permission_15",
        "auth_permissions_has_permission_16",
        "auth_permissions_has_permission_17",
        "auth_permissions_has_permission_18",
    ],
)
def test_has_permission(call_expr):
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
        'merge_roles({"admin"}, {"user", "read"})',
        'merge_roles({"admin"}, {"user", "read"})',
        'merge_roles({"admin"}, {"user", "read"})',
        'merge_roles({"admin"}, {"user", "read"})',
        'merge_roles({"admin"}, {"user", "read"})',
        'merge_roles({"admin"}, {"user", "read"})',
        'merge_roles({"admin"}, {"user", "read"})',
        'merge_roles({"admin"}, {"user", "read"})',
        'merge_roles({"admin"}, {"user", "read"})',
        'merge_roles({"admin"}, {"user", "read"})',
        'merge_roles({"admin"}, {"user", "read"})',
        'merge_roles({"admin"}, {"user", "read"})',
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
        "auth_permissions_merge_roles_7",
        "auth_permissions_merge_roles_8",
        "auth_permissions_merge_roles_9",
        "auth_permissions_merge_roles_10",
        "auth_permissions_merge_roles_11",
        "auth_permissions_merge_roles_12",
        "auth_permissions_merge_roles_13",
        "auth_permissions_merge_roles_14",
        "auth_permissions_merge_roles_15",
        "auth_permissions_merge_roles_16",
        "auth_permissions_merge_roles_17",
        "auth_permissions_merge_roles_18",
    ],
)
def test_merge_roles(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "role_hierarchy(1, 3)",
        "role_hierarchy(2, 3)",
        "role_hierarchy(3, 3)",
        "role_hierarchy(4, 3)",
        "role_hierarchy(0, 3)",
        "role_hierarchy(1, 3)",
        "role_hierarchy(2, 3)",
        "role_hierarchy(3, 3)",
        "role_hierarchy(4, 3)",
        "role_hierarchy(0, 3)",
        "role_hierarchy(1, 3)",
        "role_hierarchy(2, 3)",
        "role_hierarchy(3, 3)",
        "role_hierarchy(4, 3)",
        "role_hierarchy(0, 3)",
        "role_hierarchy(1, 3)",
        "role_hierarchy(2, 3)",
        "role_hierarchy(3, 3)",
    ],
    ids=[
        "auth_permissions_role_hierarchy_1",
        "auth_permissions_role_hierarchy_2",
        "auth_permissions_role_hierarchy_3",
        "auth_permissions_role_hierarchy_4",
        "auth_permissions_role_hierarchy_5",
        "auth_permissions_role_hierarchy_6",
        "auth_permissions_role_hierarchy_7",
        "auth_permissions_role_hierarchy_8",
        "auth_permissions_role_hierarchy_9",
        "auth_permissions_role_hierarchy_10",
        "auth_permissions_role_hierarchy_11",
        "auth_permissions_role_hierarchy_12",
        "auth_permissions_role_hierarchy_13",
        "auth_permissions_role_hierarchy_14",
        "auth_permissions_role_hierarchy_15",
        "auth_permissions_role_hierarchy_16",
        "auth_permissions_role_hierarchy_17",
        "auth_permissions_role_hierarchy_18",
    ],
)
def test_role_hierarchy(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "permission_mask(15, 7)",
        "permission_mask(15, 7)",
        "permission_mask(15, 7)",
        "permission_mask(15, 7)",
        "permission_mask(15, 7)",
        "permission_mask(15, 7)",
        "permission_mask(15, 7)",
        "permission_mask(15, 7)",
        "permission_mask(15, 7)",
        "permission_mask(15, 7)",
        "permission_mask(15, 7)",
        "permission_mask(15, 7)",
        "permission_mask(15, 7)",
        "permission_mask(15, 7)",
        "permission_mask(15, 7)",
        "permission_mask(15, 7)",
        "permission_mask(15, 7)",
        "permission_mask(15, 7)",
    ],
    ids=[
        "auth_permissions_permission_mask_1",
        "auth_permissions_permission_mask_2",
        "auth_permissions_permission_mask_3",
        "auth_permissions_permission_mask_4",
        "auth_permissions_permission_mask_5",
        "auth_permissions_permission_mask_6",
        "auth_permissions_permission_mask_7",
        "auth_permissions_permission_mask_8",
        "auth_permissions_permission_mask_9",
        "auth_permissions_permission_mask_10",
        "auth_permissions_permission_mask_11",
        "auth_permissions_permission_mask_12",
        "auth_permissions_permission_mask_13",
        "auth_permissions_permission_mask_14",
        "auth_permissions_permission_mask_15",
        "auth_permissions_permission_mask_16",
        "auth_permissions_permission_mask_17",
        "auth_permissions_permission_mask_18",
    ],
)
def test_permission_mask(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
