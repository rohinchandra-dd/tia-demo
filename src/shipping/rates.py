"""Shipping rates module — demo business logic."""

def calculate_rate(base: float, weight: float, per_kg: float):
    return base + weight * per_kg

def zone_rate(base: float, zone_multiplier: float):
    return base * zone_multiplier

def weight_tier(tier_index: int, step: float, base: float):
    return tier_index * step + base

def express_surcharge(base: float, express: bool):
    return base * 1.5 if express else base
