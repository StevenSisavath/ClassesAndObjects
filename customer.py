from shopping_cart import ShoppingCart
class Customer:
    
    def __init__(self, name) :
        self.name = name
        self.shopping_cart = ShoppingCart()

    def add_new_product(self, product_to_add):
        self.shopping_cart.add_product_to_list(product_to_add)
    
    def view_shopping_cart_items(self):
        for self.item in self.shopping_cart.list_of_products: #ShoppingCart.list_of_products():
            print(self.item)