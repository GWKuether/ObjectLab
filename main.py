
from itertools import product
from shopping_cart import ShoppingCart
from product import Product
from customer import Customer


# from alarm_clock import AlarmClock

# alarm_clock_1 = AlarmClock("10:00 AM", True, "10:05 AM")

# print(alarm_clock_1.current_time)
# print(alarm_clock_1.is_alarm_clock_on)
# print(alarm_clock_1.alarm_time)

corn = Product("Corn", "$1", "Vegetable")

shopping_cart_1 = ShoppingCart("Silver")

shopping_cart_1.add_product_to_cart(corn)
shopping_cart_1.add_product_to_cart(corn)
shopping_cart_1.add_product_to_cart(corn)

print(len(shopping_cart_1.shopping_carts_products))


shopping_cart_1.how_many_products_inside()

shopping_cart_1.remove_all_products_from_cart()

shopping_cart_1.how_many_products_inside()

customer_1 = Customer("Bill")

print(customer_1.name)

customer_1.add_product_to_cart.add_product_to_cart(corn)
