from ConcreteCreator import ConcreteCreator
from Storage import Storage
# factory test
tv = ConcreteCreator.create("tv", desc="duzy", price=5, tax=2, inches=40)
tv2 = ConcreteCreator.create("tv", desc="maly", price=2500, tax=100, inches=41)
s = Storage()
s.add_product(tv)
s.add_product(tv2)
s.add_product(tv2)
s.add_product(tv2)
s.add_product(tv2)
print(s.get_products())