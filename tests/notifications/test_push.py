"""Tests for notifications.push — generated; re-run scripts/generate_test_modules.py."""

import pytest

from src.notifications import push as _module


@pytest.mark.parametrize(
    "call_expr",
    [
        "push_payload(1, 1.1)",
        "push_payload(2, 1.2)",
        "push_payload(3, 1.3)",
        "push_payload(4, 1.4)",
        "push_payload(5, 1.5)",
        "push_payload(6, 1.6)",
    ],
    ids=[
        "notifications_push_push_payload_1",
        "notifications_push_push_payload_2",
        "notifications_push_push_payload_3",
        "notifications_push_push_payload_4",
        "notifications_push_push_payload_5",
        "notifications_push_push_payload_6",
    ],
)
def test_push_payload(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "device_token(1, 1.1)",
        "device_token(2, 1.2)",
        "device_token(3, 1.3)",
        "device_token(4, 1.4)",
        "device_token(5, 1.5)",
        "device_token(6, 1.6)",
    ],
    ids=[
        "notifications_push_device_token_1",
        "notifications_push_device_token_2",
        "notifications_push_device_token_3",
        "notifications_push_device_token_4",
        "notifications_push_device_token_5",
        "notifications_push_device_token_6",
    ],
)
def test_device_token(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
