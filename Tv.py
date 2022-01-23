from IProduct import IProduct

class Tv(IProduct):
    inches: float
    def __init__(self, desc, price, tax, inches):
        self.inches = inches
        self.description = desc
        self.price = price
        self.tax = tax

    def get_description(self):
        return self.description
    
    def get_price(self):
        return self.price
    
    def get_tax(self):
        return self.tax
    
    def get_inches(self):
        return self.get_inches
