from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk, messagebox

class dash:
    def __init__(self,root):
        self.root=root
        self.root.title("Infotrix")
        self.root.geometry("1560x700+0+0")
        self.root.config(bg="white")

        title = Label(self.root, text="Welcome Mousmi Uikey", padx=10, compound=LEFT, font=("goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1,height=50)



root = Tk()
obj=dash(root)
root.mainloop()