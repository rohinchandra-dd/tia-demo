"""Shared helpers for controlled flaky test demos."""

from __future__ import annotations

import os
import random

import pytest


def _attempt(key: str) -> int:
    """Count attempts in-process so EFD and Auto Test Retries share state."""
    env_key = f"_FLAKY_DEMO_{key}"
    count = int(os.environ.get(env_key, "0")) + 1
    os.environ[env_key] = str(count)
    return count


def fail_once(key: str, message: str) -> None:
    """Fail on the first attempt, pass on Auto Test Retry."""
    if _attempt(key) == 1:
        pytest.fail(message)


def maybe_flake(probability: float, message: str) -> None:
    """Probabilistic failure on the first attempt; passes on Auto Test Retry."""
    if _attempt(message) == 1 and random.random() < probability:
        pytest.fail(message)


def efd_alternate(key: str, message: str) -> None:
    """Fail once on new tests — Early Flake Detection retries until pass."""
    fail_once(key, message)


@pytest.fixture
def attempt_counter():
    counts: dict[str, int] = {}

    def record(name: str) -> int:
        counts[name] = counts.get(name, 0) + 1
        return counts[name]

    return record
