from IProduct import IProduct
import uuid

class Phone(IProduct):
    bluetooth: bool
    def __init__(self, desc, price, tax, bluetooth):
        self.id = uuid.uuid1()
        self.bluetooth = bluetooth
        self.description = desc
        self.price = price
        self.tax = tax
        
    def get_description(self):
        return self.description
    
    def get_price(self):
        return self.price
    
    def get_tax(self):
        return self.tax
        
    def get_bluetooth(self):
        return self.bluetooth