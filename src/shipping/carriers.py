"""Shipping carriers module — demo business logic."""

def select_carrier(carriers: list):
    return carriers[0] if carriers else "default"

def carrier_score(on_time: float, cost_score: float):
    return on_time * 0.6 + cost_score * 0.4

def cutoff_time(hour: int, cutoff_hour: int):
    return hour < cutoff_hour

def service_level(priority: int):
    return "express" if priority > 5 else "standard"
