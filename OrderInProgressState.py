from OrderState import OrderState


class OrderInProgressState(OrderState):
    def __init__(self, order):
        self.order = order
        
    def fulfill(self):
        self.order.notify_mediator_remove()
        return
    
    def cancel(self):
        self.order.notify_mediator_add()
        return 