import abc

class Factory(abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'create') and
                callable(subclass.create) and
                NotImplemented)
        
    @abc.abstractmethod
    def create(t, **kwargs):
        """create object of type t"""