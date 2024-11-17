from tkinter import *
from tkinter import ttk

def main():
    root = Tk()
    app = LoginPage(root)
    root.mainloop()

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x750+0+0")
        self.root.title("Hotel Management System")

        self.title_label = Label(self.root, text = "Hotel Management System", font = ('Arial', 35, 'bold'), bg = "lightgrey", bd = 8, relief = GROOVE)
        self.title_label.pack(side = TOP, fill = 'x')



if __name__ == "__main__":
    main()