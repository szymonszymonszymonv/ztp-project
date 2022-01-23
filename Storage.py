from Singleton import Singleton

class Storage(metaclass=Singleton):
    def __init__(self):
        self.products = {}
        pass
    
    def get_products(self):
        pass
    
    def add_product(self, product):
        pass
    
    def delete_product(self, product):
        pass