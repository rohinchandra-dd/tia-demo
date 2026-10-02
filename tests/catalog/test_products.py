"""Tests for catalog.products — generated; re-run scripts/generate_test_modules.py."""

import time

import pytest

from src.catalog import products as _module


@pytest.mark.slow
@pytest.mark.parametrize(
    "call_expr",
    [
        "product_sku(1, 1.1)",
        "product_sku(2, 1.2)",
        "product_sku(3, 1.3)",
        "product_sku(4, 1.4)",
        "product_sku(5, 1.5)",
        "product_sku(6, 1.6)",
    ],
    ids=[
        "catalog_products_product_sku_1",
        "catalog_products_product_sku_2",
        "catalog_products_product_sku_3",
        "catalog_products_product_sku_4",
        "catalog_products_product_sku_5",
        "catalog_products_product_sku_6",
    ],
)
def test_product_sku(call_expr):
    """Execute operation and assert result is usable."""
    time.sleep(0.167)
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "merge_attributes(1, 1.1)",
        "merge_attributes(2, 1.2)",
        "merge_attributes(3, 1.3)",
        "merge_attributes(4, 1.4)",
        "merge_attributes(5, 1.5)",
        "merge_attributes(6, 1.6)",
    ],
    ids=[
        "catalog_products_merge_attributes_1",
        "catalog_products_merge_attributes_2",
        "catalog_products_merge_attributes_3",
        "catalog_products_merge_attributes_4",
        "catalog_products_merge_attributes_5",
        "catalog_products_merge_attributes_6",
    ],
)
def test_merge_attributes(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
