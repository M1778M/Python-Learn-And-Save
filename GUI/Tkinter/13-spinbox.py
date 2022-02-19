from tkinter import *

def get():
    print(w.get())
window = Tk()
window.title("None")

w = Spinbox(window,from_=0,to=100)
w.pack()

Button(window,text='Get',command=get).pack()

window.geometry('500x500')
window.mainloop()