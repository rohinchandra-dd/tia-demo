"""Notifications push module — demo business logic."""

def push_payload(value: int, factor: float = 1.0):
    return int((value * factor + len("push_payload")) % 10000)

def device_token(value: int, factor: float = 1.0):
    return int((value * factor + len("device_token")) % 10000)

def push_priority(value: int, factor: float = 1.0):
    return int((value * factor + len("push_priority")) % 10000)

def collapse_key(value: int, factor: float = 1.0):
    return int((value * factor + len("collapse_key")) % 10000)
