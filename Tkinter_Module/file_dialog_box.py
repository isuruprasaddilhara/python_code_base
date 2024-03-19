from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root=Tk()
root.title("Codemy.com")
root.iconphoto(False, PhotoImage(file = 'C:/Users/ASUS/Downloads/batman.png')  )

def open():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir="D:", title="Select a File", filetypes=(("png files","*.png"),("all files","*.*")))

    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_img_label = Label(image=my_img).pack()



my_btn = Button(root,text="Open File",command=open).pack()

mainloop()