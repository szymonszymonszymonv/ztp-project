import uuid

class Invoice :
    def  __init__(self, ordering, products):
        self.ordering = ordering
        self.products = products
        self.number = uuid.uuid4()
        self.sumPrice = self.get_sum_price()

    def get_ordering(self):
        return self.ordering


    def get_sum_price(self):
        sum_price = 0
        for val in self.products:
            price = val.get_price()
            price *= ((val.get_tax() + 100) / 100)
            sum_price += price
        return sum_price

    def get_products(self):
        return self.products
    
    def get_number(self):
        return self.number

