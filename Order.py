from Invoice import Invoice
import OrderState

class Order:
    state: OrderState
    def __init__(self, products, ordering, mediator):
        self.ordering = ordering
        self.mediator = mediator
        self.products = products
        self.invoice = Invoice(ordering, products)

    def set_state(self, state):
        states = {
            "cancelled": Order.OrderCancelledState,
            "fulfilled": Order.OrderFulfilledState,
            "progress": Order.OrderInProgressState
        }
        
        self.state = states[state.lower()](self)
        pass
    
    def notify_mediator_add(self):
        self.mediator.add_to_storage(self.products)
        return
    
    def notify_mediator_remove(self):
        self.mediator.remove_from_storage(self.products)
        return


