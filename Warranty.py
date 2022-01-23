

class Warranty:

    def __init__(self, product):
        self._product = product

    def get_description(self):
        return self._product.description

    def get_price(self):
        return self._product.price

    def get_tax(self):
        return self._product.tax


