"""Inventory cycle_count module — demo business logic."""


def count_variance(expected: int, actual: int):
    return abs(expected - actual)


def adjust_count(actual: int, adjustment: int):
    return actual + adjustment


def schedule_count(day_of_week: int):
    return day_of_week in {1, 3, 5}


def count_accuracy(variance: float, expected: int):
    return 1.0 - (variance / max(1, expected))
