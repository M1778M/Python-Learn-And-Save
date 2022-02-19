from tkinter import *

window = Tk()
window.title("None")
modes = [("male",'male'),('female' ,'female'),('not','not')]
stri = StringVar()
stri.set("male")
for text,mode in modes:
    Radiobutton(window,text=text,variable=stri,value=mode).pack()

window.geometry('400x400')
window.mainloop()