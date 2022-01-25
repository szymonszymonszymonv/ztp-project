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
        if self.products[product] <= 0:
            self.products.pop(product, None)
            
    def add_products(self, products):
        # for key, val in products.items():
        #     added = False
        #     for product, quantity in self.products.items():
        #         if key.id == product.id:
        #             self.products[product] += val
        #             added = True
        #         if not added:
        #             self.products[key]
        
        for key, val in products.items():
            prod = key
            if hasattr(key, 'original'):
                prod = key.original
            if prod in self.products:
                self.products[prod] += val
            else:
                self.products[prod] = val
                
    def delete_products(self, products):
        for key, val in products.items():
            prod = key
            if hasattr(key, 'original'):
                prod = key.original
            
            if prod in self.products:
                self.products[prod] -= val
                if self.products[prod] <= 0:
                    self.products.pop(prod, None)
        #     for product, quantity in self.products.items():
        #         if key.id == product.id:
        #             self.products[product] -= val
        #         if self.products[product] <= 0:
        #             self.products.pop(product, None)
            
        pass
            