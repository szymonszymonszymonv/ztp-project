import abc
import Order

class OrderState(abc.ABCMeta):
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
        return
    
    def cancel(self):
        self.order.notify_mediator_add()
        return 
    
class OrderFulfilledState(OrderState):
    def __init__(self, order):
        self.order = order
        
    def fulfill(self):
        return
    
    def cancel(self):
        self.order.notify_mediator_add()
        return 
    
class OrderCancelledState(OrderState):
    def __init__(self, order):
        self.order = order
        
    def fulfill(self):
        return
    
    def cancel(self):
        return 