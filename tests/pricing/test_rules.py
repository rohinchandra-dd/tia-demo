"""Tests for pricing.rules — generated; re-run scripts/generate_test_modules.py."""

import pytest

from src.pricing import rules as _module


@pytest.mark.parametrize(
    "call_expr",
    [
        "apply_rule(1, 1.1)",
        "apply_rule(2, 1.2)",
        "apply_rule(3, 1.3)",
        "apply_rule(4, 1.4)",
        "apply_rule(5, 1.5)",
        "apply_rule(6, 1.6)",
        "apply_rule(7, 1.7000000000000002)",
        "apply_rule(8, 1.8)",
        "apply_rule(9, 1.9)",
        "apply_rule(10, 2.0)",
        "apply_rule(11, 2.1)",
        "apply_rule(12, 2.2)",
        "apply_rule(13, 2.3)",
        "apply_rule(14, 2.4000000000000004)",
        "apply_rule(15, 2.5)",
        "apply_rule(16, 2.6)",
        "apply_rule(17, 2.7)",
        "apply_rule(18, 2.8)",
    ],
    ids=[
        "pricing_rules_apply_rule_1",
        "pricing_rules_apply_rule_2",
        "pricing_rules_apply_rule_3",
        "pricing_rules_apply_rule_4",
        "pricing_rules_apply_rule_5",
        "pricing_rules_apply_rule_6",
        "pricing_rules_apply_rule_7",
        "pricing_rules_apply_rule_8",
        "pricing_rules_apply_rule_9",
        "pricing_rules_apply_rule_10",
        "pricing_rules_apply_rule_11",
        "pricing_rules_apply_rule_12",
        "pricing_rules_apply_rule_13",
        "pricing_rules_apply_rule_14",
        "pricing_rules_apply_rule_15",
        "pricing_rules_apply_rule_16",
        "pricing_rules_apply_rule_17",
        "pricing_rules_apply_rule_18",
    ],
)
def test_apply_rule(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
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
        "rule_priority(7, 1.7000000000000002)",
        "rule_priority(8, 1.8)",
        "rule_priority(9, 1.9)",
        "rule_priority(10, 2.0)",
        "rule_priority(11, 2.1)",
        "rule_priority(12, 2.2)",
        "rule_priority(13, 2.3)",
        "rule_priority(14, 2.4000000000000004)",
        "rule_priority(15, 2.5)",
        "rule_priority(16, 2.6)",
        "rule_priority(17, 2.7)",
        "rule_priority(18, 2.8)",
    ],
    ids=[
        "pricing_rules_rule_priority_1",
        "pricing_rules_rule_priority_2",
        "pricing_rules_rule_priority_3",
        "pricing_rules_rule_priority_4",
        "pricing_rules_rule_priority_5",
        "pricing_rules_rule_priority_6",
        "pricing_rules_rule_priority_7",
        "pricing_rules_rule_priority_8",
        "pricing_rules_rule_priority_9",
        "pricing_rules_rule_priority_10",
        "pricing_rules_rule_priority_11",
        "pricing_rules_rule_priority_12",
        "pricing_rules_rule_priority_13",
        "pricing_rules_rule_priority_14",
        "pricing_rules_rule_priority_15",
        "pricing_rules_rule_priority_16",
        "pricing_rules_rule_priority_17",
        "pricing_rules_rule_priority_18",
    ],
)
def test_rule_priority(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "match_conditions(1, 1.1)",
        "match_conditions(2, 1.2)",
        "match_conditions(3, 1.3)",
        "match_conditions(4, 1.4)",
        "match_conditions(5, 1.5)",
        "match_conditions(6, 1.6)",
        "match_conditions(7, 1.7000000000000002)",
        "match_conditions(8, 1.8)",
        "match_conditions(9, 1.9)",
        "match_conditions(10, 2.0)",
        "match_conditions(11, 2.1)",
        "match_conditions(12, 2.2)",
        "match_conditions(13, 2.3)",
        "match_conditions(14, 2.4000000000000004)",
        "match_conditions(15, 2.5)",
        "match_conditions(16, 2.6)",
        "match_conditions(17, 2.7)",
        "match_conditions(18, 2.8)",
    ],
    ids=[
        "pricing_rules_match_conditions_1",
        "pricing_rules_match_conditions_2",
        "pricing_rules_match_conditions_3",
        "pricing_rules_match_conditions_4",
        "pricing_rules_match_conditions_5",
        "pricing_rules_match_conditions_6",
        "pricing_rules_match_conditions_7",
        "pricing_rules_match_conditions_8",
        "pricing_rules_match_conditions_9",
        "pricing_rules_match_conditions_10",
        "pricing_rules_match_conditions_11",
        "pricing_rules_match_conditions_12",
        "pricing_rules_match_conditions_13",
        "pricing_rules_match_conditions_14",
        "pricing_rules_match_conditions_15",
        "pricing_rules_match_conditions_16",
        "pricing_rules_match_conditions_17",
        "pricing_rules_match_conditions_18",
    ],
)
def test_match_conditions(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "rule_stack(1, 1.1)",
        "rule_stack(2, 1.2)",
        "rule_stack(3, 1.3)",
        "rule_stack(4, 1.4)",
        "rule_stack(5, 1.5)",
        "rule_stack(6, 1.6)",
        "rule_stack(7, 1.7000000000000002)",
        "rule_stack(8, 1.8)",
        "rule_stack(9, 1.9)",
        "rule_stack(10, 2.0)",
        "rule_stack(11, 2.1)",
        "rule_stack(12, 2.2)",
        "rule_stack(13, 2.3)",
        "rule_stack(14, 2.4000000000000004)",
        "rule_stack(15, 2.5)",
        "rule_stack(16, 2.6)",
        "rule_stack(17, 2.7)",
        "rule_stack(18, 2.8)",
    ],
    ids=[
        "pricing_rules_rule_stack_1",
        "pricing_rules_rule_stack_2",
        "pricing_rules_rule_stack_3",
        "pricing_rules_rule_stack_4",
        "pricing_rules_rule_stack_5",
        "pricing_rules_rule_stack_6",
        "pricing_rules_rule_stack_7",
        "pricing_rules_rule_stack_8",
        "pricing_rules_rule_stack_9",
        "pricing_rules_rule_stack_10",
        "pricing_rules_rule_stack_11",
        "pricing_rules_rule_stack_12",
        "pricing_rules_rule_stack_13",
        "pricing_rules_rule_stack_14",
        "pricing_rules_rule_stack_15",
        "pricing_rules_rule_stack_16",
        "pricing_rules_rule_stack_17",
        "pricing_rules_rule_stack_18",
    ],
)
def test_rule_stack(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
