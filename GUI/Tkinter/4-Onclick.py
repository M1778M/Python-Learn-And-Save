from tkinter import *
cnt = 0
def onclick():
    global cnt
    cnt += 1
    print(cnt)
    lb.config(text='count: {}'.format(cnt))


window = Tk()
window.title("None")
lb = Label(window,text='T: ')
lb.pack()
Button(window,text="Click!",command=onclick).pack()


window.geometry('400x400')
window.mainloop()