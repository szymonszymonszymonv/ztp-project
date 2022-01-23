

class Order:
    def __init__(self, products,  ordering, state, invoice, mediator):
        self.ordering = ordering
        self.state = state
        self.invoice = invoice
        self.mediator = mediator
        self.products = products


#     def setState(self, state):
# #         wyslij state do mediatora pewnie

