from tests.data import Data
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_SAUCE as SAUCE,
    INGREDIENT_TYPE_FILLING as FILLING,
)

class TestIngredient:
    def test_ingredient_getters_sauce_hot(self):
        ing = Ingredient(SAUCE, Data.HOT_SAUCE, Data.HOT_SAUCE_PRICE)
        assert ing.get_type() == SAUCE
        assert ing.get_name() == Data.HOT_SAUCE
        assert ing.get_price() == Data.HOT_SAUCE_PRICE

    def test_ingredient_getters_sauce_sour(self):
        ing = Ingredient(SAUCE, Data.SOUR_CREAM, Data.SOUR_CREAM_PRICE)
        assert ing.get_type() == SAUCE
        assert ing.get_name() == Data.SOUR_CREAM
        assert ing.get_price() == Data.SOUR_CREAM_PRICE

    def test_ingredient_getters_sauce_chilli(self):
        ing = Ingredient(SAUCE, Data.CHILLI_SAUCE, Data.CHILLI_SAUCE_PRICE)
        assert ing.get_type() == SAUCE
        assert ing.get_name() == Data.CHILLI_SAUCE
        assert ing.get_price() == Data.CHILLI_SAUCE_PRICE

    def test_ingredient_getters_filling_cutlet(self):
        ing = Ingredient(FILLING, Data.CUTLET, Data.CUTLET_PRICE)
        assert ing.get_type() == FILLING
        assert ing.get_name() == Data.CUTLET
        assert ing.get_price() == Data.CUTLET_PRICE

    def test_ingredient_getters_filling_dinosaur(self):
        ing = Ingredient(FILLING, Data.DINOSAUR, Data.DINOSAUR_PRICE)
        assert ing.get_type() == FILLING
        assert ing.get_name() == Data.DINOSAUR
        assert ing.get_price() == Data.DINOSAUR_PRICE

    def test_ingredient_getters_filling_sausage(self):
        ing = Ingredient(FILLING, Data.SAUSAGE, Data.SAUSAGE_PRICE)
        assert ing.get_type() == FILLING
        assert ing.get_name() == Data.SAUSAGE
        assert ing.get_price() == Data.SAUSAGE_PRICE
