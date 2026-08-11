"""Shared utils module — demo business logic."""

def clamp(value: float, minimum: float, maximum: float):
    return max(minimum, min(maximum, value))

def normalize_email(email: str):
    return email.strip().lower()

def slugify(text: str):
    return text.lower().replace(" ", "-")

def safe_divide(numerator: float, denominator: float, default: float = 0.0):
    return numerator / denominator if denominator else default
