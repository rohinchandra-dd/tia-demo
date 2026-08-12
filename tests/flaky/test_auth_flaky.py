"""Auth-domain flaky tests — TIA runs these when src/auth/ changes."""

from __future__ import annotations

import pytest

from src.auth.permissions import has_permission, merge_roles
from src.auth.tokens import generate_token, validate_token
from tests.flaky.conftest import fail_once, maybe_flake

pytestmark = pytest.mark.flaky_demo


def test_auth_token_refresh_timeout():
    fail_once("auth_token", "Simulated token refresh timeout")
    assert validate_token("tok_42_abc12345") is True


def test_auth_permission_cache_retry():
    fail_once("auth_permission", "Simulated permission cache miss")
    assert has_permission("read", {"read", "write"}) is True


def test_auth_role_merge_race():
    maybe_flake(0.35, "Simulated role merge race")
    merged = merge_roles({"admin"}, {"user", "read"})
    assert "admin" in merged and "read" in merged


def test_auth_token_generation_jitter():
    maybe_flake(0.35, "Simulated token generation jitter")
    assert generate_token(99, "seed").startswith("tok_")
