"""Shared formatters module — demo business logic."""


def format_currency(amount: float):
    return f"${amount:.2f}"


def format_date(year: int, month: int, day: int):
    return f"{year:04d}-{month:02d}-{day:02d}"


def format_phone(area: str, prefix: str, line: str):
    return f"({area}) {prefix}-{line}"


def truncate_text(text: str, max_len: int):
    return text[:max_len] + ("..." if len(text) > max_len else "")
