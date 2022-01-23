import abc

class IProduct(metaclass=abc.ABCMeta):
    price: int
    description: str
    tax: float
    
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_description') and
                callable(subclass.get_description) and
                hasattr(subclass, 'get_price') and
                callable(subclass.get_price) and
                hasattr(subclass, 'get_tax') and
                callable(subclass.get_tax) or
                NotImplemented)
        
    @abc.abstractmethod
    def get_description(self):
        """get product description"""
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_price(self):
        """get product price"""
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_tax(self):
        """get product tax"""
        raise NotImplementedError