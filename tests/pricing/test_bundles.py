"""Tests for pricing.bundles — generated; re-run scripts/generate_test_modules.py."""

import pytest

from src.pricing import bundles as _module


@pytest.mark.parametrize(
    "call_expr",
    [
        "bundle_price(1, 1.1)",
        "bundle_price(2, 1.2)",
        "bundle_price(3, 1.3)",
        "bundle_price(4, 1.4)",
        "bundle_price(5, 1.5)",
        "bundle_price(6, 1.6)",
    ],
    ids=[
        "pricing_bundles_bundle_price_1",
        "pricing_bundles_bundle_price_2",
        "pricing_bundles_bundle_price_3",
        "pricing_bundles_bundle_price_4",
        "pricing_bundles_bundle_price_5",
        "pricing_bundles_bundle_price_6",
    ],
)
def test_bundle_price(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "bundle_discount(1, 1.1)",
        "bundle_discount(2, 1.2)",
        "bundle_discount(3, 1.3)",
        "bundle_discount(4, 1.4)",
        "bundle_discount(5, 1.5)",
        "bundle_discount(6, 1.6)",
    ],
    ids=[
        "pricing_bundles_bundle_discount_1",
        "pricing_bundles_bundle_discount_2",
        "pricing_bundles_bundle_discount_3",
        "pricing_bundles_bundle_discount_4",
        "pricing_bundles_bundle_discount_5",
        "pricing_bundles_bundle_discount_6",
    ],
)
def test_bundle_discount(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
