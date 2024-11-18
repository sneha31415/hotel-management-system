
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from datetime import datetime
import sys
from tkinter import ttk

'''
you can keep the buttons for save, add disabled and enable it after generte is clicked 
'''
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

        cust_name =  StringVar()
        cust_contact = StringVar()
        # curr date and time
        date = StringVar()
        now = datetime.now().strftime("%Y-%m-%d  %H:%M")
        date.set(now)

        item = StringVar()
        item_quan = StringVar()
        cost_per_item = StringVar()
        
        total_list = []
        self.grand_total = 0

        # menu
        menu_items = {
            "Idli"      : 30,
            "Medu Vada" : 40,
            "Paratha"   : 50,
            "Dosa"      : 60,
            "Sandwich"  : 45,
            "noodles"   : 50,
            "fried rice" : 50,
            "dal rice"  : 67,
            "chai"      : 15,
            "vada pav"  : 14,
            "samosa"    : 13
    }
        
        
         #--------- functions---------- 
        def default_bill():
            '''
            default text on every bill
            '''
            self.bill_text.insert(END, "\t\t\t      VJTI Canteen")
            self.bill_text.insert(END, "\n\t\t    near Quanrangle, VJTI, Matunga E")
            self.bill_text.insert(END, "\n\t\t        Contact - +21 2100080914")
            self.bill_text.insert(END, "\n======================================================================")
            self.bill_text.insert(END, f"\nBill Number {bill_no_tk.get()}")


        def generate_bill():
            if cust_name.get()== "" :
                messagebox.showerror("customer name cannot be empty!")
            else:
                self.bill_text.delete(6.0, END)
                self.bill_text.insert(END, f"\nCustomer Name {cust_name.get()}")
                self.bill_text.insert(END, f"\nCustomer Contact {cust_contact.get()}")
                self.bill_text.insert(END, f"\nDate {date.get()}")
                self.bill_text.insert(END, "\n======================================================================")
                self.bill_text.insert(END, "\nProduct Name\t\t        Quantity\t\t   cost per item\t\t   total cost ")
                self.bill_text.insert(END, "\n======================================================================")


        def clear():
            '''
            clears all info except date,  and bill from the form
            '''
            total_list = []
            cust_name.set("")
            cust_contact.set("")
            item.set("")
            item_quan.set("")
            cost_per_item.set("")

        def reset():
            '''
            resets the entire bill
            '''
            total_list = []
            self.bill_text.delete("1.0", END)
            default_bill()

        def add_func():
            item_quantity = int(item_quan.get())
            coi = int(cost_per_item.get())
            total = item_quantity * coi

            total_list.append(total)
            self.bill_text.insert(END, f"\n{item.get()}\t\t        {item_quantity}\t\t       {coi}\t\t          {total}")


        def grand_total():
            '''
            global grand total
            '''
            for item in total_list:
                self.grand_total +=  item

            self.bill_text.insert(END, "\n======================================================================")
            self.bill_text.insert(END, f"\n\t\t\t\t\t\t    Grand total : {self.grand_total}")
            self.bill_text.insert(END, "\n======================================================================")

        def save_func():
            user_choice = messagebox.askyesno("Confirm", f"Do you want to save the bill {bill_no_tk.get()}", parent = self.root )
            if (user_choice > 0):
                self.bill_content = self.bill_text.get("1.0", END)
                try:
                    con = open(f"{sys.path[0]}/bills/" + str(bill_no_tk.get()) + ".txt", "w")
                except Exception as e:
                    messagebox.showerror("error!", f"error due to {e}", parent = self.root)
                con.write(self.bill_content)
                con.close()
                messagebox.showinfo("success!", f" bill {bill_no_tk.get()} has been saved successfully!", parent = self.root)
            else:
                return
            
        def update_price(event):
            selected_item = item.get()
            if selected_item in menu_items:
                cost_per_item.set(menu_items[selected_item])  # Set the price for the selected item
            else:
                cost_per_item.set("")  # Clear the price if the selection is invalid



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

        self.name_entry = Entry(self.entry_frame, bd = 5, textvariable=cust_name, font = ('Arial', 15))
        self.name_entry.grid(row = 1, column= 1, padx=2, pady=2)

        # contact number
        self.contact_label = Label(self.entry_frame, text = "contact Number", font = ('Arial', 15), bg = "lightgrey")
        self.contact_label.grid(row = 2, column= 0, padx= 2, pady = 2)

        self.contact_entry = Entry(self.entry_frame, bd = 5, textvariable=cust_contact, font = ('Arial', 15))
        self.contact_entry.grid(row = 2, column= 1, padx=2, pady=2)

        # date 
        self.date_label = Label(self.entry_frame, text = "Date", font = ('Arial', 15), bg = "lightgrey")
        self.date_label.grid(row = 3, column= 0, padx= 2, pady = 2)

        self.date_entry = Entry(self.entry_frame, bd = 5, textvariable=date, font = ('Arial', 15))
        self.date_entry.grid(row = 3, column= 1, padx=2, pady=2)
        self.date_entry.config(state = "disabled")

        # item purchased
        self.item_lable = Label(self.entry_frame, text = "Item purchased", font = ('Arial', 15), bg = "lightgrey")
        self.item_lable.grid(row = 4, column= 0, padx= 2, pady = 2)

        # self.item_entry = Entry(self.entry_frame, bd = 5, textvariable=item, font = ('Arial', 15))
        # self.item_entry.grid(row = 4, column= 1, padx=2, pady=2)
        # ADDING A DROPDOWN ENTRY
        self.item_combobox = ttk.Combobox(self.entry_frame, values=list(menu_items.keys()), textvariable=item, font=('Arial', 15), state="readonly")
        self.item_combobox.grid(row=4, column=1, padx=2, pady=2)
        self.item_combobox.bind("<<ComboboxSelected>>", update_price)

        # item quantity purchased
        self.item_quantity_lable = Label(self.entry_frame, text = "Item quantity", font = ('Arial', 15), bg = "lightgrey")
        self.item_quantity_lable.grid(row = 5, column= 0, padx= 2, pady = 2)

        self.item_quantity_entry = Entry(self.entry_frame, bd = 5, textvariable=item_quan, font = ('Arial', 15))
        self.item_quantity_entry.grid(row = 5, column= 1, padx=2, pady=2)

        # cost of one item 
        self.item_cost_lable = Label(self.entry_frame, text = "cost of one", font = ('Arial', 15), bg = "lightgrey")
        self.item_cost_lable.grid(row = 6, column= 0, padx= 2, pady = 2)

        self.item_cost_entry = Entry(self.entry_frame, bd = 5, textvariable=cost_per_item, font = ('Arial', 15))
        self.item_cost_entry.grid(row = 6, column= 1, padx=2, pady=2)


       
        # -----------buttons----------------
        self.button_frame = LabelFrame(self.entry_frame, text = "options",  bd = 5, bg = "lightgrey", font = ("Arial", 15))
        self.button_frame.place(x = 10, y = 300, width = 400, height = 220)

        self.add_btn = Button(self.button_frame, bd = 5, text = "Add", font = ("Arial", 12), width = 12, height=3, command = add_func)
        self.add_btn.grid(row = 0, column= 0, padx=4, pady=2)

        self.generate_btn = Button(self.button_frame, bd = 5, text = "Generate", font = ("Arial", 12), width = 12, height=3, command=generate_bill)
        self.generate_btn.grid(row = 0, column= 1, padx=4, pady=2)

        self.clear_btn = Button(self.button_frame, bd = 5, text = "Clear", font = ("Arial", 12), width = 12, height=3, command = clear)
        self.clear_btn.grid(row = 0, column= 2, padx=4, pady=2)

        self.total_btn = Button(self.button_frame, bd = 5, text = "Total", font = ("Arial", 12), width = 12, height=3, command = grand_total)
        self.total_btn.grid(row = 1, column= 0, padx=4, pady=2)

        self.reset_btn = Button(self.button_frame, bd = 5, text = "Reset", font = ("Arial", 12), width = 12, height=3, command = reset)
        self.reset_btn.grid(row = 1, column= 1, padx=4, pady=2)

        self.save_btn = Button(self.button_frame, bd = 5, text = "Save", font = ("Arial", 12), width = 12, height=3, command=save_func)
        self.save_btn.grid(row = 1, column= 2, padx=4, pady=2)

        # bill frame
        self.bill_frame = LabelFrame(self.root, text = "Bill", bd = 7, bg = "lightgrey", font = ("sans-serif", 22), relief=GROOVE)
        self.bill_frame.place(x = 700, y = 95, width = 600, height = 600)

        # scroll bar for bill
        self.y_scroll = Scrollbar(self.bill_frame, orient="vertical")
        # text in bill
        self.bill_text = Text(self.bill_frame, bg="white", yscrollcommand=self.y_scroll.set)
        self.y_scroll.config(command = self.bill_text.yview)
        # pack the scroll before the text
        self.y_scroll.pack(side = RIGHT, fill = Y)
        self.bill_text.pack(fill = BOTH, expand=TRUE)

        default_bill()


root = Tk()
app = BillingPage(root) #comment afterward
root.mainloop()