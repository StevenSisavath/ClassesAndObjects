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
# 1. Print the customer’s name to the terminal 
random_customer = Customer(input("What is your name?"))
print(random_customer.name)

#2. Call the customer’s add product to shopping cart method three times and add the three products objects you created 
product1 = Product('Milk', 3.98, 'dairy')
product2 = Product('Nilla Wafers', 4.18, 'snack')
product3 = Product('Straws', 1.46, 'utensils')
random_customer.add_new_product(product1.name)
random_customer.add_new_product(product2.name)
random_customer.add_new_product(product3.name)

# 3. Call the customer’s view products method 
random_customer.view_shopping_cart_items()

# 4. Call the customer’s shopping cart’s get cart total method. Capture the total the method returns in a variable and print to the terminal 
print(random_customer.shopping_cart.return_total_of_list())

# 5. Call the customer’s shopping cart’s empty cart method 
random_customer.shopping_cart.remove_all_products_in_list()

# 6. Check if all products have been removed from the shopping cart 
print('')
print(random_customer.view_shopping_cart_items())
print('')