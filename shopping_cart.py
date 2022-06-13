
class ShoppingCart:

    def __init__(self):
        self.products = []   


    def add_product_to_cart(self, product):
        self.products.append(product)


    def remove_product_from_cart(self, product):
        self.products.remove(product)

    def empty_cart(self):
        self.products.clear() # got from solution walkthrough
        
    
    def calculate_cart_total(self):  # got from solution walkthrough
        final_total = 0
        for product in self.products:
            final_total += product.product_price
            return final_total




# Class properties to keep track of the ShoppingCart's products (list)

# Method to calculate & return current total of all products in the cart

# Method to add new products to the cart (appending to the products list)

# Method to empty all carts from the shopping cart




