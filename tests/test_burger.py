from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING
from tests.data import Data


def make_ingredient_mock(name: str, price: int, ingredient_type: str):
    ing = Mock()
    ing.get_name.return_value = name
    ing.get_price.return_value = price
    ing.get_type.return_value = ingredient_type
    return ing


class TestBurger:

    def test_set_buns_sets_bun(self):
        burger = Burger()
        bun = Bun(Data.BLACK_BUN, Data.BLACK_BUN_PRICE)

        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient_appends_to_list(self):
        burger = Burger()
        ingredient = make_ingredient_mock("cutlet", 100, INGREDIENT_TYPE_FILLING)

        burger.add_ingredient(ingredient)

        assert burger.ingredients == [ingredient]

    def test_remove_ingredient_deletes_by_index(self):
        burger = Burger()
        ingredient = make_ingredient_mock("cutlet", 100, INGREDIENT_TYPE_FILLING)
        burger.add_ingredient(ingredient)

        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_move_ingredient_moves_item(self):
        burger = Burger()
        first = make_ingredient_mock("cutlet", 100, INGREDIENT_TYPE_FILLING)
        second = make_ingredient_mock("sausage", 300, INGREDIENT_TYPE_FILLING)
        burger.add_ingredient(first)
        burger.add_ingredient(second)

        burger.move_ingredient(0, 1)

        assert len(burger.ingredients) == 2
        assert burger.ingredients == [second, first]

    def test_get_price_counts_bun_twice_plus_ingredients(self):
        burger = Burger()
        bun = Mock()
        bun.get_price.return_value = 100
        burger.set_buns(bun)

        burger.add_ingredient(make_ingredient_mock("a", 100, INGREDIENT_TYPE_FILLING))
        burger.add_ingredient(make_ingredient_mock("b", 200, INGREDIENT_TYPE_FILLING))
        burger.add_ingredient(make_ingredient_mock("c", 300, INGREDIENT_TYPE_FILLING))

        assert burger.get_price() == 800  # 100*2 + 100+200+300

    def test_get_receipt_formats_correctly(self):
        burger = Burger()
        bun = Mock()
        bun.get_name.return_value = "red bun"
        bun.get_price.return_value = 300
        burger.set_buns(bun)

        burger.add_ingredient(make_ingredient_mock("hot sauce", 100, "SAUCE"))
        burger.add_ingredient(make_ingredient_mock("sour cream", 200, "SAUCE"))
        burger.add_ingredient(make_ingredient_mock("chili sauce", 300, "SAUCE"))

        expected = "\n".join([
            "(==== red bun ====)",
            "= sauce hot sauce =",
            "= sauce sour cream =",
            "= sauce chili sauce =",
            "(==== red bun ====)\n",
            "Price: 1200",
        ])

        assert burger.get_receipt() == expected
