from unittest.mock import MagicMock

import pytest

from data import (
    BUN_NAME,
    BUN_PRICE,
    FILLING_NAME,
    FILLING_PRICE,
    FILLING_TYPE,
    SAUCE_NAME,
    SAUCE_PRICE,
    SAUCE_TYPE,
)
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun():
    bun = MagicMock(spec=Bun)
    bun.get_name.return_value = BUN_NAME
    bun.get_price.return_value = BUN_PRICE
    return bun


@pytest.fixture
def ingredients():
    sauce = MagicMock(spec=Ingredient)
    sauce.get_type.return_value = SAUCE_TYPE
    sauce.get_name.return_value = SAUCE_NAME
    sauce.get_price.return_value = SAUCE_PRICE

    filling = MagicMock(spec=Ingredient)
    filling.get_type.return_value = FILLING_TYPE
    filling.get_name.return_value = FILLING_NAME
    filling.get_price.return_value = FILLING_PRICE
    return sauce, filling
