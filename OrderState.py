import abc
import Order

class OrderState(abc.ABC):
    order: Order
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'fulfill') and
                callable(subclass.fulfill) and
                hasattr(subclass, 'cancel') and
                callable(subclass.cancel) or
                NotImplemented)
        
    @abc.abstractmethod
    def fulfill(self):
        """fulfill order"""
        raise NotImplementedError
        
    def cancel(self):
        """cancel order"""
        raise NotImplementedError
    


class OrderInProgressState(OrderState):
    def __init__(self, order):
        self.order = order
        
    def fulfill(self):
        self.order.notify_mediator_remove()
        self.order.set_state("fulfilled")
        return
    
    def cancel(self):
        self.order.notify_mediator_add()
        self.order.set_state("cancelled")
        return 
    
    def __str__(self):
        return "in progress"
    
class OrderFulfilledState(OrderState):
    def __init__(self, order):
        self.order = order
        
    def fulfill(self):
        return
    
    def cancel(self):
        self.order.set_state("cancelled")
        self.order.notify_mediator_add()
        return 
    
    def __str__(self):
        return "fulfilled"
    
class OrderCancelledState(OrderState):
    def __init__(self, order):
        self.order = order
        
    def fulfill(self):
        return
    
    def cancel(self):
        return 
    
    def __str__(self):
        return "cancelled"