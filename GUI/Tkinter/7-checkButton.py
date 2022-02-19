from tkinter import *
def get():
    print(male_var.get())
    if male_var.get() == 1:
        print("you are male.")
    else:
        print("You are not male.")

window = Tk()
window.title('GT')
male_var = IntVar()
Checkbutton(window,text='male',variable=male_var).pack()
btn = Button(window,text="enter",command=get)
btn.pack()
window.geometry('400x400')
window.mainloop()