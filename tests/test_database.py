from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from tests.data import Data


class TestDatabase:
    def test_available_buns_returns_expected_buns(self, database):
        buns = database.available_buns()

        assert [(b.get_name(), b.get_price()) for b in buns] == [
            (Data.BLACK_BUN, Data.BLACK_BUN_PRICE),
            (Data.WHITE_BUN, Data.WHITE_BUN_PRICE),
            (Data.RED_BUN, Data.RED_BUN_PRICE),
        ]

    def test_available_ingredients_returns_expected_ingredients(self, database):
        ingredients = database.available_ingredients()

        assert [(i.get_type(), i.get_name(), i.get_price()) for i in ingredients] == [
            (INGREDIENT_TYPE_SAUCE, Data.HOT_SAUCE, Data.HOT_SAUCE_PRICE),
            (INGREDIENT_TYPE_SAUCE, Data.SOUR_CREAM, Data.SOUR_CREAM_PRICE),
            (INGREDIENT_TYPE_SAUCE, Data.CHILLI_SAUCE, Data.CHILLI_SAUCE_PRICE),
            (INGREDIENT_TYPE_FILLING, Data.CUTLET, Data.CUTLET_PRICE),
            (INGREDIENT_TYPE_FILLING, Data.DINOSAUR, Data.DINOSAUR_PRICE),
            (INGREDIENT_TYPE_FILLING, Data.SAUSAGE, Data.SAUSAGE_PRICE),
        ]
