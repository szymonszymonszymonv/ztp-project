from Singleton import Singleton

class Storage(metaclass=Singleton):
    def __init__(self):
        self.products = {}
        pass
    
    def get_products(self):
        return self.products
    
    def add_product(self, product):
        if product in self.products:
            self.products[product] += 1
        else:
            self.products[product] = 1
    
    def delete_product(self, product):
        if not product in self.products:
            return False
        self.products[product] -= 1
        if self.products[product] == 0:
            self.products.pop(product, None)
            