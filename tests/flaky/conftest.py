"""Shared helpers for controlled flaky test demos."""

from __future__ import annotations

import random

import pytest

# Module-level attempt counters survive ddtrace in-process retries.
_attempts: dict[str, int] = {}


def fail_once(key: str, message: str) -> None:
    """Fail on the first attempt, pass on Auto Test Retry."""
    _attempts[key] = _attempts.get(key, 0) + 1
    if _attempts[key] == 1:
        pytest.fail(message)


def maybe_flake(probability: float, message: str) -> None:
    """Probabilistic failure for Flaky Tests dashboard demos."""
    if random.random() < probability:
        pytest.fail(message)


def efd_alternate(key: str, message: str) -> None:
    """Alternate pass/fail across attempts — surfaces with Early Flake Detection."""
    _attempts[key] = _attempts.get(key, 0) + 1
    if _attempts[key] % 2 == 1:
        pytest.fail(message)


@pytest.fixture
def attempt_counter():
    counts: dict[str, int] = {}

    def record(name: str) -> int:
        counts[name] = counts.get(name, 0) + 1
        return counts[name]

    return record
