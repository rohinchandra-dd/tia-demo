"""Shared pytest fixtures and configuration."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

FIXTURES_DIR = Path(__file__).resolve().parent.parent / "fixtures"


@pytest.fixture(scope="session")
def fixtures_dir() -> Path:
    return FIXTURES_DIR


@pytest.fixture(scope="session")
def sample_orders(fixtures_dir: Path) -> list[dict]:
    with (fixtures_dir / "orders.json").open(encoding="utf-8") as handle:
        return json.load(handle)


@pytest.fixture(scope="session")
def pricing_rules(fixtures_dir: Path) -> list[dict]:
    with (fixtures_dir / "pricing_rules.csv").open(encoding="utf-8") as handle:
        lines = handle.read().strip().splitlines()
    headers = lines[0].split(",")
    return [dict(zip(headers, row.split(","))) for row in lines[1:]]
