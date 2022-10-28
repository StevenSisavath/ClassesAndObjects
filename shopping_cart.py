from product import Product
class ShoppingCart:
    def __init__(self):
        self.list_of_products = []
        self.total_price_of_products = Product()

    def add_product_to_list(self, product_to_add):
        self.list_of_products.append(product_to_add)

    def return_total_of_list(self):
        total = 0.00
        for self.price in range(len(self.list_of_products-1)):
            total += self.price           
        return len(self.list_of_products)

    def remove_all_products_in_list(self):
        self.list_of_products.clear()