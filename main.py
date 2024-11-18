from tkinter import *
from tkinter import ttk
from login import *
from billing import *


def main():
    root = Tk()
    app = LoginPage(root) 
    # app = BillingPage(root) #comment afterward
    root.mainloop()

if __name__ == "__main__":
    main()