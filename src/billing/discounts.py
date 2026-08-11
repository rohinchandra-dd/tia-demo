"""Billing discounts module — demo business logic."""


def apply_coupon(amount: float, percent: float):
    return amount * (1 - min(1.0, percent))


def tier_discount(amount: float, tier: int):
    return amount * (1 - tier * 0.05)


def bulk_discount(amount: float, qty: int):
    return amount * (1 - min(0.25, qty * 0.01))


def validate_promo(code: str):
    return len(code) >= 4 and code.isalnum()
