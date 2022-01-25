from IProduct import IProduct

class Warranty(IProduct):

    def __init__(self, product):
        if not hasattr(product, 'original'):
            self.original = product
        else:
            self.original = product.original
            
        self._product = product
        self.id = product.id

    def get_description(self):
        return self._product.description

    def get_price(self):
        return self._product.price

    def get_tax(self):
        return self._product.tax


