# Write a program to prepare overall grade application based on 6 semesters.

def myresult():
    s1=float(sem1points.get())
    s2=float(sem2points.get())
    s3=float(sem3points.get())
    s4=float(sem4points.get())
    s5=float(sem5points.get())
    s6=float(sem6points.get())
    cgpa=(s1+s2+s3+s4+s5+s6)/6
    if cgpa>=10:
        gr="O"
    elif cgpa>=9:
        gr="A+"
    elif cgpa>=8:
        gr="A"
    elif cgpa>=7:
        gr="B"
    elif cgpa>=6:
        gr="C"
    elif cgpa>=5:
        gr="D"
    elif cgpa>4:
        gr="P"
    else:
        gr="F"
    s="cgpa:"+str(cgpa)+"Grade:"+gr
    res.config(text=s)
from tkinter import *
result=Tk()
result.title("Student Result")
sem1=Label(result,text="Enter semester1 points:")
sem1points=Entry(result)
sem2=Label(result,text="Enter semester2 points:")
sem2points=Entry(result)
sem3=Label(result,text="Enter semester3 points:")
sem3points=Entry(result)
sem4=Label(result,text="Enter semester4 points:")
sem4points=Entry(result)
sem5=Label(result,text="Enter semester5 points:")
sem5points=Entry(result)
sem6=Label(result,text="Enter semester6 points:")
sem6points=Entry(result)
b1=Button(result,text="Submit",command=myresult)
res=Label(result,text="?") 
sem1.grid(row=0,column=0)
sem1points.grid(row=0,column=1)

sem2.grid(row=1,column=0)
sem2points.grid(row=1,column=1)

sem3.grid(row=2,column=0)
sem3points.grid(row=2,column=1)

sem4.grid(row=3,column=0)
sem4points.grid(row=3,column=1)

sem5.grid(row=4,column=0)
sem5points.grid(row=4,column=1)

sem6.grid(row=5,column=0)
sem6points.grid(row=5,column=1)

b1.grid(row=6,column=0)
res.grid(row=6,column=1)



result.mainloop()

    
    
    
