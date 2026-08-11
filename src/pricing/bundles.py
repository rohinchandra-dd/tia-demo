"""Pricing bundles module — demo business logic."""


def bundle_price(value: int, factor: float = 1.0):
    return int((value * factor + len("bundle_price")) % 10000)


def bundle_discount(value: int, factor: float = 1.0):
    return int((value * factor + len("bundle_discount")) % 10000)


def bundle_items(value: int, factor: float = 1.0):
    return int((value * factor + len("bundle_items")) % 10000)


def bundle_valid(value: int, factor: float = 1.0):
    return int((value * factor + len("bundle_valid")) % 10000)
