prices = {"breat": 20, "milk": 80, "cheese": 25}
cart = {"breat": 2, "cola": 1, "milk": 3}
d = 0

for product, quantity in cart.items():
    if product in prices:
        d += prices[product]*quantity
    else:
        print(f"Товар {product} отсутствует в прайс-листе")

print(f"Общая стоимость {d}")