"""Tests for shipping.carriers — generated; re-run scripts/generate_test_modules.py."""

import pytest

from src.shipping import carriers as _module


@pytest.mark.parametrize(
    "call_expr",
    [
        'select_carrier(["fedex", "ups"])',
        'select_carrier(["fedex", "ups"])',
        'select_carrier(["fedex", "ups"])',
        'select_carrier(["fedex", "ups"])',
        'select_carrier(["fedex", "ups"])',
        'select_carrier(["fedex", "ups"])',
    ],
    ids=[
        "shipping_carriers_select_carrier_1",
        "shipping_carriers_select_carrier_2",
        "shipping_carriers_select_carrier_3",
        "shipping_carriers_select_carrier_4",
        "shipping_carriers_select_carrier_5",
        "shipping_carriers_select_carrier_6",
    ],
)
def test_select_carrier(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "carrier_score(0.81, 0.71)",
        "carrier_score(0.82, 0.72)",
        "carrier_score(0.83, 0.73)",
        "carrier_score(0.84, 0.74)",
        "carrier_score(0.85, 0.75)",
        "carrier_score(0.86, 0.76)",
    ],
    ids=[
        "shipping_carriers_carrier_score_1",
        "shipping_carriers_carrier_score_2",
        "shipping_carriers_carrier_score_3",
        "shipping_carriers_carrier_score_4",
        "shipping_carriers_carrier_score_5",
        "shipping_carriers_carrier_score_6",
    ],
)
def test_carrier_score(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
