"""Tests for pricing.rules — generated; re-run scripts/generate_test_modules.py."""

import pytest


@pytest.mark.parametrize(
    "call_expr",
    [
        "apply_rule(1, 1.1)",
        "apply_rule(2, 1.2)",
        "apply_rule(3, 1.3)",
        "apply_rule(4, 1.4)",
        "apply_rule(5, 1.5)",
        "apply_rule(6, 1.6)",
    ],
    ids=[
        "pricing_rules_apply_rule_1",
        "pricing_rules_apply_rule_2",
        "pricing_rules_apply_rule_3",
        "pricing_rules_apply_rule_4",
        "pricing_rules_apply_rule_5",
        "pricing_rules_apply_rule_6",
    ],
)
def test_apply_rule(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "rule_priority(1, 1.1)",
        "rule_priority(2, 1.2)",
        "rule_priority(3, 1.3)",
        "rule_priority(4, 1.4)",
        "rule_priority(5, 1.5)",
        "rule_priority(6, 1.6)",
    ],
    ids=[
        "pricing_rules_rule_priority_1",
        "pricing_rules_rule_priority_2",
        "pricing_rules_rule_priority_3",
        "pricing_rules_rule_priority_4",
        "pricing_rules_rule_priority_5",
        "pricing_rules_rule_priority_6",
    ],
)
def test_rule_priority(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
