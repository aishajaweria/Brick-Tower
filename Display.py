import tkinter
import tkinter.messagebox
from tkinter import *
import tkinter.font as font
window=tkinter.Tk()
window.title("Bricks Tower")

#main screen
window.configure(bg='#29C5F6')
def nextr():
    window.destroy()
    import block

def nextw():
    window.destroy()
    import frame

myFont = font.Font(family = "Cambria",size=25,weight='bold')

Btn=tkinter.Button(window,text='Start',command=nextr ,bg="#29C5F6",bd=0.3)
Btn2=tkinter.Button(window,text='Back',command=nextw ,bg="#29C5F6",bd=0.3)


#Setting font size
var=tkinter.Label(window,text="BRICKS TOWER",bg='#29C5F6',fg='black')
var1=tkinter.Label(window,text="This is a Brick Tower Game.",bg='#29C5F6',fg='white')
var2=tkinter.Label(window,text="In this game, the user have to ",bg='#29C5F6',fg='white')
var3=tkinter.Label(window,text="bulid a tower using moveable",bg='#29C5F6',fg='white')
var4=tkinter.Label(window,text="bricks to win.",bg='#29C5F6',fg='white')




var['font'] = myFont
var1['font'] = myFont
var2['font'] = myFont
var3['font'] = myFont
var4['font'] = myFont


Btn['font'] = myFont
Btn2['font']= myFont

var.place(relx=0.5, rely=0.1, anchor=CENTER)
var1.place(relx=0.5, rely=0.3, anchor=CENTER)
var2.place(relx=0.5, rely=0.4, anchor=CENTER)
var3.place(relx=0.5, rely=0.5, anchor=CENTER)
var4.place(relx=0.5, rely=0.6, anchor=CENTER)


Btn.place(relx=0.3, rely=0.8, anchor=CENTER)
Btn2.place(relx=0.7, rely=0.8, anchor=CENTER)
#setting Window's geometry
window.geometry("500x600")
window.mainloop()
