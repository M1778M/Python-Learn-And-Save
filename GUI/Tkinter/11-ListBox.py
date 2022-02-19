from tkinter import *

def add():
    lb.insert(END,name.get())

def cls():
    lb.delete(0,END)
window = Tk()
window.title("NOne")
name = Entry(window)
name.pack()
lb = Listbox(window,)
lb.pack()
lb.insert(1,"ali")
lb.insert(2,"kokab")
lb.insert(3,"maryam")
lb.insert(4,"reza")
lb.insert(5,"kein")
Button(window,text="Add",command=add).pack()
Button(window,text='clear',command=cls).pack()
window.geometry('500x500')
window.mainloop()