from tkinter import *
from tkinter import messagebox
from functools import partial
window=Tk()
window.title("Login form")
window.geometry("340x300")
window.configure(bg="blue4")
def login(Username,password):
    print('login entry recorded')
    print("username entered:",Username.get())
    print("username entered:",password.get())
    return
frame=Frame(bg="blue4")

login_label=Label(frame,text="Login",bg="blue4",fg="white",font=("times new roman",30))
login_label.grid(row=0,column=0,columnspan=2,pady=20)

user_name=Label(frame,text="Username:",bg="blue4",fg="lavenderblush",font=("times new roman",16,"bold"))
Username=StringVar()
user_name.grid(row=1,column=0,pady=5)

user_entry=Entry(frame,textvariable=Username)
user_entry.grid(row=1,column=1)

password_label=Label(frame,text="Password:",bg="blue4",fg='lavenderblush',font=("times new roman",16,"bold"))
password=StringVar()
password_label.grid(row=2,column=0,pady=10)

password_entry=Entry(frame,textvariable=password,show="*")
password_entry.grid(row=2,column=1)

login=partial(login,Username,password)

login_button=Button(frame,text="Login",bg="paleturquoise",fg="midnightblue",font=("times new roman",11,"bold"),command=login)
login_button.grid(row=3,column=0,columnspan=3,pady=20)

frame.pack()
window.mainloop()