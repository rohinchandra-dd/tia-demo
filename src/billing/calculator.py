"""Billing calculator module — demo business logic."""


def add_tax(amount: float, rate: float):
    return round(amount * (1 + rate), 2)


def apply_discount(amount: float, discount: float):
    return max(0.0, amount - discount)


def round_currency(value: float, decimals: int = 2):
    return round(value, decimals)


def split_payment(total: float, parts: int):
    return round(total / parts, 2)
