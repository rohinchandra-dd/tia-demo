"""Auto Test Retry recoverable flaky tests — fail once, pass on retry."""

from __future__ import annotations

import pytest

_attempts: dict[str, int] = {}


@pytest.mark.flaky_demo
def test_payment_gateway_timeout():
    _attempts["payment"] = _attempts.get("payment", 0) + 1
    if _attempts["payment"] == 1:
        pytest.fail("Simulated transient payment gateway timeout")
    assert True


@pytest.mark.flaky_demo
def test_external_tax_api_timeout():
    _attempts["tax_api"] = _attempts.get("tax_api", 0) + 1
    if _attempts["tax_api"] == 1:
        pytest.fail("Simulated external tax API timeout")
    assert True


@pytest.mark.flaky_demo
def test_shipping_rate_lookup_retry():
    _attempts["shipping_rate"] = _attempts.get("shipping_rate", 0) + 1
    if _attempts["shipping_rate"] == 1:
        pytest.fail("Simulated carrier rate lookup failure")
    assert True
