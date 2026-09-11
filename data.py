BUN_NAME = "Краторная булка"
BUN_PRICE = 100

SAUCE_TYPE = "SAUCE"
SAUCE_NAME = "Соус с шипами Антарианского плоскоходца"
SAUCE_PRICE = 25

FILLING_TYPE = "FILLING"
FILLING_NAME = "Мясо бессмертных моллюсков Protostomia"
FILLING_PRICE = 75

BUN_ONLY_PRICE = BUN_PRICE * 2
BURGER_WITH_SAUCE_PRICE = BUN_ONLY_PRICE + SAUCE_PRICE
BURGER_WITH_FILLING_PRICE = BUN_ONLY_PRICE + FILLING_PRICE
FULL_BURGER_PRICE = BUN_ONLY_PRICE + SAUCE_PRICE + FILLING_PRICE

RECEIPT_WITH_SAUCE_AND_FILLING = (
    f"(==== {BUN_NAME} ====)\n"
    f"= {SAUCE_TYPE.lower()} {SAUCE_NAME} =\n"
    f"= {FILLING_TYPE.lower()} {FILLING_NAME} =\n"
    f"(==== {BUN_NAME} ====)\n\n"
    f"Price: {FULL_BURGER_PRICE}"
)

RECEIPT_WITH_FILLING_AND_SAUCE = (
    f"(==== {BUN_NAME} ====)\n"
    f"= {FILLING_TYPE.lower()} {FILLING_NAME} =\n"
    f"= {SAUCE_TYPE.lower()} {SAUCE_NAME} =\n"
    f"(==== {BUN_NAME} ====)\n\n"
    f"Price: {FULL_BURGER_PRICE}"
)
