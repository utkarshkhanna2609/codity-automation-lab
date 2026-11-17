import pytest

from pricing.cart import Line, total


def test_small_order_pays_shipping():
    assert total([Line("mug", 1_200, 1)]) == 1_200 + 96 + 499


def test_large_order_ships_free():
    assert total([Line("chair", 6_000, 1)]) == 6_000 + 480


def test_discount_applies_before_tax():
    assert total([Line("chair", 6_000, 1)], discount_pct=10) == 5_400 + 432


def test_discount_out_of_range_is_refused():
    with pytest.raises(ValueError):
        total([Line("mug", 1_200, 1)], discount_pct=150)
