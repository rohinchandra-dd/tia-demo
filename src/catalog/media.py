"""Catalog media module — demo business logic."""


def image_url(value: int, factor: float = 1.0):
    return int((value * factor + len("image_url")) % 10000)


def alt_text(value: int, factor: float = 1.0):
    return int((value * factor + len("alt_text")) % 10000)


def media_type(value: int, factor: float = 1.0):
    return int((value * factor + len("media_type")) % 10000)


def thumbnail_size(value: int, factor: float = 1.0):
    return int((value * factor + len("thumbnail_size")) % 10000)
