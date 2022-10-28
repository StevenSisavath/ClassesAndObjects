class ShoppingCart:
    def __init__(self):
        self.list_of_products = []

    def add_product_to_list(self, product_to_add):
        self.list_of_products.append(product_to_add)

    def return_total_of_list(self):
        return len(self.list_of_products)

    def remove_all_products_in_list(self):
        self.list_of_products.clear()