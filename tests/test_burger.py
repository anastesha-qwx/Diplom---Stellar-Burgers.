from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from praktikum.database import Database
from tests.data import Data


class TestBurger:
    def test_set_buns_sets_bun(self):
        burger = Burger()
        bun = Bun(Data.BLACK_BUN, Data.BLACK_BUN_PRICE)

        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient_adds_to_list(self):
        burger = Burger()

        ingredient = Mock()
        ingredient.get_price.return_value = Data.CUTLET_PRICE
        ingredient.get_name.return_value = Data.CUTLET
        ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING

        burger.add_ingredient(ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient_removes_by_index(self):
        burger = Burger()
        ingredient = Mock()

        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_move_ingredient_moves_item(self):
        burger = Burger()

        first = Mock()
        first.get_price.return_value = Data.CUTLET_PRICE
        first.get_name.return_value = Data.CUTLET
        first.get_type.return_value = INGREDIENT_TYPE_FILLING

        second = Mock()
        second.get_price.return_value = Data.SAUSAGE_PRICE
        second.get_name.return_value = Data.SAUSAGE
        second.get_type.return_value = INGREDIENT_TYPE_FILLING

        burger.add_ingredient(first)
        burger.add_ingredient(second)

        burger.move_ingredient(0, 1)

        assert burger.ingredients[0] == second
        assert burger.ingredients[1] == first

    def test_get_price_returns_sum_of_bun_and_ingredients(self):
        burger = Burger()
        db = Database()

        burger.set_buns(db.available_buns()[0])  # black bun (100)
        burger.add_ingredient(db.available_ingredients()[0])  # hot sauce (100)
        burger.add_ingredient(db.available_ingredients()[1])  # sour cream (200)
        burger.add_ingredient(db.available_ingredients()[2])  # chili sauce (300)

        assert burger.get_price() == 800

    def test_get_receipt_returns_expected_text(self):
        burger = Burger()
        db = Database()

        burger.set_buns(db.available_buns()[2])  # red bun (300)
        burger.add_ingredient(db.available_ingredients()[0])  # hot sauce (100)
        burger.add_ingredient(db.available_ingredients()[1])  # sour cream (200)
        burger.add_ingredient(db.available_ingredients()[2])  # chili sauce (300)

        expected = (
            f"(==== {Data.RED_BUN} ====)\n"
            f"= {INGREDIENT_TYPE_SAUCE.lower()} {Data.HOT_SAUCE} =\n"
            f"= {INGREDIENT_TYPE_SAUCE.lower()} {Data.SOUR_CREAM} =\n"
            f"= {INGREDIENT_TYPE_SAUCE.lower()} {Data.CHILLI_SAUCE} =\n"
            f"(==== {Data.RED_BUN} ====)\n\n"
            f"Price: 1200"
        )

        assert burger.get_receipt() == expected

