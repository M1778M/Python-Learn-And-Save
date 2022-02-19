from tkinter import *

window = Tk()
window.title("None")

scr = Scrollbar(window)
scr.pack(side=RIGHT,fill=BOTH)

lb = Listbox(window)
lb.pack(expand=True,fill = BOTH)

scr.config(command=lb.yview)

for i in range(2222):
    lb.insert(END,"{}".format(i))
window.geometry('500x500')
window.mainloop()