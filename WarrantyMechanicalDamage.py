from Warranty import Warranty


class WarrantyMechanicalDamage(Warranty):

    def get_description(self):
        return f'{self._product.get_description()}, included mechanical damage warranty'

    def get_price(self):
        return self._product.get_price() * 1.15

    def get_tax(self):
        return self._product.get_tax() * 1.15
