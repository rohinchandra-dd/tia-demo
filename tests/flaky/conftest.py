"""Fixtures for flaky test demos."""

from __future__ import annotations

import pytest

# Module-level attempt tracking survives ddtrace in-process retries.


@pytest.fixture
def attempt_counter():
    counts: dict[str, int] = {}

    def record(name: str) -> int:
        counts[name] = counts.get(name, 0) + 1
        return counts[name]

    return record
