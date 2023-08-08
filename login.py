from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import sqlite3
import os
root=Tk()
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login system")
        self.root.geometry("1350x700+0+30")
        self.root.config(bg="white")

        self.var_username = StringVar()
        self.var_password = StringVar()

        self.photo = ImageTk.PhotoImage(Image.open("C:/Users/user/Downloads/login1.png"))  # create a label to show image in window
        label = Label(self.root, image=self.photo,bg="white").place(x=120, y=0,width=500, relheight=1)

        frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        frame.place(x=650,y=90,width=400,height=500)


        title=Label(frame,text="Login ",font=("times new roman",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)

        #============label====================
        username = Label(frame, text="Username", font=("Andalus", 15, "bold"), bg="white", fg="#767171").place(x=60, y=100)
        passwrd = Label(frame, text="Password", font=("Andalus", 15, "bold"), bg="white", fg="#767171").place(x=60, y=200)

        #==============text variable===============

        self.username1 = Entry(frame,textvariable= self.var_username,font=("times new roman", 20), bg="#ECECEC")
        self.username1.place(x=60, y=140)
        self.passwrd1 = Entry(frame,textvariable=self.var_password,font=("times new roman", 20), bg="#ECECEC")
        self.passwrd1.place(x=60, y=240)

        log=Button(frame,text="Sign In",font=("Arial Rounded MT Bold",15),bg="#5DADE2",bd=0,fg="white",cursor="hand2",command=self.login).place(x=60,y=310,width=280,height=40)

        oor=Label(frame,text="OR",font=("times new roman",15),fg="#767171",bg="white").place(x=180,y=365)

        forget=Button(frame,text="Forget Password?",font=("times new roman",13),bg="white",fg="#00759E",bd=0).place(x=135,y=400)

        sign = Label(frame, text="Don't have an account?", font=("Andalus", 10, "bold"), bg="white", fg="#767171").place(x=100, y=440)
        signup=Button(frame,text="Sign up",font=("Andalu",10,"bold"),bg="white",fg="#00759E",bd=0,command=self.reg_win).place(x=255,y=440)



    def reg_win(self):
        self.root.destroy()
        import register


    def login(self):

        if self.var_username.get() =="" or self.var_password.get()=="":
            messagebox.showerror("Error","Username and password required",parent=self.root )
        else:
            try:
                con = sqlite3.connect(database="mac.db")
                cur = con.cursor()
                cur.execute("select * from employe where email=? and password=?",(self.var_username.get(),self.var_password.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid Username and Password", parent=self.root)

                else:
                    messagebox.showinfo("Success","Welcome",parent=self.root)
                    self.root.destroy()
                    os.system("python dash.py")
                    con.close()
            except Exception as es:
                messagebox.showerror("Error", f"error due to:{str(es)}", parent=self.root)



obj=Login(root)
root.mainloop()