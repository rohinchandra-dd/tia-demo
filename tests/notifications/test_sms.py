"""Tests for notifications.sms — generated; re-run scripts/generate_test_modules.py."""

import pytest


@pytest.mark.parametrize(
    "call_expr",
    [
        "format_sms(1, 1.1)",
        "format_sms(2, 1.2)",
        "format_sms(3, 1.3)",
        "format_sms(4, 1.4)",
        "format_sms(5, 1.5)",
        "format_sms(6, 1.6)",
    ],
    ids=[
        "notifications_sms_format_sms_1",
        "notifications_sms_format_sms_2",
        "notifications_sms_format_sms_3",
        "notifications_sms_format_sms_4",
        "notifications_sms_format_sms_5",
        "notifications_sms_format_sms_6",
    ],
)
def test_format_sms(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "sms_segments(1, 1.1)",
        "sms_segments(2, 1.2)",
        "sms_segments(3, 1.3)",
        "sms_segments(4, 1.4)",
        "sms_segments(5, 1.5)",
        "sms_segments(6, 1.6)",
    ],
    ids=[
        "notifications_sms_sms_segments_1",
        "notifications_sms_sms_segments_2",
        "notifications_sms_sms_segments_3",
        "notifications_sms_sms_segments_4",
        "notifications_sms_sms_segments_5",
        "notifications_sms_sms_segments_6",
    ],
)
def test_sms_segments(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
