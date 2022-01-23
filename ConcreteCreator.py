from Factory import Factory
from Phone import Phone
from Tv import Tv
from Computer import Computer

class ConcreteCreator(Factory):
    
    def create(t, **kwargs):
        types = {
            "phone": Phone,
            "computer": Computer,
            "tv": Tv
        }
        return types[t.lower()](**kwargs)
