
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

        self.entry_frame = LabelFrame(self.root, text = "Enter Details", bg = "lightgrey", font = ("sans-serif", 20), bd = 7, relief = GROOVE)
        self.entry_frame.place(x = 20, y = 95, width = 500, height = 650)    