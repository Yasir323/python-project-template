"""Integration tests live here (testcontainers, real Postgres/Redis).

Run with `make itest`. Excluded from the default unit run.
"""

import pytest


@pytest.mark.integration
def test_placeholder() -> None:
    """Replace with real infrastructure tests."""
    assert True
