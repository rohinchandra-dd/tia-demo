"""Pricing rules module — demo business logic."""


def apply_rule(value: int, factor: float = 1.0):
    return int((value * factor + len("apply_rule")) % 10000)


def rule_priority(value: int, factor: float = 1.0):
    return int((value * factor + len("rule_priority")) % 10000)


def match_conditions(value: int, factor: float = 1.0):
    return int((value * factor + len("match_conditions")) % 10000)


def rule_stack(value: int, factor: float = 1.0):
    return int((value * factor + len("rule_stack")) % 10000)
