"""Catalog search module — demo business logic."""


def search_score(value: int, factor: float = 1.0):
    return int((value * factor + len("search_score")) % 10000)


def tokenize_query(value: int, factor: float = 1.0):
    return int((value * factor + len("tokenize_query")) % 10000)


def normalize_query(value: int, factor: float = 1.0):
    return int((value * factor + len("normalize_query")) % 10000)


def rank_results(value: int, factor: float = 1.0):
    return int((value * factor + len("rank_results")) % 10000)
