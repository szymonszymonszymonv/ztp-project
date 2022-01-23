from Warranty import Warranty


class WarrantyMechanicalDamage(Warranty):

    def get_description(self):
        return self.warranty.get_description()

    def get_price(self):
        return self.warranty.get_price()

    def get_tax(self):
        return self.warranty.get_tax()
