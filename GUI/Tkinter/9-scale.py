from tkinter import *
window = Tk()
window.title('None')
def get():
    print(scale.get())
scale = Scale(window,from_=0,to=100,orient=HORIZONTAL)
scale.pack()
Button(window,text='Enter',command=get).pack()
window.geometry('400x400')
window.mainloop()