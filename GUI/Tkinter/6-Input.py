from tkinter import *

def ent():
    lbl.config(text='Nice')
    print("%")
    print(name.get())
    print(f.get())
    if f.get() == "Hello":
        print("Root")

window = Tk()
window.title("None")

Label(window,text='name').pack()
name = Entry(window)
name.pack()
Label(window,text='family').pack()
f = Entry(window)
f.pack()

btn = Button(window,text='Enter',command=ent)
btn.pack()
lbl = Label(window,text='')
lbl.pack()
window.geometry('400x400')
window.mainloop()