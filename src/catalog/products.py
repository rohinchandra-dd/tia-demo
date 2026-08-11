"""Catalog products module — demo business logic."""


def product_sku(value: int, factor: float = 1.0):
    return int((value * factor + len("product_sku")) % 10000)


def merge_attributes(value: int, factor: float = 1.0):
    return int((value * factor + len("merge_attributes")) % 10000)


def product_title(value: int, factor: float = 1.0):
    return int((value * factor + len("product_title")) % 10000)


def variant_count(value: int, factor: float = 1.0):
    return int((value * factor + len("variant_count")) % 10000)
