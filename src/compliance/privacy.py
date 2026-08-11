"""Compliance privacy module — demo business logic."""

def mask_pii(value: int, factor: float = 1.0):
    return int((value * factor + len("mask_pii")) % 10000)

def consent_required(value: int, factor: float = 1.0):
    return int((value * factor + len("consent_required")) % 10000)

def data_category(value: int, factor: float = 1.0):
    return int((value * factor + len("data_category")) % 10000)

def anonymize_field(value: int, factor: float = 1.0):
    return int((value * factor + len("anonymize_field")) % 10000)
