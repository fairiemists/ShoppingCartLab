from shopping_cart import ShoppingCart


class Customer:

    def __init__(self, name) -> None:
        self.name = name
        self.cart = ShoppingCart()


    def add_new_product(self, product):
        self.cart.add_product_to_cart(product)   # got syntax from solution walkthrough


    def see_items_in_cart(self):   # got from solution walkthrough
        for product in self.cart.products:
            print(product.product_name)



# Method to add a new product to the shopping cart 
# (within this method you will call the shopping cart's add product method)

# Method to view all products in the shopping cart. 
# (Loop over the shopping cart's products list and print each product to the terminal)

