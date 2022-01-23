import Order

class Invoice :

    def  __init__(self, ordering, products):
        self.ordering = ordering
        self.products = products

    def get_ordering(self):
        print(self.ordering)
        return self.ordering


    def get_sum_price(self):
        sum_price = 0
        for val in self.products:
            sum_price += val.price
            sum_price *= ((val.tax + 100) / 100)
        return sum_price

    def get_products(self):
        print(self.products.description)
        return self.products






