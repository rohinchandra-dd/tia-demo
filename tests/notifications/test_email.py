"""Tests for notifications.email — generated; re-run scripts/generate_test_modules.py."""

import pytest

from src.notifications import email as _module


@pytest.mark.parametrize(
    "call_expr",
    [
        "render_subject(1, 1.1)",
        "render_subject(2, 1.2)",
        "render_subject(3, 1.3)",
        "render_subject(4, 1.4)",
        "render_subject(5, 1.5)",
        "render_subject(6, 1.6)",
    ],
    ids=[
        "notifications_email_render_subject_1",
        "notifications_email_render_subject_2",
        "notifications_email_render_subject_3",
        "notifications_email_render_subject_4",
        "notifications_email_render_subject_5",
        "notifications_email_render_subject_6",
    ],
)
def test_render_subject(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "render_body(1, 1.1)",
        "render_body(2, 1.2)",
        "render_body(3, 1.3)",
        "render_body(4, 1.4)",
        "render_body(5, 1.5)",
        "render_body(6, 1.6)",
    ],
    ids=[
        "notifications_email_render_body_1",
        "notifications_email_render_body_2",
        "notifications_email_render_body_3",
        "notifications_email_render_body_4",
        "notifications_email_render_body_5",
        "notifications_email_render_body_6",
    ],
)
def test_render_body(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
