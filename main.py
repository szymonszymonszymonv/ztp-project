from ConcreteCreator import ConcreteCreator
from Storage import Storage
from tkinter import *
from tkinter import ttk
from WarrantyMechanicalDamage import WarrantyMechanicalDamage

from WarrantyTheft import WarrantyTheft

# tv = ConcreteCreator.create("tv", desc="duzy", price=5, tax=2, inches=40)
# tv2 = ConcreteCreator.create("tv", desc="maly", price=2500, tax=100, inches=41)
s = Storage()
# s.add_product(tv)
# s.add_product(tv2)
# s.add_product(tv2)
# s.add_product(tv2)
# s.add_product(tv2)

# iphone = ConcreteCreator.create("phone", desc="iphone12", price=5000, tax=500, bluetooth=True)
# iphone_warranty = WarrantyTheft(iphone)
# iphone_warranties = WarrantyMechanicalDamage(iphone_warranty)

# print(iphone_warranties.get_description())
print(s.get_products())


def populate_list():
    storage_list.delete(0, END)
    for row in s.get_products():
        storage_list.insert(END, row)

def add_tv():
    tv = ConcreteCreator.create("tv", desc=description_text.get(), price=int(price_text.get()),
                                tax=float(tax_text.get()), inches=int(inches_text.get()))
    s.add_product(tv)
    storage_list.delete(0, END)
    populate_list()
    #storage_list.insert(END, (description_text.get(), price_text.get(), tax_text.get(), inches_text.get()))

def add_pc():
    pc = ConcreteCreator.create("computer", desc=pc_description_text.get(), price=int(pc_price_text.get()),
                                tax=float(pc_tax_text.get()), os=system_text.get())
    s.add_product(pc)
    storage_list.delete(0, END)
    populate_list()


def add_phone():
    phone = ConcreteCreator.create("phone", desc=phone_description_text.get(), price=int(phone_price_text.get()),
                                tax=float(phone_tax_text.get()), bluetooth=bluetooth.get())
    s.add_product(phone)
    storage_list.delete(0, END)
    populate_list()

#app initializer
app = Tk()
app.title("Storage")
app.geometry('500x500')

my_notebook = ttk.Notebook(app)
my_notebook.pack(pady=15)

#frames
frame1 = Frame(my_notebook, width=500, height=500)
frame2 = Frame(my_notebook, width=500, height=500)
frame3 = Frame(my_notebook, width=500, height=500)
frame4 = Frame(my_notebook, width=500, height=500)
frame5 = Frame(my_notebook, width=500, height=500)

frame1.pack(fill="both", expand=1)
frame2.pack(fill="both", expand=1)
frame3.pack(fill="both", expand=1)
frame4.pack(fill="both", expand=1)
frame5.pack(fill="both", expand=1)

#adding frames
my_notebook.add(frame1, text="Storage")
my_notebook.add(frame2, text="Add TV")
my_notebook.add(frame3, text="Add Computer")
my_notebook.add(frame4, text="Add Phone")
my_notebook.add(frame5, text="experiment")

#frame1
storage_list = Listbox(frame1, height=8, width=50, border=0)
storage_list.grid(row=2, column=2, columnspan=3, rowspan=6, pady=20, padx=20)
populate_list()

#frame2
# inch
inches_text = StringVar()
inches_label = Label(frame2, text='Inches', font=('bold', 14), pady=20)
inches_label.grid(row=1, column=0, sticky=W)
inches_entry = Entry(frame2, textvariable=inches_text)
inches_entry.grid(row=1, column=1)
# desc
description_text = StringVar()
description_label = Label(frame2, text='Description', font=('bold', 14))
description_label.grid(row=1, column=2, sticky=W)
description_entry = Entry(frame2, textvariable=description_text)
description_entry.grid(row=1, column=3)
# price
price_text = StringVar()
price_label = Label(frame2, text='Price', font=('bold', 14))
price_label.grid(row=2, column=2, sticky=W)
price_entry = Entry(frame2, textvariable=price_text)
price_entry.grid(row=2, column=3)
# tax
tax_text = StringVar()
tax_label = Label(frame2, text='Tax', font=('bold', 14))
tax_label.grid(row=2, column=0, sticky=W)
tax_entry = Entry(frame2, textvariable=tax_text)
tax_entry.grid(row=2, column=1)

add_btn = Button(frame2, text='Add TV', width=12, command=add_tv)
add_btn.grid(row=3, column=0, pady=20)

#frame3
system_text = StringVar()
system_label = Label(frame3, text='System', font=('bold', 14), pady=20)
system_label.grid(row=1, column=0, sticky=W)
system_entry = Entry(frame3, textvariable=system_text)
system_entry.grid(row=1, column=1)
# desc
pc_description_text = StringVar()
pc_description_label = Label(frame3, text='Description', font=('bold', 14))
pc_description_label.grid(row=1, column=2, sticky=W)
pc_description_entry = Entry(frame3, textvariable=pc_description_text)
pc_description_entry.grid(row=1, column=3)
# price
pc_price_text = StringVar()
pc_price_label = Label(frame3, text='Price', font=('bold', 14))
pc_price_label.grid(row=2, column=2, sticky=W)
pc_price_entry = Entry(frame3, textvariable=pc_price_text)
pc_price_entry.grid(row=2, column=3)
# tax
pc_tax_text = StringVar()
pc_tax_label = Label(frame3, text='Tax', font=('bold', 14))
pc_tax_label.grid(row=2, column=0, sticky=W)
pc_tax_entry = Entry(frame3, textvariable=pc_tax_text)
pc_tax_entry.grid(row=2, column=1)

