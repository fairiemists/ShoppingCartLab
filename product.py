from cgi import print_exception
from tokenize import ContStr
from unicodedata import name


class Product:
    
    def __init__(self, product_name, product_price, product_category):
        self.name = product_name
        self.price = product_price 
        self.category = product_category

    