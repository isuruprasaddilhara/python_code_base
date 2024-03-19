from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Check boxes")
root.geometry("500x500")

def show():
    myLabel = Label(root, text=var.get()).pack()

var = StringVar()
c = Checkbutton(root, text="Check this box, I dare you!", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

myLabel=Label(root, text=var.get())
myLabel.pack()

my_btn = Button(root, text="show selection", command=show).pack()

root.mainloop()