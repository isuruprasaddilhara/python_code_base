from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title("Learn to code at codemy.com")
root.iconbitmap('images/batman1.jpg')

frame = LabelFrame(root, text="This is my Frame...", padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Dont Click here!")
b.grid(row=0, column=0)

root.mainloop()
