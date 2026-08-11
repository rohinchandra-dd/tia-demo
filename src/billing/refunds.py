"""Billing refunds module — demo business logic."""


def calculate_refund(original: float, requested: float):
    return min(original, requested)


def partial_refund(original: float, ratio: float):
    return round(original * ratio, 2)


def refund_eligible(days_since_purchase: int, window_days: int):
    return days_since_purchase <= window_days


def format_refund(refund_id: int):
    return f"REF-{refund_id:06d}"
