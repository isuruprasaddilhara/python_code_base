from tkinter import *
from tkinter import messagebox

root= Tk()
root.title("Message Box")
#showinfo, showwarning, showerror, askquesion, askokcancle, askyesno
def popup():
    response = messagebox.askyesno("This is my Popup!","Hello World!")
    Label(root, text=response).pack()

Button(root, text="Popup", command=popup).pack()

root.mainloop()