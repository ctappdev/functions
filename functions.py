def required_return_price(*, unit_price: int, unit_qty: int) -> int:

    """Calculate a total price with required named key word arguments"""
    print(f"Required Unit Price {unit_price}")
    print(f"Required Unit Quantity {unit_qty}")

    return unit_price * unit_qty


def optional_return_price(unit_price: int, unit_qty: int) -> int:
    """Calculate a total price with optional named key word arguments"""
    print(f"Optional Unit Price {unit_price}")
    print(f"Optional Unit Quantity {unit_qty}")

    return unit_price * unit_qty


calc_price = required_return_price(unit_price=10, unit_qty=5)
print(f"Type is {type(calc_price)}")
print(f"Price 1 is {calc_price}")


calc_price = optional_return_price(calc_price, 5)
print(f"Price 2 is {calc_price}")
