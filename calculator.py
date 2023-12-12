
from tkinter import *

#this is a simple calculator proramm usign tkinter python


root=Tk()
root.title("Calculator")

def addButton(number):
    current=input.get() #avoir ce qu on ecrit
    input.delete(0,END) #ayms7 mtln la ktbt 300 ubghet n3wd nktb 500, mtb9ch dek 300 tma utm7a 3d tktb chihja khra
    input.insert(0, str(current)+ str(number)) #on utilisier str pour ne pas compter + , juste pour concatener pour pouvoir
    #ecrire 55 ,3330 .., et non un seul nmbre
    return

def addButton2():
    first_number=input.get()
    global f_number # so we can use it in all our code not just localy in the function
    f_number=int(first_number)  # make sure to make it
    input.delete(0,END)
    return

def equalButton():
    second_number=input.get()
    input.delete(0,END)
    input.insert(0,f_number + int(second_number))
    return

def clearButton():
    input.delete(0,END)
    return
#DEFINE INOUT AND BUTTONS:

input=Entry(root,width=35, borderwidth=5)
input.grid(row=0 ,column=0 ,columnspan= 3 ,padx=10 ,pady=10)

button_1=Button(root,text='1' ,padx=40 ,pady=20, command=lambda: addButton(1))
#afin de pouvoir passer de parametre, on doit utiliser(), on peut juste si on utilise LAMBDA
button_2=Button(root,text='2' ,padx=40 ,pady=20, command=lambda: addButton(2))
button_3=Button(root,text='3' ,padx=40 ,pady=20,command=lambda: addButton(3))
button_4=Button(root,text='4' ,padx=40 ,pady=20, command=lambda: addButton(4))
button_5=Button(root,text='5' ,padx=40 ,pady=20, command=lambda: addButton(5))
button_6=Button(root,text='6' ,padx=40 ,pady=20,command=lambda: addButton(6))
button_7=Button(root,text='7' ,padx=40 ,pady=20, command=lambda: addButton(7))
button_8=Button(root,text='8' ,padx=40 ,pady=20, command=lambda: addButton(8))
button_9=Button(root,text='9' ,padx=40 ,pady=20, command=lambda: addButton(9))
button_0=Button(root,text='0' ,padx=40 ,pady=20, command=lambda: addButton(0))
button_add=Button(root,text='+' ,padx=39 ,pady=20, command=addButton2)
button_equal=Button(root,text='=' ,padx='91' ,pady=20,  command=equalButton)
button_clear=Button(root,text='Clear' ,padx=79 ,pady=20,  command=clearButton)
#put the buttons oh the screen :
button_1.grid(row=3 ,column=0 )
button_2.grid(row=3 ,column=1 )
button_3.grid(row=3,column=2 )

button_4.grid(row=2 ,column=0 )
button_5.grid(row=2 ,column=1 )
button_6.grid(row=2 ,column=2 )

button_7.grid(row=1 , column= 0)
button_8.grid(row= 1, column= 1)
button_9.grid(row= 1, column=2 )

button_0.grid(row=4 ,column=0 )
button_add.grid(row=5 ,column=0 )
button_equal.grid(row=5 ,column=1 ,columnspan=2)

button_clear.grid(row=4 ,column=1 ,columnspan=2)

root.mainloop()