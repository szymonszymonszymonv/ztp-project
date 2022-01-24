import uuid

class Invoice :
    def  __init__(self, ordering, products):
        self.ordering = ordering
        self.products = products
        self.number = uuid.uuid1()
        self.sum_price = self.get_sum_price()

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

    def __str__(self):
        str = f'nr. faktury: {self.number}\nzamawiajacy: {self.ordering}\nsuma: {self.sum_price}\nprodukty: '
        for k, v in self.get_products().items():
            str += f'{k}: x{v}\n'
        
        return str
