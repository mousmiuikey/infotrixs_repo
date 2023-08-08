from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import sqlite3
import os

root=Tk()
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.photo = ImageTk.PhotoImage(Image.open("C:/Users/user/Downloads/blur1.jpg"))  # create a label to show image in window
        label = Label(self.root, image=self.photo).place(x=500, y=0,width=1500, relheight=1)

        self.photo1 = ImageTk.PhotoImage(Image.open("C:/Users/user/Downloads/sign.jpg"))  # create a label to show image in window
        label1 = Label(self.root, image=self.photo1).place(x=0, y=50, width=500, height=750)

        frame=Frame(self.root,bg="white")
        frame.place(x=500,y=120,width=700,height=500)

        self.var_name = StringVar()
        self.var_lastname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_que = StringVar()
        self.var_ans = StringVar()
        self.var_paswd = StringVar()
        self.var_conpaswd = StringVar()

        #==============title=================
        title=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)

        #================widget================

        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=90)
        lname = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=90)
        contact = Label(frame, text="Contact.No", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=160)
        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=160)
        que = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=230)
        ans = Label(frame, text=" Answer", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=230)
        paswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=300)
        conpaswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=300)


    #==============text variable===============

        self.fname1=Entry(frame,textvariable=self.var_name,font=("times new roman",15),bg="light grey")
        self.fname1.place(x=50,y=120,width=250)
        self.lname1 = Entry(frame,textvariable=self.var_lastname, font=("times new roman", 15), bg="light grey")
        self.lname1.place(x=370, y=120, width=250)
        self.contact1 = Entry(frame,textvariable=self.var_contact, font=("times new roman", 15), bg="light grey")
        self.contact1.place(x=50, y=190, width=250)
        self.email1 = Entry(frame, textvariable=self.var_email,font=("times new roman", 15), bg="light grey")
        self.email1.place(x=370, y=190, width=250)
        self.que1 = ttk.Combobox(frame,textvariable=self.var_que,font=("times new roman", 15),state="readonly",justify=CENTER)
        self.que1['values']=("select","Your Pet Name","Your Birth Place","Your Best Friend Name")
        self.que1.place(x=50, y=260, width=250)
        self.que1.current(0)
        self.ans1 = Entry(frame,textvariable=self.var_ans, font=("times new roman", 15), bg="light grey")
        self.ans1.place(x=370, y=260, width=250)
        self.paswd1 = Entry(frame,textvariable=self.var_paswd, font=("times new roman", 15), bg="light grey")
        self.paswd1.place(x=50, y=330, width=250)
        self.conpaswd1 = Entry(frame,textvariable=self.var_conpaswd, font=("times new roman", 15), bg="light grey")
        self.conpaswd1.place(x=370, y=330, width=250)

        #===========checkbox=================

        self.var_check=IntVar()
        self.chk=Checkbutton(frame,text="I Agree Terms and Conditions",variable=self.var_check,onvalue=1,offvalue=0).place(x=50,y=370)

        #self.img=ImageTk.PhotoImage(Image.open("C:/Users/user/Downloads/now.jpg"))
        #self.lbl=Button(Label(frame,image=self.img,bg="white").place(x=200,y=380,width=220,height=100))

        self.btn=Button(frame,text="Register Now ",font=("Calibri",15,"bold"),bg="green",fg="white",bd=0,command=self.register)
        self.btn.place(x=50,y=410,width=220,height=40)

        sign=Button(self.root,text="SIGN IN",font=("Calibri",15,"bold"),bg="#F75D59",fg="white",bd=0,command=self.sign_win).place(x=230,y=518,width=100,height=28)


    def sign_win(self):
        self.root.destroy()
        os.system("python login.py")


    def register(self):
        con = sqlite3.connect("mac.db")
        cur = con.cursor()
        if self.var_name.get()=="" or  self.var_lastname.get()=="" or self.var_contact.get()=="" or self.var_email.get()=="" or self.var_que.get()=="" or self.var_ans.get()=="" or self.var_paswd.get()=="" or self.var_conpaswd.get()=="":
               messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_paswd.get()!=self.var_conpaswd.get()=="":
            messagebox.showerror("Error","Password and Confirm password should be same",parent=self.root)

        elif self.var_check.get()==0:
            messagebox.showerror("Success", "Please Agree our Terms and Conditions", parent=self.root)

        else:
            try:
                con = sqlite3.connect("mac.db")
                cur = con.cursor()
                cur.execute("select * from employe where email=?",(self.var_email.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already Exist",parent=self.root)
                else:
                    cur.execute("insert into employe(fname,lname,contact,email,question,answer,password) values(?,?,?,?,?,?,?)",(
                        self.var_name.get(),
                        self.var_lastname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_que.get(),
                        self.var_ans.get(),
                        self.var_paswd.get()
                    ))
                    con=con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Register Successfully", parent=self.root)
                    self.clear()
                    self.sign_win()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}")

    def clear(self):
        self.var_name.delete(0,END)
        self.var_lastname.delete(0, END)
        self.var_contact.delete(0, END)
        self.var_email.delete(0, END)
        self.var_ans.delete(0, END)
        self.var_paswd.delete(0, END)
        self.var_conpaswd.delete(0, END)
        self.var_que.current(0)


obj=Register(root)
root.mainloop()