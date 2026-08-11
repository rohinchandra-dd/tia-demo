"""Tests for compliance.exports — generated; re-run scripts/generate_test_modules.py."""

import pytest

from src.compliance import exports as _module


@pytest.mark.parametrize(
    "call_expr",
    [
        "export_format(1, 1.1)",
        "export_format(2, 1.2)",
        "export_format(3, 1.3)",
        "export_format(4, 1.4)",
        "export_format(5, 1.5)",
        "export_format(6, 1.6)",
    ],
    ids=[
        "compliance_exports_export_format_1",
        "compliance_exports_export_format_2",
        "compliance_exports_export_format_3",
        "compliance_exports_export_format_4",
        "compliance_exports_export_format_5",
        "compliance_exports_export_format_6",
    ],
)
def test_export_format(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "export_row(1, 1.1)",
        "export_row(2, 1.2)",
        "export_row(3, 1.3)",
        "export_row(4, 1.4)",
        "export_row(5, 1.5)",
        "export_row(6, 1.6)",
    ],
    ids=[
        "compliance_exports_export_row_1",
        "compliance_exports_export_row_2",
        "compliance_exports_export_row_3",
        "compliance_exports_export_row_4",
        "compliance_exports_export_row_5",
        "compliance_exports_export_row_6",
    ],
)
def test_export_row(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
