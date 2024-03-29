from tkinter import *
from functools import partial
root=Tk()
root.title('Registration form')
root.configure(bg="pink")
root.geometry('580x725')
frame=Frame(root,bg="pink")
def button(name,number,mail,branch):
    print("New Registration recorded")
    print("Student name:",name.get())
    print("Student ID:",number.get())
    print("Student MailID:",mail.get())
    print("Branch:",branch.get())
    
head=Label(frame,text="Student Registration",bg="pink",fg="purple",font=("times new roman",22,"bold"))
head.grid(row=0,columnspan=3,pady=30)

s_n=Label(frame,text="Student Name :",bg="pink",fg="black",font=("times new roman",15,"bold"))
s_n.grid(pady=20)
name=StringVar()
n_e=Entry(frame,textvariable=name,width=30)
n_e.grid(row=1,column=1,pady=15)

s_id=Label(frame,text="Student ID :",bg="pink",fg="black",font=("times new roman",15,"bold"))
s_id.grid()
number=StringVar()
id_e=Entry(frame,textvariable=number,width=30)
id_e.grid(row=2,column=1,pady=15)

gender=Label(frame,text="Gender :",bg="pink",fg="black",font=("times new roman",15,"bold"))
gender.grid(row=3,column=0,pady=15)

radio=IntVar()
R1 = Radiobutton(frame,text="male",variable=radio,value=1,bg="pink",fg="purple",font=("times new roman",14,"bold"))  
R1.grid(row=3,column=1)  
R2 = Radiobutton(frame,text="female",variable=radio,value=2,bg="pink",fg="purple",font=("times new roman",14,"bold"))  
R2.grid(row=4,column=1)  

Mail=Label(frame,text="Mail-ID :",bg="pink",fg="black",font=("times new roman",15,"bold"))
Mail.grid()
mail=StringVar()
m_e=Entry(frame,textvariable=mail,width=30)
m_e.grid(row=5,column=1,pady=20)

Branch=Label(frame,text="Branch :",bg="pink",fg="black",font=("times new roman",15,"bold"))
Branch.grid()
branch=StringVar()
b_e=Entry(frame,textvariable=branch,width=30)
b_e.grid(row=6,column=1,pady=15)

college=Label(frame,text="College",bg="pink",fg="black",font=("times new roman",15,"bold"))
college.grid(row=7,column=0,pady=20)
menu= StringVar()
menu.set("Select College")
drop= OptionMenu(frame, menu,"Narasaraopeta Engineering College","Tirumala Engineering College", "Sai Tirumala NVR eng ",
                 "Eswar Engineering College","Chalapathi Engineering College","Narasaraopet Institute of Technology","Krishnaveni Engineering College")
drop.grid(row=7,column=1)
course=Label(frame,text="Course :",bg="pink",fg="black",font=("times new roman",15,"bold"))
course.grid(row=8,column=0,pady=15)
cb1=IntVar()
cb2=IntVar()
cb3=IntVar()
cb4=IntVar()
cb5=IntVar()
cb6=IntVar()
ck1=Checkbutton(frame,text="c",variable=cb1,onvalue=1,offvalue=0,height=1,width=5,bg="pink",fg="purple",font=("times new roman",13,"bold"))
ck2=Checkbutton(frame,text="c++",variable=cb2,onvalue=1,offvalue=0,height=1,width=5,bg="pink",fg="purple",font=("times new roman",13,"bold"))
ck3=Checkbutton(frame,text="python",variable=cb3,onvalue=1,offvalue=0,height=1,width=13,bg="pink",fg="purple",font=("times new roman",13,"bold"))
ck4=Checkbutton(frame,text="java",variable=cb4,onvalue=1,offvalue=0,height=1,width=10,bg="pink",fg="purple",font=("times new roman",13,"bold"))
ck5=Checkbutton(frame,text="javascript",variable=cb5,onvalue=1,offvalue=0,height=1,width=9,bg="pink",fg="purple",font=("times new roman",13,"bold"))
ck6=Checkbutton(frame,text="nodejs",variable=cb6,onvalue=1,offvalue=0,height=1,width=12,bg="pink",fg="purple",font=("times new roman",13,"bold"))
ck1.grid(row=9,column=0)
ck2.grid(row=9,column=1)
ck3.grid(row=10,column=0)
ck4.grid(row=10,column=1)
ck5.grid(row=11,column=0)
ck6.grid(row=11,column=1)

button=partial(button,name,number,mail,branch)
button=Button(frame,text="Submit",bg="skyblue",fg="black",font=("times new roman",14,"bold"),command=button)
button.grid(row=15,column=0,columnspan=3,pady=35)
frame.pack()
root.mainloop()
