
from tkinter import *
from tkinter import ttk
import random

# --------billing window class-----------
class BillingPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x750+0+0")
        self.root.title("Billing System")

        self.title_label = Label(self.root, text = "Billing System", font = ('Arial', 35, 'bold'), bg = "lightgrey", bd = 8, relief = GROOVE)
        self.title_label.pack(side = TOP, fill = 'x')

        # --------variables--------
        bill_no_tk = IntVar()
        bill_no_tk.set(random.randint(10000, 99999))

        # ---------entry---------
        self.entry_frame = LabelFrame(self.root, text = "Enter Details", bg = "lightgrey", font = ("sans-serif", 20), bd = 7, relief = GROOVE)
        self.entry_frame.place(x = 120, y = 95, width = 500, height = 600)    

        # bill number
        self.bill_no_label = Label(self.entry_frame, text = "Bill Number", font = ('Arial', 15), bg = "lightgrey")
        self.bill_no_label.grid(row = 0, column= 0, padx= 2, pady = 2)

        self.bill_no_entry = Entry(self.entry_frame, bd = 5, textvariable=bill_no_tk, font = ('Arial', 15))
        self.bill_no_entry.grid(row = 0, column= 1, padx=2, pady=2)
        self.bill_no_entry.config(state = "disabled")

        # customer name
        self.name_label = Label(self.entry_frame, text = "customer Name", font = ('Arial', 15), bg = "lightgrey")
        self.name_label.grid(row = 1, column= 0, padx= 2, pady = 2)

        self.name_entry = Entry(self.entry_frame, bd = 5, textvariable=None, font = ('Arial', 15))
        self.name_entry.grid(row = 1, column= 1, padx=2, pady=2)

        # contact number
        self.contact_label = Label(self.entry_frame, text = "contact Number", font = ('Arial', 15), bg = "lightgrey")
        self.contact_label.grid(row = 2, column= 0, padx= 2, pady = 2)

        self.contact_entry = Entry(self.entry_frame, bd = 5, textvariable=None, font = ('Arial', 15))
        self.contact_entry.grid(row = 2, column= 1, padx=2, pady=2)

        # date 
        self.date_label = Label(self.entry_frame, text = "Date", font = ('Arial', 15), bg = "lightgrey")
        self.date_label.grid(row = 3, column= 0, padx= 2, pady = 2)

        self.date_entry = Entry(self.entry_frame, bd = 5, textvariable=None, font = ('Arial', 15))
        self.date_entry.grid(row = 3, column= 1, padx=2, pady=2)

        # item purchased
        self.item_lable = Label(self.entry_frame, text = "Item purchased", font = ('Arial', 15), bg = "lightgrey")
        self.item_lable.grid(row = 4, column= 0, padx= 2, pady = 2)

        self.item_entry = Entry(self.entry_frame, bd = 5, textvariable=None, font = ('Arial', 15))
        self.item_entry.grid(row = 4, column= 1, padx=2, pady=2)

        # item quantity purchased
        self.item_quantity_lable = Label(self.entry_frame, text = "Item quantity", font = ('Arial', 15), bg = "lightgrey")
        self.item_quantity_lable.grid(row = 5, column= 0, padx= 2, pady = 2)

        self.item_quantity_entry = Entry(self.entry_frame, bd = 5, textvariable=None, font = ('Arial', 15))
        self.item_quantity_entry.grid(row = 5, column= 1, padx=2, pady=2)

        # item quantity purchased
        self.item_cost_lable = Label(self.entry_frame, text = "cost of one", font = ('Arial', 15), bg = "lightgrey")
        self.item_cost_lable.grid(row = 6, column= 0, padx= 2, pady = 2)

        self.item_cost_entry = Entry(self.entry_frame, bd = 5, textvariable=None, font = ('Arial', 15))
        self.item_cost_entry.grid(row = 6, column= 1, padx=2, pady=2)


        # -----------buttons----------------
        self.button_frame = LabelFrame(self.entry_frame, text = "options",  bd = 5, bg = "lightgrey", font = ("Arial", 15))
        self.button_frame.place(x = 10, y = 300, width = 400, height = 220)

        self.add_btn = Button(self.button_frame, bd = 5, text = "Add", font = ("Arial", 12), width = 12, height=3)
        self.add_btn.grid(row = 0, column= 0, padx=4, pady=2)

        self.generate_btn = Button(self.button_frame, bd = 5, text = "Generate", font = ("Arial", 12), width = 12, height=3)
        self.generate_btn.grid(row = 0, column= 1, padx=4, pady=2)

        self.clear_btn = Button(self.button_frame, bd = 5, text = "Clear", font = ("Arial", 12), width = 12, height=3)
        self.clear_btn.grid(row = 0, column= 2, padx=4, pady=2)

        self.total_btn = Button(self.button_frame, bd = 5, text = "Total", font = ("Arial", 12), width = 12, height=3)
        self.total_btn.grid(row = 1, column= 0, padx=4, pady=2)

        self.reset_btn = Button(self.button_frame, bd = 5, text = "Reset", font = ("Arial", 12), width = 12, height=3)
        self.reset_btn.grid(row = 1, column= 1, padx=4, pady=2)

        self.save_btn = Button(self.button_frame, bd = 5, text = "Save", font = ("Arial", 12), width = 12, height=3)
        self.save_btn.grid(row = 1, column= 2, padx=4, pady=2)

        # bill frame
        self.bill_frame = LabelFrame(self.root, text = "Bill", bd = 7, bg = "lightgrey", font = ("sans-serif", 22), relief=GROOVE)
        self.bill_frame.place(x = 700, y = 95, width = 500, height = 600)

        # scroll bar for bill
        self.y_scroll = Scrollbar(self.bill_frame, orient="vertical")
        # text in bill
        self.bill_text = Text(self.bill_frame, bg="white", yscrollcommand=self.y_scroll.set)
        self.y_scroll.config(command = self.bill_text.yview)
        # pack the scroll before the text
        self.y_scroll.pack(side = RIGHT, fill = Y)
        self.bill_text.pack(fill = BOTH, expand=TRUE)

root = Tk()
app = BillingPage(root) #comment afterward
root.mainloop()