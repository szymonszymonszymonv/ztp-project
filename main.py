from ConcreteCreator import ConcreteCreator

# factory test
tv = ConcreteCreator.create("tv", desc="duzy", price=5, tax=2, inches=40)
print(tv)