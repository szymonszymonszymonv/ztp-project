from IProduct import IProduct
import uuid


class Computer(IProduct):
    operating_system: str
    def __init__(self, desc, price, tax, os):
        self.id = uuid.uuid1()
        self.operating_system = os
        self.description = desc
        self.price = price
        self.tax = tax

    def get_description(self):
        return self.description
    
    def get_price(self):
        return self.price
    
    def get_tax(self):
        return self.tax
    
    def get_operating_system(self):
        return self.operating_system
