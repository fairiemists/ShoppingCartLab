from product import Product

class ShoppingCart:

    def __init__(self):
        self.product = Product()
        self.product_list = []   


    def add_product_to_cart(self):
        self.product = Product()


    def remove_product_from_cart(self, product_name):
        self.product = product_name

    def empty_cart(self):
        self.product_list

    



# Class properties to keep track of the ShoppingCart's products (list)

# Method to calculate & return current total of all products in the cart

# Method to add new products to the cart (appending to the products list)

# Method to empty all carts from the shopping cart




