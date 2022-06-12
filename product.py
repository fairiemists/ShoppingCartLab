from cgi import print_exception
from tokenize import ContStr
from unicodedata import name


class Product:
    
    def __init__(self, name, price, product_category):
        self.name = name
        self.price = price 
        self.category = product_category

    