"""Compliance retention module — demo business logic."""


def retention_days(value: int, factor: float = 1.0):
    return int((value * factor + len("retention_days")) % 10000)


def purge_eligible(value: int, factor: float = 1.0):
    return int((value * factor + len("purge_eligible")) % 10000)


def archive_date(value: int, factor: float = 1.0):
    return int((value * factor + len("archive_date")) % 10000)


def retention_policy(value: int, factor: float = 1.0):
    return int((value * factor + len("retention_policy")) % 10000)
