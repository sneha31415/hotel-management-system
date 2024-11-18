from tkinter import *
from tkinter import ttk
from billing import *

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x750+0+0")
        self.root.title("Hotel Management System")

        self.title_label = Label(self.root, text = "Hotel Management System", font = ('Arial', 35, 'bold'), bg = "lightgrey", bd = 8, relief = GROOVE)
        self.title_label.pack(side = TOP, fill = 'x')

        self.main_frame = Frame(self.root, bg = "lightgrey", bd = 6, relief=GROOVE)
        self.main_frame.place(x = 280, y = 150, width = 800, height = 450)

        self.login_label = Label(self.main_frame, text = "Login", bd = 6, relief=GROOVE, anchor = CENTER, bg = "lightgrey", font = ("sans-serif", 25, "bold"))
        self.login_label.pack(side = TOP, fill = "x")

        self.entry_frame = LabelFrame(self.main_frame, text = "Enter Details", bd = 6, relief=GROOVE, bg = "lightgrey", font = ("sans-serif", 18))
        self.entry_frame.pack(fill = BOTH, expand=TRUE)
        
        # ---------variables for username and pwd--------
        username = StringVar()
        password = StringVar()

        # ----------username----------
        self.user_label = Label(self.entry_frame, text = "Enter username : ", bg = "lightgrey", font = ("sans-serif", 15))
        self.user_label.grid(row = 0, column = 0, padx = 2, pady = 2)

        self.user_entry = Entry(self.entry_frame, font = ("sans-serif", 15), bd = 3, textvariable=username)
        self.user_entry.grid(row = 0, column=1, padx=2,pady = 2)

        # ---------password----------
        self.password_label = Label(self.entry_frame, text = "Enter password : ", bg = "lightgrey", font = ("sans-serif", 15))
        self.password_label.grid(row = 1, column = 0, padx = 2, pady = 2)

        self.password_entry = Entry(self.entry_frame, font = ("sans-serif", 15), bd = 3, textvariable=password, show = '*')
        self.password_entry.grid(row = 1, column=1, padx=2,pady = 2)


        # --------functions ------------
        def check_login():
            '''
            this will check 
            '''
            if username.get() == "" and password.get() == "":
                self.billing_btn.config(state = "normal")
            else:
                pass #-> message box
        
        def reset():
            '''
            clears the username and password
            '''
            username.set("")
            password.set("")

        def billing_sect():
            '''
            open a billing window on login
            '''
            self.new_window = Toplevel(self.root)
            self.app = BillingPage(self.new_window)
    

        # ---------buttons----------
        self.button_frame = LabelFrame(self.entry_frame, text = "Options", font = ("Arial", 15), bg = "lightgrey", bd = 7, relief = GROOVE)
        self.button_frame.place(x = 20, y = 100, width = 730, height = 90)
        
        self.login_btn = Button(self.button_frame, text = "Login", font = ("Arial", 15), bd = 5, width = 15, command=check_login)
        self.login_btn.grid(row = 0, column= 0, padx =20, pady=2)

        self.billing_btn = Button(self.button_frame, text = "Billing", font = ("Arial", 15), bd = 5, width = 15, pady=2, command = billing_sect)
        self.billing_btn.grid(row = 0, column= 1, padx =20)
        # bydefault billing is disabled
        self.billing_btn.config(state = "disabled")
        
        self.reset_btn = Button(self.button_frame, text = "Reset", font = ("Arial", 15), bd = 5, width = 15, command=reset)
        self.reset_btn.grid(row = 0, column= 2, padx =20, pady=2)
