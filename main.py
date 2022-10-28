from alarm_clock import AlarmClock
from customer import Customer
from shopping_cart import ShoppingCart
from product import Product

# Alarm Clock Tasks
# test_alarm_clock = AlarmClock()
# test_alarm_clock.set_current_time()
# test_alarm_clock.set_alarm_time()
# test_alarm_clock.set_alarm_on_or_off()
# print(test_alarm_clock.toggle_result) #test

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Customer Shopping Cart Tasks
# 1.
random_customer = Customer(input("What is your name?"))
print(random_customer.name)

#2. 
product1 = Product('Milk', 3.98, 'dairy')
product2 = Product('Nilla Wafers', 4.18, 'snack')
product3 = Product('Straws', 1.46, 'utensils')
random_customer.add_new_product(product1.name)
random_customer.add_new_product(product2.name)
random_customer.add_new_product(product3.name)

# 3.
random_customer.view_shopping_cart_items()

# 4.
print(random_customer.shopping_cart.return_total_of_list())

# 5.
random_customer.shopping_cart.remove_all_products_in_list()

# 6.
print('')
print(random_customer.view_shopping_cart_items())
print('')