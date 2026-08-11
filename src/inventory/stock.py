"""Inventory stock module — demo business logic."""


def check_stock(available: int, requested: int):
    return available >= requested


def reserve_stock(available: int, requested: int):
    return max(0, available - requested)


def release_stock(available: int, released: int):
    return available + released


def stock_level(qty: int, threshold: int):
    return "low" if qty < threshold else "ok"
