from Factory import Factory
from Phone import Phone
from Tv import Tv
from Computer import Computer

class ConcreteCreator(Factory):
    
    def create(t, *args):
        types = {
            "phone": Phone,
            "computer": Computer,
            "tv": Tv
        }
        print(args)
        return types[t.lower()](*args)
