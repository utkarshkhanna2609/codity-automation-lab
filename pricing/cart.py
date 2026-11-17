"""Cart totals for the checkout service."""
from __future__ import annotations

from dataclasses import dataclass

TAX_RATE = 0.08
FREE_SHIPPING_OVER_CENTS = 5_000
SHIPPING_CENTS = 499


@dataclass(frozen=True)
class Line:
    sku: str
    unit_cents: int
    qty: int


def subtotal(lines: list[Line]) -> int:
    return sum(l.unit_cents * l.qty for l in lines)


def total(lines: list[Line], discount_pct: int = 0) -> int:
    """Subtotal, less the discount, plus tax and shipping, in cents."""
    if not 0 <= discount_pct <= 100:
        raise ValueError("discount_pct must be between 0 and 100")
    sub = subtotal(lines)
    discounted = sub - sub * discount_pct // 100
    tax = round(discounted * TAX_RATE)
    shipping = 0 if discounted >= FREE_SHIPPING_OVER_CENTS else SHIPPING_CENTS
    return discounted + tax + shipping
