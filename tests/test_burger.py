import pytest


def test_selected_bun_is_used_in_price(burger, bun):
    burger.set_buns(bun)
    assert burger.get_price() == 200


def test_added_ingredient_is_used_in_price(burger, bun, ingredients):
    burger.set_buns(bun)
    burger.add_ingredient(ingredients[0])
    assert burger.get_price() == 225


@pytest.mark.parametrize(
    "index, remaining",
    [(0, 1), (1, 0)],
    ids=["first", "second"],
)
def test_ingredient_is_removed_by_index(burger, ingredients, index, remaining):
    for ingredient in ingredients:
        burger.add_ingredient(ingredient)
    burger.remove_ingredient(index)
    assert burger.ingredients == [ingredients[remaining]]


@pytest.mark.parametrize(
    "index, new_index, order",
    [(0, 1, (1, 0)), (1, 0, (1, 0))],
    ids=["move_forward", "move_back"],
)
def test_ingredient_is_moved_to_new_index(
    burger, ingredients, index, new_index, order
):
    for ingredient in ingredients:
        burger.add_ingredient(ingredient)
    burger.move_ingredient(index, new_index)
    assert burger.ingredients == [ingredients[item] for item in order]


@pytest.mark.parametrize(
    "count, price",
    [(0, 200), (2, 300)],
    ids=["bun_only", "full_burger"],
)
def test_price_contains_bun_twice_and_ingredients(
    burger, bun, ingredients, count, price
):
    burger.set_buns(bun)
    for ingredient in ingredients[:count]:
        burger.add_ingredient(ingredient)
    assert burger.get_price() == price


def test_receipt_contains_bun_ingredients_and_price(burger, bun, ingredients):
    burger.set_buns(bun)
    for ingredient in ingredients:
        burger.add_ingredient(ingredient)
    receipt = (
        "(==== Краторная булка ====)\n"
        "= sauce Соус с шипами Антарианского "
        "плоскоходца =\n"
        "= filling Мясо бессмертных моллюсков Protostomia =\n"
        "(==== Краторная булка ====)\n\n"
        "Price: 300"
    )
    assert burger.get_receipt() == receipt
