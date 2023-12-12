
#this is my first project using tkinter python
from tkinter import *


# 1-positioning with tkinter s grid system :

root = Tk()    #notre fenetre et parent

def myClick():
    hello="hello "+ e.get()
    myLabel=Label(root,text=hello)
    myLabel.pack()

e= Entry(root,width=50 ,fg="pink")
e.pack()
e.insert(0,'Enter yu name : ')  #insert islike placeholder, 0 cuz we habe just one entry and we wan to put it inside it
#pack centre our element



myButton=Button(root,text="enter yu name : " , command=myClick) #always rember,in command dont use () when callin fcts !
myButton.pack()




root.mainloop()

