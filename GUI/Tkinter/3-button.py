from tkinter import *
import time
window = Tk()
window.title("Button")
lb = Label(window,text="Hello World")
btn = Button(window,text="Click Me",bg="yellow",fg='blue')
lb.config(fg="red")
btn.config(bg='#fff',text='None')
lb.pack()
btn.pack()
window.geometry('400x400')
window.mainloop()