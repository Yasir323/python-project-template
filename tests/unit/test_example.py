"""Tests for the example module — delete alongside it."""

import pytest

from package_name.example import Money, fetch_balance


class TestMoney:
    def test_add_same_currency(self) -> None:
        assert Money(100).add(Money(250)) == Money(350)

    def test_add_currency_mismatch_raises(self) -> None:
        with pytest.raises(ValueError, match="currency mismatch"):
            Money(100, "INR").add(Money(100, "USD"))

    def test_immutable(self) -> None:
        with pytest.raises(AttributeError):
            Money(1).amount = 2  # type: ignore[misc]


async def test_fetch_balance_returns_zero() -> None:
    balance = await fetch_balance("acc-123")
    assert balance == Money(0, "INR")


async def test_fetch_balance_empty_account_id() -> None:
    balance = await fetch_balance("")
    assert balance == Money(0, "INR")
