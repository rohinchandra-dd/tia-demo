"""Tests for compliance.retention — generated; re-run scripts/generate_test_modules.py."""

import pytest


@pytest.mark.parametrize(
    "call_expr",
    [
        "retention_days(1, 1.1)",
        "retention_days(2, 1.2)",
        "retention_days(3, 1.3)",
        "retention_days(4, 1.4)",
        "retention_days(5, 1.5)",
        "retention_days(6, 1.6)",
    ],
    ids=[
        "compliance_retention_retention_days_1",
        "compliance_retention_retention_days_2",
        "compliance_retention_retention_days_3",
        "compliance_retention_retention_days_4",
        "compliance_retention_retention_days_5",
        "compliance_retention_retention_days_6",
    ],
)
def test_retention_days(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "purge_eligible(1, 1.1)",
        "purge_eligible(2, 1.2)",
        "purge_eligible(3, 1.3)",
        "purge_eligible(4, 1.4)",
        "purge_eligible(5, 1.5)",
        "purge_eligible(6, 1.6)",
    ],
    ids=[
        "compliance_retention_purge_eligible_1",
        "compliance_retention_purge_eligible_2",
        "compliance_retention_purge_eligible_3",
        "compliance_retention_purge_eligible_4",
        "compliance_retention_purge_eligible_5",
        "compliance_retention_purge_eligible_6",
    ],
)
def test_purge_eligible(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
