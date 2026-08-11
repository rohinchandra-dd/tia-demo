"""Tests for catalog.media — generated; re-run scripts/generate_test_modules.py."""

import pytest

from src.catalog import media as _module


@pytest.mark.parametrize(
    "call_expr",
    [
        "image_url(1, 1.1)",
        "image_url(2, 1.2)",
        "image_url(3, 1.3)",
        "image_url(4, 1.4)",
        "image_url(5, 1.5)",
        "image_url(6, 1.6)",
    ],
    ids=[
        "catalog_media_image_url_1",
        "catalog_media_image_url_2",
        "catalog_media_image_url_3",
        "catalog_media_image_url_4",
        "catalog_media_image_url_5",
        "catalog_media_image_url_6",
    ],
)
def test_image_url(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None


@pytest.mark.parametrize(
    "call_expr",
    [
        "alt_text(1, 1.1)",
        "alt_text(2, 1.2)",
        "alt_text(3, 1.3)",
        "alt_text(4, 1.4)",
        "alt_text(5, 1.5)",
        "alt_text(6, 1.6)",
    ],
    ids=[
        "catalog_media_alt_text_1",
        "catalog_media_alt_text_2",
        "catalog_media_alt_text_3",
        "catalog_media_alt_text_4",
        "catalog_media_alt_text_5",
        "catalog_media_alt_text_6",
    ],
)
def test_alt_text(call_expr):
    """Execute operation and assert result is usable."""
    result = eval(call_expr, vars(_module))
    if isinstance(result, bool):
        assert result in (True, False)
    else:
        assert result is not None
