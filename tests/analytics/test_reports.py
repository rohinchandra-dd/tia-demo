"""Tests for analytics.reports — generated; re-run scripts/generate_test_modules.py."""

import pytest

from src.analytics import reports as _module


@pytest.mark.parametrize(
    "call_expr",
    [
        "report_period(1, 1.1)",
        "report_period(2, 1.2)",
        "report_period(3, 1.3)",
        "report_period(4, 1.4)",
        "report_period(5, 1.5)",
        "report_period(6, 1.6)",
    ],
    ids=[
        "analytics_reports_report_period_1",
        "analytics_reports_report_period_2",
        "analytics_reports_report_period_3",
        "analytics_reports_report_period_4",
        "analytics_reports_report_period_5",
        "analytics_reports_report_period_6",
    ],
)
def test_report_period(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "report_title(1, 1.1)",
        "report_title(2, 1.2)",
        "report_title(3, 1.3)",
        "report_title(4, 1.4)",
        "report_title(5, 1.5)",
        "report_title(6, 1.6)",
    ],
    ids=[
        "analytics_reports_report_title_1",
        "analytics_reports_report_title_2",
        "analytics_reports_report_title_3",
        "analytics_reports_report_title_4",
        "analytics_reports_report_title_5",
        "analytics_reports_report_title_6",
    ],
)
def test_report_title(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
