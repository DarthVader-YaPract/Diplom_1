from unittest.mock import MagicMock

import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun():
    bun = MagicMock(spec=Bun)
    bun.get_name.return_value = "Краторная булка"
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def ingredients():
    sauce = MagicMock(spec=Ingredient)
    sauce.get_type.return_value = "SAUCE"
    sauce.get_name.return_value = (
        "Соус с шипами Антарианского плоскоходца"
    )
    sauce.get_price.return_value = 25

    filling = MagicMock(spec=Ingredient)
    filling.get_type.return_value = "FILLING"
    filling.get_name.return_value = (
        "Мясо бессмертных моллюсков Protostomia"
    )
    filling.get_price.return_value = 75
    return sauce, filling
