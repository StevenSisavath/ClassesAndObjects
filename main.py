from alarm_clock import AlarmClock
from customer import Customer
from shopping_cart import ShoppingCart
from product import Product

# test_alarm_clock = AlarmClock()
# test_alarm_clock.set_current_time()
# test_alarm_clock.set_alarm_time()
# test_alarm_clock.set_alarm_on_or_off()
# print(test_alarm_clock.toggle_result) #test

random_customer = Customer(input("What is your name?"))
print(random_customer.name)
product1 = Product('Milk', 3.98, 'dairy')
product2 = Product('Nilla Wafers', 4.18, 'snack')
product3 = Product('Straws', 1.46, 'utensils')
random_customer.add_new_product(product1.name)
random_customer.add_new_product(product2.name)
random_customer.add_new_product(product3.name)
print(random_customer.shopping_cart)