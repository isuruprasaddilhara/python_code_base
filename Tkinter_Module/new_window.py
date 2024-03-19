from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("New window")



def open():
    global my_img
    top = Toplevel()
    top.title("My second window")
    my_img = ImageTk.PhotoImage(Image.open("images/batman1.jpg"))
    my_label = Label(top, image=my_img)
    my_label.pack()
    btn2 = Button(top, text="Close Window",command=top.destroy).pack()

btn= Button(root, text="Open Second window",command=open).pack()

mainloop()