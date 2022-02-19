from tkinter import *
window = Tk()
window.title("Label")
Label(window,text="Hello World",font="Tahoma").pack()
Label(window,text="Hello World",fg='green',bg='gray',font=("Tahoma",20)).pack()
Label(window,text="Hello World",foreground='red',background="blue").pack()

window.geometry('400x400')
window.mainloop()