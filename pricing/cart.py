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
    sub = subtotal(lines)
    tax = round(sub * TAX_RATE)
    shipping = 0 if sub >= FREE_SHIPPING_OVER_CENTS else SHIPPING_CENTS
    gross = sub + tax + shipping
    # Promo: take the discount off the whole basket.
    return gross - gross * discount_pct // 100
