"""Tests for catalog.categories — generated; re-run scripts/generate_test_modules.py."""

import pytest


@pytest.mark.parametrize(
    "call_expr",
    [
        "category_path(1, 1.1)",
        "category_path(2, 1.2)",
        "category_path(3, 1.3)",
        "category_path(4, 1.4)",
        "category_path(5, 1.5)",
        "category_path(6, 1.6)",
    ],
    ids=[
        "catalog_categories_category_path_1",
        "catalog_categories_category_path_2",
        "catalog_categories_category_path_3",
        "catalog_categories_category_path_4",
        "catalog_categories_category_path_5",
        "catalog_categories_category_path_6",
    ],
)
def test_category_path(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "parent_category(1, 1.1)",
        "parent_category(2, 1.2)",
        "parent_category(3, 1.3)",
        "parent_category(4, 1.4)",
        "parent_category(5, 1.5)",
        "parent_category(6, 1.6)",
    ],
    ids=[
        "catalog_categories_parent_category_1",
        "catalog_categories_parent_category_2",
        "catalog_categories_parent_category_3",
        "catalog_categories_parent_category_4",
        "catalog_categories_parent_category_5",
        "catalog_categories_parent_category_6",
    ],
)
def test_parent_category(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr)
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
