from ConcreteCreator import ConcreteCreator
from Mediator import Mediator
from Storage import Storage
from tkinter import *
from StandardWarranty import StandardWarranty
from WarrantyMechanicalDamage import WarrantyMechanicalDamage
from WarrantyTheft import WarrantyTheft
from Order import Order

class ShoppingView():
    def __init__(self, app, notebook):
        self.app = app
        self.notebook = notebook
        self.storage = Storage()
        self.mediator = Mediator(self.storage)
        self.frame1 = Frame(self.notebook, width=500, height=500)
        self.frame5 = Frame(self.notebook, width=500, height=500)
        self.storage_list = Listbox(self.frame1, height=8, width=50, border=0)
        self.order_box = Text(self.frame1, wrap=WORD, height=8, width=37)
        self.chosen_product = None
        self.product_idx = -1
        self.products_cart = {}
        self.orders = []
        
    def create_view(self):
        
        def populate_list():
            self.storage_list.delete(0, END)
            for i, (k, v) in enumerate(self.storage.get_products().items()):
                self.storage_list.insert(i, k)

        def select_item(e):
            global select_item
            index = self.storage_list.curselection()[0]
            selected_product = list(self.storage.get_products())[index]
            self.chosen_product = selected_product
            print(f"SELECTING: {selected_product}")
            
        def make_order():
            ordering = name_text.get()
            order = Order(self.products_cart, ordering, self.mediator)
            self.orders.append(order)
            print(self.orders)
        
        def buy_product():
            
            p = StandardWarranty(self.chosen_product) if warranty.get() else self.chosen_product
            p = WarrantyMechanicalDamage(p) if mechanical_warranty.get() else p
            p = WarrantyTheft(p) if theft_warranty.get() else p
            print(f'KUPUJE PRODUKT: {p}')
            
            if not p in self.products_cart:
                self.products_cart[p] = 1
                self.order_box.insert(END, "- ")
                self.order_box.insert(END, p )
                self.order_box.insert(END, "\n")
            else:
                self.products_cart[p] += 1
                self.order_box.insert(END, "- ")
                self.order_box.insert(END, p)
                self.order_box.insert(END, "\n")
                
            # print(self.products_cart)
            for k, v in self.products_cart.items():
                print(k.__str__())
            # robimy order z ziomkiem i produktami
        #frames
        frame1 = Frame(self.notebook, width=500, height=500)
        frame5 = Frame(self.notebook, width=500, height=500)

        frame1.pack(fill="both", expand=1)
        frame5.pack(fill="both", expand=1)

        #adding frames
        self.notebook.add(frame1, text="Storage")
        self.notebook.add(frame5, text="experiment")

        #frame1
        self.storage_list = Listbox(frame1, height=8, width=50, border=0)
        self.storage_list.grid(row=1, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
        populate_list()
        #bind select
        self.storage_list.bind('<<ListboxSelect>>', select_item)


        #warranties
        #standard
        warranty = BooleanVar()
        warranty_label = Label(frame1, text='Standard', font=('bold', 10))
        warranty_label.grid(row=1, column=3, sticky=W)
        warranty_entry = Checkbutton(frame1, variable=warranty, onvalue=True, offvalue=False)
        warranty_entry.grid(row=1, column=4)

        #theftwarranty
        theft_warranty = BooleanVar()
        theft_warranty_label = Label(frame1, text='Theft', font=('bold', 10))
        theft_warranty_label.grid(row=2, column=3, sticky=W)
        theft_warranty_entry = Checkbutton(frame1, variable=theft_warranty, onvalue=True, offvalue=False)
        theft_warranty_entry.grid(row=2, column=4)

        #mechanicalwarranty
        mechanical_warranty = BooleanVar()
        mechanical_warranty_label = Label(frame1, text='Mechanical', font=('bold', 10))
        mechanical_warranty_label.grid(row=3, column=3, sticky=W)
        mechanical_warranty_entry = Checkbutton(frame1, variable=mechanical_warranty, onvalue=True, offvalue=False)
        mechanical_warranty_entry.grid(row=3, column=4)

        #ordering name
        name_text = StringVar()
        name_label = Label(frame1, text='Name', font=('bold', 12))
        name_label.grid(row=12, column=3, sticky=W)
        name_entry = Entry(frame1, textvariable=name_text)
        name_entry.grid(row=12, column=4, sticky=W)


        #buybutton(?)
        buy_btn = Button(frame1, text='Add to order', width=12, command=buy_product)
        buy_btn.grid(row=6, column=3, pady=10)

        #makeorder
        order_btn = Button(frame1, text='Make order', width=12, command=make_order)
        order_btn.grid(row=13, column=3, pady=10)

        #orderlist
        self.order_box = Text(frame1, wrap=WORD, height=8, width=37)
        self.order_box.grid(row=8, column=0, columnspan=3, rowspan=6, pady=20, padx=20)



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
                                    float(price_text.get()),
                                    float(tax_text.get()),
                                    active_field)
            print(f'adding {type(product)} ({product})')
                
            self.storage.add_product(product)
            self.storage_list.delete(0, END)
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
