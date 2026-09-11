import pytest

from data import (
    BUN_ONLY_PRICE,
    BURGER_WITH_FILLING_PRICE,
    BURGER_WITH_SAUCE_PRICE,
    FULL_BURGER_PRICE,
    RECEIPT_WITH_FILLING_AND_SAUCE,
    RECEIPT_WITH_SAUCE_AND_FILLING,
)


class TestBurger:
    def test_set_buns_sets_bun_for_price(self, burger, bun):
        burger.set_buns(bun)
        assert burger.get_price() == BUN_ONLY_PRICE

    def test_add_ingredient_adds_ingredient_to_price(
        self, burger, bun, ingredients
    ):
        burger.set_buns(bun)
        burger.add_ingredient(ingredients[0])
        assert burger.get_price() == BURGER_WITH_SAUCE_PRICE

    @pytest.mark.parametrize(
        "index, expected_price",
        [
            (0, BURGER_WITH_FILLING_PRICE),
            (1, BURGER_WITH_SAUCE_PRICE),
        ],
        ids=["remove_sauce", "remove_filling"],
    )
    def test_remove_ingredient_removes_ingredient_from_price(
        self, burger, bun, ingredients, index, expected_price
    ):
        burger.set_buns(bun)
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)
        burger.remove_ingredient(index)
        assert burger.get_price() == expected_price

    @pytest.mark.parametrize(
        "index, new_index, expected_receipt",
        [
            (0, 1, RECEIPT_WITH_FILLING_AND_SAUCE),
            (1, 0, RECEIPT_WITH_FILLING_AND_SAUCE),
        ],
        ids=["move_sauce_forward", "move_filling_back"],
    )
    def test_move_ingredient_changes_ingredient_order(
        self, burger, bun, ingredients, index, new_index, expected_receipt
    ):
        burger.set_buns(bun)
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)
        burger.move_ingredient(index, new_index)
        assert burger.get_receipt() == expected_receipt

    @pytest.mark.parametrize(
        "count, expected_price",
        [(0, BUN_ONLY_PRICE), (2, FULL_BURGER_PRICE)],
        ids=["bun_only", "burger_with_ingredients"],
    )
    def test_get_price_calculates_bun_and_ingredients(
        self, burger, bun, ingredients, count, expected_price
    ):
        burger.set_buns(bun)
        for ingredient in ingredients[:count]:
            burger.add_ingredient(ingredient)
        assert burger.get_price() == expected_price

    def test_get_receipt_returns_burger_description(
        self, burger, bun, ingredients
    ):
        burger.set_buns(bun)
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)
        assert burger.get_receipt() == RECEIPT_WITH_SAUCE_AND_FILLING
