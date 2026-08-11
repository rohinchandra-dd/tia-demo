"""Catalog categories module — demo business logic."""


def category_path(value: int, factor: float = 1.0):
    return int((value * factor + len("category_path")) % 10000)


def parent_category(value: int, factor: float = 1.0):
    return int((value * factor + len("parent_category")) % 10000)


def leaf_categories(value: int, factor: float = 1.0):
    return int((value * factor + len("leaf_categories")) % 10000)


def category_depth(value: int, factor: float = 1.0):
    return int((value * factor + len("category_depth")) % 10000)
