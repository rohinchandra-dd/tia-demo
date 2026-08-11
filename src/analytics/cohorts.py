"""Analytics cohorts module — demo business logic."""


def cohort_size(value: int, factor: float = 1.0):
    return int((value * factor + len("cohort_size")) % 10000)


def retention_rate(value: int, factor: float = 1.0):
    return int((value * factor + len("retention_rate")) % 10000)


def cohort_period(value: int, factor: float = 1.0):
    return int((value * factor + len("cohort_period")) % 10000)


def cohort_label(value: int, factor: float = 1.0):
    return int((value * factor + len("cohort_label")) % 10000)
