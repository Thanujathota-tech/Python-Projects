from tkinter import *
import math as m
head=Tk()
head.config(bg="skyblue")
head.title("scientific Calculator")
e=Entry(head,width=25,borderwidth=6,relief=RIDGE,fg="black",bg="white",font=("bold"))
e.grid(row=0,column=0,columnspan=5,padx=10,pady=15)
def click(to_print):
    old=e.get()
    e.delete(0,END)
    e.insert(0,old+to_print)
    return
def sc(event):
    key=event.widget
    text=key['text']
    no=e.get()
    result=''
    if text=='deg':
        result=str(m.degrees(float(no)))
    if text=='sin':
        result=str(m.sin(float(no)))
    if text=='cos':
        result=str(m.cos(float(no)))
    if text=='tan':
        result=str(m.tan(float(no)))
    if text=='log':
        result=str(m.log10(float(no)))
    if text=='ln':
        result=str(m.log(float(no)))
    if text=='Sqrt':
        result=str(m.sqrt(float(no)))
    if text=='x!':
        result=str(m.factorial(int(no)))    
    if text=='1/X':
        result=str(1/(float(no)))
    if text=='pi':
        if no=="":
            result=str(m.pi)
        else:
            result=str(float(no)*m.pi)
    if text=='e':
        if no=="":
            result=str(m.e)
        else:
            result=str(m.e**float(no))
    e.delete(0,END)
    e.insert(0,result)
    
def clear():
    e.delete(0,END)
    return
def bksps():
    current=e.get()
    length=len(current)-1
    e.delete(length,END)
def evaluate():
    ans=e.get()
    ans=eval(ans)
    e.delete(0,END)
    e.insert(0,ans)
                
            
lg=Button(head,text="log",padx=28,pady=10,relief=RAISED,bg="lightgreen",fg="black")
lg.bind("<Button-1>",sc)
ln=Button(head,text="ln",padx=28,pady=10,relief=RAISED,bg="lightgreen",fg="black")
ln.bind("<Button-1>",sc)

open=Button(head,text=" (",padx=29,pady=10,relief=RAISED,bg="lightgreen",fg="black",command=lambda:click("("))
close=Button(head,text=" )",padx=29,pady=10,relief=RAISED,bg="lightgreen",fg="black",command=lambda:click(")"))

dot=Button(head,text="  .",padx=29,pady=10,relief=RAISED,bg="lightgreen",fg="black",command=lambda:click("."))
exp=Button(head,text=" ^",padx=30,pady=10,relief=RAISED,bg="orange",fg="white",command=lambda:click("^"))

degb=Button(head,text="deg",padx=23,pady=10,relief=RAISED,bg="orange",fg="white")
degb.bind("<Button-1>",sc)
sinb=Button(head,text="sin",padx=24,pady=10,relief=RAISED,bg="orange",fg="white")
sinb.bind("<Button-1>",sc)
cosb=Button(head,text="cos",padx=24,pady=10,relief=RAISED,bg="orange",fg="white")
cosb.bind("<Button-1>",sc)
tanb=Button(head,text="tan",padx=24,pady=10,relief=RAISED,bg="orange",fg="white")
tanb.bind("<Button-1>",sc)

sqrtm=Button(head,text="Sqrt",padx=23,pady=10,relief=RAISED,bg="blue",fg="white")
sqrtm.bind("<Button-1>",sc)
ac=Button(head,text="C",padx=29,pady=10,relief=RAISED,bg="violet",fg="black",command=lambda:clear())
bksp=Button(head,text="bksp",padx=19,pady=10,relief=RAISED,bg="violet",fg="black",command=bksps)
mod=Button(head,text="mod",padx=19,pady=10,relief=RAISED,bg="violet",fg="black",command=lambda:click("mod"))
div=Button(head,text="/",padx=29,pady=10,relief=RAISED,bg="red",fg="white",command=lambda:click("/"))

fact=Button(head,text="x!",padx=29,pady=10,relief=RAISED,bg="blue",fg="white")
fact.bind("<Button-1>",sc)
seven=Button(head,text="7",padx=30,pady=10,relief=RAISED,bg="yellow",fg="black",command=lambda:click("7"))
eight=Button(head,text="8",padx=29,pady=10,relief=RAISED,bg="yellow",fg="black",command=lambda:click("8"))
nine=Button(head,text="9",padx=29,pady=10,relief=RAISED,bg="yellow",fg="black",command=lambda:click("9"))
mul=Button(head,text="x",padx=29,pady=10,relief=RAISED,bg="red",fg="white",command=lambda:click("*"))

frac=Button(head,text="1/X",padx=25,pady=10,relief=RAISED,bg="blue",fg="white")
frac.bind("<Button-1>",sc)
four=Button(head,text="4",padx=30,pady=10,relief=RAISED,bg="yellow",fg="black",command=lambda:click("4"))
five=Button(head,text="5",padx=29,pady=10,relief=RAISED,bg="yellow",fg="black",command=lambda:click("5"))
six=Button(head,text="6",padx=29,pady=10,relief=RAISED,bg="yellow",fg="black",command=lambda:click("6"))
minus=Button(head,text="-",padx=29,pady=10,relief=RAISED,bg="red",fg="white",command=lambda:click("-"))

pib=Button(head,text="pi",padx=29,pady=10,relief=RAISED,bg="blue",fg="white")
pib.bind("<Button-1>",sc)
one=Button(head,text="1",padx=30,pady=10,relief=RAISED,bg="yellow",fg="black",command=lambda:click("1"))
two=Button(head,text="2",padx=29,pady=10,relief=RAISED,bg="yellow",fg="black",command=lambda:click("2"))
three=Button(head,text="3",padx=29,pady=10,relief=RAISED,bg="yellow",fg="black",command=lambda:click("3"))
add=Button(head,text="+",padx=29,pady=10,relief=RAISED,bg="red",fg="white",command=lambda:click("+"))

e_b=Button(head,text="e",padx=30,pady=10,relief=RAISED,bg="blue",fg="white")
e_b.bind("<Button-1>",sc)
zero=Button(head,text="0",padx=29,pady=10,relief=RAISED,bg="yellow",fg="black",command=lambda:click('0'))
equal=Button(head,text="=",padx=29,pady=10,relief=RAISED,bg="red",fg="white",command=lambda:evaluate())

lg.grid(row=1,column=0)
ln.grid(row=1,column=1)
open.grid(row=1,column=2)
close.grid(row=1,column=3)
dot.grid(row=1,column=4)

exp.grid(row=2,column=0)
degb.grid(row=2,column=1)
sinb.grid(row=2,column=2)
cosb.grid(row=2,column=3)
tanb.grid(row=2,column=4)

sqrtm.grid(row=3,column=0)
ac.grid(row=3,column=1)
bksp.grid(row=3,column=2)
mod.grid(row=3,column=3)
div.grid(row=3,column=4)

fact.grid(row=4,column=0)
seven.grid(row=4,column=1)
eight.grid(row=4,column=2)
nine.grid(row=4,column=3)
mul.grid(row=4,column=4)

frac.grid(row=5,column=0)
four.grid(row=5,column=1)
five.grid(row=5,column=2)
six.grid(row=5,column=3)
minus.grid(row=5,column=4)

pib.grid(row=6,column=0)
one.grid(row=6,column=1)
two.grid(row=6,column=2)
three.grid(row=6,column=3)
add.grid(row=6,column=4)

e_b.grid(row=7,column=1)
zero.grid(row=7,column=2)
equal.grid(row=7,column=3)

head.mainloop()