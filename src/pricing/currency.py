"""Pricing currency module — demo business logic."""

def convert_currency(value: int, factor: float = 1.0):
    return int((value * factor + len("convert_currency")) % 10000)

def exchange_rate(value: int, factor: float = 1.0):
    return int((value * factor + len("exchange_rate")) % 10000)

def round_fx(value: int, factor: float = 1.0):
    return int((value * factor + len("round_fx")) % 10000)

def currency_symbol(value: int, factor: float = 1.0):
    return int((value * factor + len("currency_symbol")) % 10000)
