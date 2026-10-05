"""Timing checks for the checkout flow."""

from __future__ import annotations

import pytest

_efd_attempts = 0


# Rename before pushing. Early Flake Detection only retries a test whose name is
# absent from the known-tests baseline for this service, and the baseline records
# a name the first time it runs -- including dry runs. See DEMO.md C4.
@pytest.mark.flaky_demo
def test_checkout_flow_timing_RENAME_ME():
    global _efd_attempts
    _efd_attempts += 1
    if _efd_attempts % 2 == 1:
        pytest.fail("Simulated new checkout flow race (EFD demo)")
    assert True
