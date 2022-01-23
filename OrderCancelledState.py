from OrderState import OrderState


class OrderCancelledState(OrderState):
    def __init__(self, order):
        self.order = order
        
    def fulfill(self):
        return
    
    def cancel(self):
        return 