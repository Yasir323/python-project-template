"""Example module — delete once real code exists.

Exists so the template's tests, typing, and coverage gate have a
target and every check passes on a fresh clone.
"""

import asyncio
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Money:
    """An amount in minor units (paise, cents) — never floats."""

    amount: int
    currency: str = "INR"

    def add(self, other: "Money") -> "Money":
        """Add two amounts of the same currency.

        Raises:
            ValueError: if currencies differ.
        """
        if self.currency != other.currency:
            raise ValueError(
                f"currency mismatch: {self.currency} != {other.currency}"
            )
        return Money(self.amount + other.amount, self.currency)


async def fetch_balance(account_id: str) -> Money:
    """Pretend-async lookup; proves pytest-asyncio is wired up."""
    await asyncio.sleep(0)
    return Money(amount=0, currency="INR") if account_id else Money(0)
