from Warranty import Warranty


class WarrantyTheft(Warranty):

    def get_description(self):
        return f'{self._product.get_description()}, included theft warranty'

    def get_price(self):
        return self._product.get_price() * 1.05

    def get_tax(self):
        return self._product.get_tax() * 1.05





