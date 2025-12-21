import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from tests.data import Data


INGREDIENT_CASES = [
    (INGREDIENT_TYPE_SAUCE, Data.HOT_SAUCE, Data.HOT_SAUCE_PRICE),
    (INGREDIENT_TYPE_SAUCE, Data.SOUR_CREAM, Data.SOUR_CREAM_PRICE),
    (INGREDIENT_TYPE_SAUCE, Data.CHILLI_SAUCE, Data.CHILLI_SAUCE_PRICE),
    (INGREDIENT_TYPE_FILLING, Data.CUTLET, Data.CUTLET_PRICE),
    (INGREDIENT_TYPE_FILLING, Data.DINOSAUR, Data.DINOSAUR_PRICE),
    (INGREDIENT_TYPE_FILLING, Data.SAUSAGE, Data.SAUSAGE_PRICE),
]


class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_CASES)
    def test_init_sets_fields(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price

    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_CASES)
    def test_get_type_returns_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_CASES)
    def test_get_name_returns_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_CASES)
    def test_get_price_returns_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price
