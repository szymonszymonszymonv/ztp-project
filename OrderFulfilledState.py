from OrderState import OrderState


class OrderFulfilledState(OrderState):
    def __init__(self, order):
        self.order = order
        
    def fulfill(self):
        return
    
    def cancel(self):
        self.order.notify_mediator_add()
        return 