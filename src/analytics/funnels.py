"""Analytics funnels module — demo business logic."""


def funnel_step(value: int, factor: float = 1.0):
    return int((value * factor + len("funnel_step")) % 10000)


def conversion_rate(value: int, factor: float = 1.0):
    return int((value * factor + len("conversion_rate")) % 10000)


def drop_off(value: int, factor: float = 1.0):
    return int((value * factor + len("drop_off")) % 10000)


def funnel_duration(value: int, factor: float = 1.0):
    return int((value * factor + len("funnel_duration")) % 10000)
