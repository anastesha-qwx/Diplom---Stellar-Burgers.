import pytest

from praktikum.bun import Bun
from tests.data import Data


BUN_CASES = [
    (Data.BLACK_BUN, Data.BLACK_BUN_PRICE),
    (Data.RED_BUN, Data.RED_BUN_PRICE),
    (Data.WHITE_BUN, Data.WHITE_BUN_PRICE),
]


class TestBun:
    @pytest.mark.parametrize("name, price", BUN_CASES)
    def test_get_name_returns_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", BUN_CASES)
    def test_get_price_returns_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
