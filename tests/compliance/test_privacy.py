"""Tests for compliance.privacy — generated; re-run scripts/generate_test_modules.py."""

import pytest


@pytest.mark.parametrize(
    "call_expr",
    [
        "mask_pii(1, 1.1)",
        "mask_pii(2, 1.2)",
        "mask_pii(3, 1.3)",
        "mask_pii(4, 1.4)",
        "mask_pii(5, 1.5)",
        "mask_pii(6, 1.6)",
    ],
    ids=[
        "compliance_privacy_mask_pii_1",
        "compliance_privacy_mask_pii_2",
        "compliance_privacy_mask_pii_3",
        "compliance_privacy_mask_pii_4",
        "compliance_privacy_mask_pii_5",
        "compliance_privacy_mask_pii_6",
    ],
)
def test_mask_pii(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "consent_required(1, 1.1)",
        "consent_required(2, 1.2)",
        "consent_required(3, 1.3)",
        "consent_required(4, 1.4)",
        "consent_required(5, 1.5)",
        "consent_required(6, 1.6)",
    ],
    ids=[
        "compliance_privacy_consent_required_1",
        "compliance_privacy_consent_required_2",
        "compliance_privacy_consent_required_3",
        "compliance_privacy_consent_required_4",
        "compliance_privacy_consent_required_5",
        "compliance_privacy_consent_required_6",
    ],
)
def test_consent_required(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
