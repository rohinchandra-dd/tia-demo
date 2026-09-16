"""PR Signals in Slack demo test scenario."""

from __future__ import annotations

import os
import pytest


def test_pr_signals_passing_baseline():
    """Baseline test that always passes."""
    assert True


def test_pr_signals_fast_failure():
    """Deterministic failure on initial run (attempt 1), passes on retry."""
    attempt = os.environ.get("GITHUB_RUN_ATTEMPT", "1")
    if attempt == "1":
        pytest.fail(
            "Deterministic test failure for PR Signals demo (re-run to recover)"
        )
    assert True
