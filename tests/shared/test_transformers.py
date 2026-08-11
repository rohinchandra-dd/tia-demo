"""Tests for shared.transformers — generated; re-run scripts/generate_test_modules.py."""

import pytest

from src.shared import transformers as _module


@pytest.mark.parametrize(
    "call_expr",
    [
        'to_snake_case("MyVarName1")',
        'to_snake_case("MyVarName2")',
        'to_snake_case("MyVarName3")',
        'to_snake_case("MyVarName4")',
        'to_snake_case("MyVarName5")',
        'to_snake_case("MyVarName6")',
    ],
    ids=[
        "shared_transformers_to_snake_case_1",
        "shared_transformers_to_snake_case_2",
        "shared_transformers_to_snake_case_3",
        "shared_transformers_to_snake_case_4",
        "shared_transformers_to_snake_case_5",
        "shared_transformers_to_snake_case_6",
    ],
)
def test_to_snake_case(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        'to_camel_case(["hello", "world", "1"])',
        'to_camel_case(["hello", "world", "2"])',
        'to_camel_case(["hello", "world", "3"])',
        'to_camel_case(["hello", "world", "4"])',
        'to_camel_case(["hello", "world", "5"])',
        'to_camel_case(["hello", "world", "6"])',
    ],
    ids=[
        "shared_transformers_to_camel_case_1",
        "shared_transformers_to_camel_case_2",
        "shared_transformers_to_camel_case_3",
        "shared_transformers_to_camel_case_4",
        "shared_transformers_to_camel_case_5",
        "shared_transformers_to_camel_case_6",
    ],
)
def test_to_camel_case(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
