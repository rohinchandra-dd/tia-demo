"""Inventory reorder module — demo business logic."""


def reorder_point(avg_daily: float, lead_days: int, safety_stock: int):
    return avg_daily * lead_days + safety_stock


def suggest_quantity(target: int, on_hand: int):
    return max(0, target - on_hand)


def lead_time_days(base_days: int, supplier_delay: int):
    return max(1, base_days + supplier_delay)


def reorder_priority(urgency: int):
    return min(10, max(1, urgency // 10))
