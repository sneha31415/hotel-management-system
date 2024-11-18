
from tkinter import *
from tkinter import ttk


# --------billing window class-----------
class BillingPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x750+0+0")
        self.root.title("Billing System")

        self.title_label = Label(self.root, text = "Billing System", font = ('Arial', 35, 'bold'), bg = "lightgrey", bd = 8, relief = GROOVE)
        self.title_label.pack(side = TOP, fill = 'x')

        # ---------entry---------
        self.entry_frame = LabelFrame(self.root, text = "Enter Details", bg = "lightgrey", font = ("sans-serif", 20), bd = 7, relief = GROOVE)
        self.entry_frame.place(x = 20, y = 95, width = 500, height = 650)    

        # bill number
        self.bill_no_label = Label(self.entry_frame, text = "Bill Number", font = ('Arial', 15), bg = "lightgrey")
        self.bill_no_label.grid(row = 0, column= 0, padx= 2, pady = 2)

        self.bill_no_entry = Entry(self.entry_frame, bd = 5, textvariable=None, font = ('Arial', 15))
        self.bill_no_entry.grid(row = 0, column= 1, padx=2, pady=2)

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

root = Tk()
app = BillingPage(root) #comment afterward
root.mainloop()