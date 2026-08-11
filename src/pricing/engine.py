"""Pricing engine module — demo business logic."""


def base_price(value: int, factor: float = 1.0):
    return int((value * factor + len("base_price")) % 10000)


def margin_price(value: int, factor: float = 1.0):
    return int((value * factor + len("margin_price")) % 10000)


def competitor_adjust(value: int, factor: float = 1.0):
    return int((value * factor + len("competitor_adjust")) % 10000)


def price_floor(value: int, factor: float = 1.0):
    return int((value * factor + len("price_floor")) % 10000)
