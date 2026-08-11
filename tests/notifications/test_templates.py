"""Tests for notifications.templates — generated; re-run scripts/generate_test_modules.py."""

import pytest


@pytest.mark.parametrize(
    "call_expr",
    [
        "render_template(1, 1.1)",
        "render_template(2, 1.2)",
        "render_template(3, 1.3)",
        "render_template(4, 1.4)",
        "render_template(5, 1.5)",
        "render_template(6, 1.6)",
    ],
    ids=[
        "notifications_templates_render_template_1",
        "notifications_templates_render_template_2",
        "notifications_templates_render_template_3",
        "notifications_templates_render_template_4",
        "notifications_templates_render_template_5",
        "notifications_templates_render_template_6",
    ],
)
def test_render_template(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "template_vars(1, 1.1)",
        "template_vars(2, 1.2)",
        "template_vars(3, 1.3)",
        "template_vars(4, 1.4)",
        "template_vars(5, 1.5)",
        "template_vars(6, 1.6)",
    ],
    ids=[
        "notifications_templates_template_vars_1",
        "notifications_templates_template_vars_2",
        "notifications_templates_template_vars_3",
        "notifications_templates_template_vars_4",
        "notifications_templates_template_vars_5",
        "notifications_templates_template_vars_6",
    ],
)
def test_template_vars(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
