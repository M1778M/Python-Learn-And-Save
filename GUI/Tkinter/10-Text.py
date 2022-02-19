from tkinter import *
def save():
    print("Save")
    with open("output.txt",'w') as f:
        f.write(txt.get(1.0,END))

def insert():
    txt.insert(INSERT,"for i in range(22):")
window = Tk()
window.title("None")

txt = Text(window)
txt.pack()
Button(window,text='save',command=save).pack()
Button(window,text='Code',command=insert).pack()
window.geometry('800x800')
window.mainloop()