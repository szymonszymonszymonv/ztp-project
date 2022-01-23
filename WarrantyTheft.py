from Warranty import Warranty


class WarrantyTheft(Warranty):

    def __init__(self, description, price, product):
        super().__init__(product)
        self.description = description
        self.price = price


    def get_description(self):
        return self.warranty.get_description()

    def get_price(self):
        return self.warranty.get_price()

    def get_tax(self):
        return self.warranty.get_tax()





