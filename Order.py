from Invoice import Invoice
from OrderState import *

class Order:
    state: OrderState
    def __init__(self, products, ordering, mediator):
        self.ordering = ordering
        self.mediator = mediator
        self.products = products
        self.invoice = Invoice(self.ordering, self.products)

    def set_state(self, state):
        states = {
            "cancelled": OrderCancelledState,
            "fulfilled": OrderFulfilledState,
            "progress": OrderInProgressState
        }
        
        self.state = states[state.lower()](self)
        pass
    
    def notify_mediator_add(self):
        self.mediator.add_to_storage(self.products)
        return
    
    def notify_mediator_remove(self):
        self.mediator.remove_from_storage(self.products)
        return

    def __str__(self):
        return f'{self.invoice.get_number().__str__()} {self.state.__str__()}'

