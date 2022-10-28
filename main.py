from alarm_clock import AlarmClock
from customer import Customer
from shopping_cart import ShoppingCart
from product import Product
from cell_phone import CellPhone

# Alarm Clock Tasks
# test_alarm_clock = AlarmClock()
# test_alarm_clock.set_current_time()
# test_alarm_clock.set_alarm_time()
# test_alarm_clock.set_alarm_on_or_off()
# print(test_alarm_clock.toggle_result) #test

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Customer Shopping Cart Tasks
# 1. Print the customer’s name to the terminal 
# random_customer = Customer(input("What is your name?"))
# print(random_customer.name)

# #2. Call the customer’s add product to shopping cart method three times and add the three products objects you created 
# product1 = Product('Milk', 3.98, 'dairy')
# product2 = Product('Nilla Wafers', 4.18, 'snack')
# product3 = Product('Straws', 1.46, 'utensils')
# random_customer.add_new_product(product1.name)
# random_customer.add_new_product(product2.name)
# random_customer.add_new_product(product3.name)

# # 3. Call the customer’s view products method 
# random_customer.view_shopping_cart_items()

# # 4. Call the customer’s shopping cart’s get cart total method. Capture the total the method returns in a variable and print to the terminal 
# print(random_customer.shopping_cart.return_total_of_list())

# # 5. Call the customer’s shopping cart’s empty cart method 
# random_customer.shopping_cart.remove_all_products_in_list()

# # 6. Check if all products have been removed from the shopping cart 
# print('')
# print(random_customer.view_shopping_cart_items())
# print('')

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# BONUS: Cell Phone Tasks
# 1. Print the cell phone’s contacts to the terminal 
new_cell_phone = CellPhone('iPhone13', '7777777777')
for field, property in new_cell_phone.contacts.items():
    print(property)

# 2. Send two new messages to the phone through the receive text message method 
new_cell_phone.recieve_text('Hi')
new_cell_phone.recieve_text('Bye')

# 3. Print the cell phone’s messages to the terminal 
for element in new_cell_phone.messages_recieved:
    print(element)

# 4. Call the create text message method to create a new message 
new_cell_phone.send_text('Yo yo yo')

# 5. Toggle the cell phones ringer to vibrate 
new_cell_phone.toggle_vibrate_mode()

# 6. Print the cell phone’s current ringer/vibrate setting to the terminal 
print(new_cell_phone.vibrate_on)