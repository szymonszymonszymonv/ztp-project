from ConcreteCreator import ConcreteCreator
from IProduct import IProduct
from ShoppingView import ShoppingView
from Storage import Storage
from tkinter import *
from tkinter import ttk
from WarrantyMechanicalDamage import WarrantyMechanicalDamage

from WarrantyTheft import WarrantyTheft

tv = ConcreteCreator.create("tv", "duzy LG", 5, 2, 40)
tv2 = ConcreteCreator.create("tv", "maly Samsung", 2500, 100, 41)
s = Storage()
s.add_product(tv)
s.add_product(tv2)
s.add_product(tv2)
s.add_product(tv2)

#app initializer
app = Tk()
app.title("Storage")
app.geometry('600x500')

my_notebook = ttk.Notebook(app)
my_notebook.pack(pady=15)

shopping_view = ShoppingView(app, my_notebook)
shopping_view.create_view()

app.mainloop()


# factory test
