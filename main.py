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

        self.main_frame = Frame(self.root, bg = "lightgrey", bd = 6, relief=GROOVE)
        self.main_frame.place(x = 280, y = 150, width = 800, height = 450)

        self.login_label = Label(self.main_frame, text = "Login", bd = 6, relief=GROOVE, anchor = CENTER, bg = "lightgrey", font = ("sans-serif", 25, "bold"))
        self.login_label.pack(side = TOP, fill = "x")

        self.entry_frame = LabelFrame(self.main_frame, text = "Enter Details", bd = 6, relief=GROOVE, bg = "lightgrey", font = ("sans-serif", 18))
        self.entry_frame.pack(fill = BOTH, expand=TRUE)


        self.user_label = Label(self.entry_frame, text = "Enter username : ", bg = "lightgrey", font = ("sans-serif", 15))
        self.user_label.grid(row = 0, column = 0, padx = 2, pady = 2)

        # ----------variables----------
        self.user_entry = Entry(self.entry_frame, font = ("sans-serif", 15))
        self.user_entry.grid(row = 0, column=1, padx=2,pady = 2)

if __name__ == "__main__":
    main()