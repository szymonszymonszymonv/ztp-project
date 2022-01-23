import abc

from Order import Order

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
    
    