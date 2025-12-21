from tests.data import Data
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_SAUCE as SAUCE,
    INGREDIENT_TYPE_FILLING as FILLING,
)

class TestDatabase:
    def test_available_buns_returns_expected_buns(self, database):
        buns = database.available_buns()
        got = [(b.get_name(), b.get_price()) for b in buns]
        assert got == [
            (Data.BLACK_BUN, Data.BLACK_BUN_PRICE),
            (Data.WHITE_BUN, Data.WHITE_BUN_PRICE),
            (Data.RED_BUN,   Data.RED_BUN_PRICE),
        ]

    def test_available_ingredients_returns_expected_ingredients(self, database):
        ings = database.available_ingredients()
        got = [(i.get_type(), i.get_name(), i.get_price()) for i in ings]
        
        assert got == [
            (SAUCE,   Data.HOT_SAUCE,    Data.HOT_SAUCE_PRICE),
            (SAUCE,   Data.SOUR_CREAM,   Data.SOUR_CREAM_PRICE),
            (SAUCE,   Data.CHILLI_SAUCE, Data.CHILLI_SAUCE_PRICE),
            (FILLING, Data.CUTLET,       Data.CUTLET_PRICE),
            (FILLING, Data.DINOSAUR,     Data.DINOSAUR_PRICE),
            (FILLING, Data.SAUSAGE,      Data.SAUSAGE_PRICE),
        ]
