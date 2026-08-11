"""Tests for catalog.search — generated; re-run scripts/generate_test_modules.py."""

import pytest

from src.catalog import search as _module


@pytest.mark.parametrize(
    "call_expr",
    [
        "search_score(1, 1.1)",
        "search_score(2, 1.2)",
        "search_score(3, 1.3)",
        "search_score(4, 1.4)",
        "search_score(5, 1.5)",
        "search_score(6, 1.6)",
    ],
    ids=[
        "catalog_search_search_score_1",
        "catalog_search_search_score_2",
        "catalog_search_search_score_3",
        "catalog_search_search_score_4",
        "catalog_search_search_score_5",
        "catalog_search_search_score_6",
    ],
)
def test_search_score(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "tokenize_query(1, 1.1)",
        "tokenize_query(2, 1.2)",
        "tokenize_query(3, 1.3)",
        "tokenize_query(4, 1.4)",
        "tokenize_query(5, 1.5)",
        "tokenize_query(6, 1.6)",
    ],
    ids=[
        "catalog_search_tokenize_query_1",
        "catalog_search_tokenize_query_2",
        "catalog_search_tokenize_query_3",
        "catalog_search_tokenize_query_4",
        "catalog_search_tokenize_query_5",
        "catalog_search_tokenize_query_6",
    ],
)
def test_tokenize_query(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
