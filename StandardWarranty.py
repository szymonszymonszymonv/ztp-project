from Warranty import Warranty


class StandardWarranty(Warranty):

    def get_description(self):
        return f'{self._product.get_description()}, included standard warranty'

    def get_price(self):
        return self._product.get_price() * 1.1

    def get_tax(self):
        return self._product.get_tax() * 1.1