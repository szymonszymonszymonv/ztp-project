from Invoice import Invoice
from OrderCancelledState import OrderCancelledState
from OrderFulfilledState import OrderFulfilledState
from OrderInProgressState import OrderInProgressState


class Order:
    def __init__(self, products,  ordering, state, mediator):
        self.ordering = ordering
        self.state = state
        self.mediator = mediator
        self.products = products
        self.invoice = Invoice(ordering, products)

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