add_btn = Button(frame3, text='Add PC', width=12, command=add_pc)
add_btn.grid(row=3, column=0, pady=20)

#frame4
bluetooth = BooleanVar()
bluetooth_label = Label(frame4, text='Bluetooth', font=('bold', 14), pady=20)
bluetooth_label.grid(row=1, column=0, sticky=W)
bluetooth_entry = Checkbutton(frame4, variable=bluetooth, onvalue=True, offvalue=False)
bluetooth_entry.grid(row=1, column=1)
# desc
phone_description_text = StringVar()
phone_description_label = Label(frame4, text='Description', font=('bold', 14))
phone_description_label.grid(row=1, column=2, sticky=W)
phone_description_entry = Entry(frame4, textvariable=phone_description_text)
phone_description_entry.grid(row=1, column=3)
# price
phone_price_text = StringVar()
phone_price_label = Label(frame4, text='Price', font=('bold', 14))
phone_price_label.grid(row=2, column=2, sticky=W)
phone_price_entry = Entry(frame4, textvariable=phone_price_text)
phone_price_entry.grid(row=2, column=3)
# tax
phone_tax_text = StringVar()
phone_tax_label = Label(frame4, text='Tax', font=('bold', 14))
phone_tax_label.grid(row=2, column=0, sticky=W)
phone_tax_entry = Entry(frame4, textvariable=phone_tax_text)
phone_tax_entry.grid(row=2, column=1)

add_btn = Button(frame4, text='Add Phone', width=12, command=add_phone)
add_btn.grid(row=3, column=0, pady=20)

#frame5
def generate_input():
    #phone
    if selected.get() == 1:
        inches_label.pack_forget()
        inches_entry.pack_forget()
        system_label.pack_forget()
        system_entry.pack_forget()
        bluetooth_label.pack(side="top")
        bluetooth_entry.pack(side="top")
    #computer
    if selected.get() == 2:
        inches_label.pack_forget()
        inches_entry.pack_forget()
        bluetooth_entry.pack_forget()
        bluetooth_label.pack_forget()
        system_label.pack(side="top")
        system_entry.pack(side="top")

    #tv
    if selected.get() == 3:
        system_label.pack_forget()
        system_entry.pack_forget()
        bluetooth_entry.pack_forget()
        bluetooth_label.pack_forget()
        inches_label.pack(side="top")
        inches_entry.pack(side="top")
        
def add_product():
    #phone
    product = None
    if selected.get() == 1:
        active_field = bluetooth.get()
        product_type = "phone"
        
    #computer
    if selected.get() == 2:
        active_field = system_text.get()
        product_type = "computer"
        
    #tv
    if selected.get() == 3:
        product_type = "tv"
        active_field = inches_text.get()
        
    product = ConcreteCreator.create(product_type,
                              description_text.get(),
                              price_text.get(),
                              tax_text.get(),
                              active_field)
        
    s.add_product(product)
    storage_list.delete(0, END)
    populate_list()

selected = IntVar()
rad1 = Radiobutton(frame5, text="phone", value=1, variable=selected, command=generate_input)
rad1.pack(side="left")
# rad1.grid(row=0, column=0, sticky=N)
rad2 = Radiobutton(frame5, text="computer", value=2, variable=selected, command=generate_input)
rad2.pack(side="left")
# rad2.grid(row=0, column=1, sticky=N)
rad3 = Radiobutton(frame5, text="tv", value=3, variable=selected, command=generate_input)
rad3.pack(side="left")
frame6 = Frame(frame5)
frame6.pack(side="right")
# rad3.grid(row=0, column=2, sticky=N)
inches_text = StringVar()
inches_label = Label(frame6, text='Inches', font=('bold', 14), pady=20)
# inches_label.grid(row=1, column=0, sticky=W)
inches_entry = Entry(frame6, textvariable=inches_text)
# inches_entry.grid(row=1, column=1)
system_text = StringVar()
system_label = Label(frame6, text='System', font=('bold', 14), pady=20)
# system_label.grid(row=1, column=0, sticky=W)
system_entry = Entry(frame6, textvariable=system_text)
# system_entry.grid(row=1, column=1)
bluetooth = BooleanVar()
bluetooth_label = Label(frame6, text='Bluetooth', font=('bold', 14), pady=20)
# bluetooth_label.grid(row=1, column=0, sticky=W)
bluetooth_entry = Checkbutton(frame6, variable=bluetooth, onvalue=True, offvalue=False)
# bluetooth_entry.grid(row=1, column=1)

# desc
description_text = StringVar()
description_label = Label(frame6, text='Description', font=('bold', 14))
description_entry = Entry(frame6, textvariable=description_text)
description_label.pack(side="top")
description_entry.pack(side="top")
# price
price_text = StringVar()
price_label = Label(frame6, text='Price', font=('bold', 14))
price_entry = Entry(frame6, textvariable=price_text)
price_label.pack(side="top")
price_entry.pack(side="top")
# tax
tax_text = StringVar()
tax_label = Label(frame6, text='Tax', font=('bold', 14))
tax_entry = Entry(frame6, textvariable=tax_text)
tax_label.pack(side="top")
tax_entry.pack(side="top")

bluetooth_label.pack(side="top")
bluetooth_entry.pack(side="top")

add_btn = Button(frame6, text='Add Product', width=12, command=add_product)
add_btn.pack(side="bottom")

print(s.get_products())

app.mainloop()


# factory test
