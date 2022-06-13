
import tkinter as tk
from tkinter import scrolledtext as st
from tkinter import messagebox as msg
import math



def Btn20Click():
    a=eval(txt2.get())
    txt1.insert(tk.END,"{0}+".format(a))
    txt2.delete(0,tk.END)
def Btn16Click():
    a=eval(txt2.get())
    txt1.insert(tk.END,"{0}-".format(a))
    txt2.delete(0,tk.END)
def Btn12Click():
    a=eval(txt2.get())
    txt1.insert(tk.END,"{0}*".format(a))
    txt2.delete(0,tk.END)
def Btn8Click():
    a=eval(txt2.get())
    txt1.insert(tk.END,"{0}/".format(a))
    txt2.delete(0,tk.END)
def Btn23Click():
    a=eval(txt2.get())
    txt2.insert(tk.END,".".format(a))
def Btn21Click():
    a=eval(txt2.get())
    txt2.delete(0,tk.END)
    txt2.insert(tk.END,"-{0}".format(a))
    
    
def Btn3Click():
    txt1.delete(0,tk.END)
    txt2.delete(0,tk.END)
def Btn2Click():
    txt2.delete(0,tk.END) 


def Btn5Click():
    a=eval(txt2.get())
    txt2.delete(0,tk.END)
    txt2.insert(tk.END,"1/{0}".format(a))
def Btn6Click():
    a=eval(txt2.get())
    txt2.delete(0,tk.END)
    txt2.insert(tk.END,"{0}**2".format(a))
def Btn1Click():
    a=eval(txt2.get())
    txt2.delete(0,tk.END)
    txt2.insert(tk.END,"{0}/100".format(a))
def Btn7Click():
    a=eval(txt2.get())
    txt2.delete(0,tk.END)
    txt2.insert(tk.END,'{0}**(1/2)'.format(a))
    

def Btn24Click():
    b=eval(txt2.get())
    txt1.insert(tk.END,b)
    txt2.delete(0,tk.END)
    c=eval(txt1.get())
    txt1.delete(0,tk.END)
    txt2.insert(tk.END,c)


    
def Btn4Click():
    a=int(len(txt2.get()))
    txt2.delete(a-1)
    





def BtnsClick(btnName):
    s=""
    
    if btnName=="Btn9":
        s="7"
    elif btnName=="Btn10":
        s="8"
    elif btnName=="Btn11":
        s="9"
    elif btnName=="Btn13":
        s="4"
    elif btnName=="Btn14":
        s="5"
    elif btnName=="Btn15":
        s="6"
    elif btnName=="Btn17":
        s="1"
    elif btnName=="Btn18":
        s="2"
    elif btnName=="Btn19":
        s="3"
    elif btnName=="Btn22":
        s="0"
    txt2.insert(tk.END,"{0}".format(s))





MainForm=tk.Tk()
MainForm.title("小算盤")
MainForm.geometry("370x300")



txt1=tk.Entry(MainForm,width=50)

txt2=tk.Entry(MainForm,width=50)

but1=tk.Button(MainForm,text='%',width=10,command=Btn1Click)
but2=tk.Button(MainForm,text='CE',width=10,command=Btn2Click)
but3=tk.Button(MainForm,text='C',width=10,command=Btn3Click)
but4=tk.Button(MainForm,text='←',width=10,command=Btn4Click)

but5=tk.Button(MainForm,text='1/x',width=10,command=Btn5Click)
but6=tk.Button(MainForm,text='^2',width=10,command=Btn6Click)
but7=tk.Button(MainForm,text='√',width=10,command=Btn7Click)
but8=tk.Button(MainForm,text='÷',width=10,command=Btn8Click)

but9=tk.Button(MainForm,text='7',width=10,command=lambda:BtnsClick("Btn9"))
but10=tk.Button(MainForm,text='8',width=10,command=lambda:BtnsClick("Btn10"))
but11=tk.Button(MainForm,text='9',width=10,command=lambda:BtnsClick("Btn11"))
but12=tk.Button(MainForm,text='X',width=10,command=Btn12Click)

but13=tk.Button(MainForm,text='4',width=10,command=lambda:BtnsClick("Btn13"))
but14=tk.Button(MainForm,text='5',width=10,command=lambda:BtnsClick("Btn14"))
but15=tk.Button(MainForm,text='6',width=10,command=lambda:BtnsClick("Btn15"))
but16=tk.Button(MainForm,text='-',width=10,command=Btn16Click)

but17=tk.Button(MainForm,text='1',width=10,command=lambda:BtnsClick("Btn17"))
but18=tk.Button(MainForm,text='2',width=10,command=lambda:BtnsClick("Btn18"))
but19=tk.Button(MainForm,text='3',width=10,command=lambda:BtnsClick("Btn19"))
but20=tk.Button(MainForm,text='+',width=10,command=Btn20Click)

but21=tk.Button(MainForm,text='+/-',width=10,command=Btn21Click)
but22=tk.Button(MainForm,text='0',width=10,command=lambda:BtnsClick("Btn22"))
but23=tk.Button(MainForm,text='.',width=10,command=Btn23Click)
but24=tk.Button(MainForm,text='=',width=10,command=Btn24Click)


txt1.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
txt2.grid(row=1,column=0,columnspan=4,padx=5,pady=5)

but1.grid(row=2,column=0,padx=5,pady=5)
but2.grid(row=2,column=1,padx=5,pady=5)
but3.grid(row=2,column=2,padx=5,pady=5)
but4.grid(row=2,column=3,padx=5,pady=5)

but5.grid(row=3,column=0,padx=5,pady=5)
but6.grid(row=3,column=1,padx=5,pady=5)
but7.grid(row=3,column=2,padx=5,pady=5)
but8.grid(row=3,column=3,padx=5,pady=5)

but9.grid(row=4,column=0,padx=5,pady=5)
but10.grid(row=4,column=1,padx=5,pady=5)
but11.grid(row=4,column=2,padx=5,pady=5)
but12.grid(row=4,column=3,padx=5,pady=5)

but13.grid(row=5,column=0,padx=5,pady=5)
but14.grid(row=5,column=1,padx=5,pady=5)
but15.grid(row=5,column=2,padx=5,pady=5)
but16.grid(row=5,column=3,padx=5,pady=5)

but17.grid(row=6,column=0,padx=5,pady=5)
but18.grid(row=6,column=1,padx=5,pady=5)
but19.grid(row=6,column=2,padx=5,pady=5)
but20.grid(row=6,column=3,padx=5,pady=5)

but21.grid(row=7,column=0,padx=5,pady=5)
but22.grid(row=7,column=1,padx=5,pady=5)
but23.grid(row=7,column=2,padx=5,pady=5)
but24.grid(row=7,column=3,padx=5,pady=5)


MainForm.mainloop()

