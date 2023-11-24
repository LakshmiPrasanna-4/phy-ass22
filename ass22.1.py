# Write a program to prepare an applicate to subtract two numbers using tkinter.

def mysub():
    a=int(num1.get())
    b=int(num2.get())
    s=a-b
    res="result:"+str(s)
    l3.config(text=s)
from tkinter import *
subtract=Tk()
subtract.title("Subtract two numbers")
l1=Label(subtract,text="Enter first number")
num1=Entry(subtract)
l2=Label(subtract,text="Enter second number")
num2=Entry(subtract)
b=Button(subtract,text="Subtract",command=mysub)
l3=Label(subtract,text="Result:")
l1.grid(row=0,column=0)
num1.grid(row=0,column=1)
l2.grid(row=1,column=0)
num2.grid(row=1,column=1)
b.grid(row=2,column=0)
l3.grid(row=2,column=1)
subtract.mainloop()
