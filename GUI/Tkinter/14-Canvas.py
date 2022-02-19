from tkinter import *

window = Tk()
window.title("ISF")
cavas_window = Canvas(window,width=500,height=320)
cavas_window.create_line(10,20,10,100)
cavas_window.create_line(50,20,50,100,fill='red',dash=(4,4))
cavas_window.create_rectangle(100,20,200,100,fill='green')
cavas_window.create_oval(350,20,430,100,fill='#000')
cavas_window.pack()

window.geometry('500x500')
window.mainloop()