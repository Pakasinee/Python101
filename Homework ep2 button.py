from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('Information')
GUI.geometry('350x450')

L1 = Label(GUI,text='information',font=('Leelawadee', 18),fg='#FF3366')
L1.place(x=100,y=20)

######################################

def Button1():
    text = 'Nezuko Kamado'
    messagebox.showinfo('Name and Surname',text)

FB1 = Frame(GUI)
FB1.place(x=100,y=80)
B1 = ttk.Button(FB1,text='Name',command=Button1)
B1.pack(ipadx=30,ipady=20)
#######################################

def Button2():
    text = '28 December'
    messagebox.showinfo('Birthday',text)

FB2 = Frame(GUI)
FB2.place(x=100,y=80)
B2 = ttk.Button(FB1,text='Date of Birth',command=Button2)
B2.pack(ipadx=30,ipady=20)
#######################################


def Button3():
    text = 'Tanjiro Kamado'
    messagebox.showinfo('Brother',text)

FB3 = Frame(GUI)
FB3.place(x=100,y=80)
B3 = ttk.Button(FB1,text='Family',command=Button3)
B3.pack(ipadx=30,ipady=20)
#######################################


def Button4():
    text = '203 Kyoto Japan'
    messagebox.showinfo('Address',text)

FB4 = Frame(GUI)
FB4.place(x=100,y=80)
B4 = ttk.Button(FB1,text='Country',command=Button4)
B4.pack(ipadx=30,ipady=20)
#######################################




GUI.mainloop()
