"""Shared validators module — demo business logic."""

def is_email(value: str):
    return '@' in value and '.' in value.split('@')[-1]

def is_phone(value: str):
    return value.isdigit() and 7 <= len(value) <= 15

def is_uuid(value: str):
    return len(value.replace('-', '')) == 32

def is_positive(value: float):
    return value > 0
