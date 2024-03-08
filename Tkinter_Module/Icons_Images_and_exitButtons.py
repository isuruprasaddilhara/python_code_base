from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Learn to code at codemy.com")
root.iconphoto(False, PhotoImage(file = 'C:/Users/ASUS/Downloads/batman.png')  )

my_img = ImageTk.PhotoImage(Image.open('C:/Users/ASUS/Downloads/batman.jpg'))
my_label = Label(image=my_img)
my_label.pack()


button_quit=Button(root, text="Exit Program", command=root.quit)
button_quit.pack()
root.mainloop()