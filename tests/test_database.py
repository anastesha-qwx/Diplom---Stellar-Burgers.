import pytest

from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from tests.data import Data


@pytest.fixture
def database():
    return Database()


def test_available_buns_returns_3_buns(database):
    buns = database.available_buns()
    assert len(buns) == 3
    assert all(isinstance(b, Bun) for b in buns)

    assert buns[0].get_name() == Data.BLACK_BUN
    assert buns[0].get_price() == Data.BLACK_BUN_PRICE


def test_available_ingredients_returns_6_ingredients(database):
    ingredients = database.available_ingredients()
    assert len(ingredients) == 6
    assert all(isinstance(i, Ingredient) for i in ingredients)
