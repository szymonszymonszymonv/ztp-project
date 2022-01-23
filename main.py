from ConcreteCreator import ConcreteCreator
from Storage import Storage
from tkinter import *
from tkinter import ttk

tv = ConcreteCreator.create("tv", desc="duzy", price=5, tax=2, inches=40)
tv2 = ConcreteCreator.create("tv", desc="maly", price=2500, tax=100, inches=41)
s = Storage()
s.add_product(tv)
s.add_product(tv2)
s.add_product(tv2)
s.add_product(tv2)
s.add_product(tv2)
print(s.get_products())


def populate_list():
    storage_list.delete(0, END)
    for row in s.get_products():
        storage_list.insert(END, row)

def add_tv():
    tv = ConcreteCreator.create("tv", desc=description_text.get(), price=int(price_text.get()),
                                tax=int(tax_text.get()), inches=int(inches_text.get()))
    s.add_product(tv)
    storage_list.delete(0, END)
    populate_list()
    #storage_list.insert(END, (description_text.get(), price_text.get(), tax_text.get(), inches_text.get()))

def add_pc():
    pc = ConcreteCreator.create("computer", desc=pc_description_text.get(), price=int(pc_price_text.get()),
                                tax=int(pc_tax_text.get()), os=system_text.get())
    s.add_product(pc)
    storage_list.delete(0, END)
    populate_list()


def add_phone():
    phone = ConcreteCreator.create("phone", desc=phone_description_text.get(), price=int(phone_price_text.get()),
                                tax=int(phone_tax_text.get()), bluetooth=bluetooth.get())
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

frame1.pack(fill="both", expand=1)
frame2.pack(fill="both", expand=1)
frame3.pack(fill="both", expand=1)
frame4.pack(fill="both", expand=1)

#adding frames
my_notebook.add(frame1, text="Storage")
my_notebook.add(frame2, text="Add TV")
my_notebook.add(frame3, text="Add Computer")
my_notebook.add(frame4, text="Add Phone")

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


print(s.get_products())

app.mainloop()


# factory test
