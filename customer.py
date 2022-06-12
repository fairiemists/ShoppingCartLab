from shopping_cart import ShoppingCart

class Customer:

    def __init__(self, name) -> None:
        self.name = name
        self.cart_object = ShoppingCart()
