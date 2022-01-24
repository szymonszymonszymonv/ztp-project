from ConcreteCreator import ConcreteCreator
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

selected_product = None

def populate_list():
    new_list = []
    storage_list.delete(0, END)
        
    for i, (k, v) in enumerate(s.get_products().items()):
        print(f'POPULATE_LIST(): {i, k, v}')
        storage_list.insert(i, k)
        

def select_item(event):
    global select_item
    index = storage_list.curselection()[0]
    selected_item = storage_list.get(index)
    selected_product = list(s.get_products())[index]
    
def buy_product():
    # robimy order z ziomkiem i produktami
    
    


#app initializer
app = Tk()
app.title("Storage")
app.geometry('500x500')

my_notebook = ttk.Notebook(app)
my_notebook.pack(pady=15)

#frames
frame1 = Frame(my_notebook, width=500, height=500)
frame5 = Frame(my_notebook, width=500, height=500)

frame1.pack(fill="both", expand=1)
frame5.pack(fill="both", expand=1)

#adding frames
my_notebook.add(frame1, text="Storage")
my_notebook.add(frame5, text="experiment")

#frame1
storage_list = Listbox(frame1, height=8, width=50, border=0)
storage_list.grid(row=1, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
#scrollbar
scrollbar= Scrollbar(frame1)
scrollbar.grid(row=4, column=3)
#scroll to listbox
storage_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=storage_list.yview)
populate_list()
#bind select
storage_list.bind('<<ListboxSelect>>', select_item)


#warranties
#standard
warranty = BooleanVar()
warranty_label = Label(frame1, text='Standard', font=('bold', 10))
warranty_label.grid(row=1, column=5, sticky=W)
warranty_entry = Checkbutton(frame1, variable=warranty, onvalue=True, offvalue=False)
warranty_entry.grid(row=1, column=6)

#theftwarranty
theft_warranty = BooleanVar()
theft_warranty_label = Label(frame1, text='Theft', font=('bold', 10))
theft_warranty_label.grid(row=2, column=5, sticky=W)
theft_warranty_entry = Checkbutton(frame1, variable=theft_warranty, onvalue=True, offvalue=False)
theft_warranty_entry.grid(row=2, column=6)

#mechanicalwarranty
mechanical_warranty = BooleanVar()
mechanical_warranty_label = Label(frame1, text='Mechanical', font=('bold', 10))
mechanical_warranty_label.grid(row=3, column=5, sticky=W)
mechanical_warranty_entry = Checkbutton(frame1, variable=mechanical_warranty, onvalue=True, offvalue=False)
mechanical_warranty_entry.grid(row=3, column=6)

#buybutton(?)
buy_btn = Button(frame1, text='Buy item', width=12, command=buy_product)
buy_btn.grid(row=7, column=0, pady=10)

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
    product_type = ""
    active_field = None
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
    print(f'selected type: {product_type}')
        
    product = ConcreteCreator.create(product_type,
                              description_text.get(),
                              price_text.get(),
                              tax_text.get(),
                              active_field)
    print(f'adding {type(product)} ({product})')
        
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

app.mainloop()


# factory test
