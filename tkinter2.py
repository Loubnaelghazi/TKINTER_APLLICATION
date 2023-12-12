

#using Icons ,maes,and exit buttons
#don t froget to install pillow by usin the command pip install pillow if yu don t have it 
from tkinter import *
from PIL import ImageTk,Image   #to use images inn tkinter

root=Tk()
root.title('course2')

'''to change the icon of the app:'''
#root.iconbitmap('url')

''' there is 3 steps to create an pic and add it to the screen '''

#1 :
'''my_img=ImageTk.PhotoImage(Image.open("URL"))  #puisque l imae 3ndi f fs folder dyl projet, il suffet nktbu rer smya 
#2
my_label=Label(image=my_img)
#3
my_label.pack()'''









root.mainloop()