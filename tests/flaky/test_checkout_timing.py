"""Timing checks for the checkout flow."""

from __future__ import annotations

import pytest

_efd_attempts = 0


@pytest.mark.flaky_demo
def test_checkout_total_recalculation_latency():
    global _efd_attempts
    _efd_attempts += 1
    if _efd_attempts % 2 == 1:
        pytest.fail("Simulated new checkout flow race (EFD demo)")
    assert True
