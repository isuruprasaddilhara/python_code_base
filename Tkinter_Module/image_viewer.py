from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Learn to code at codemy.com")
root.iconphoto(False, PhotoImage(file = 'C:/Users/ASUS/Downloads/batman.png')  )

my_img1 = ImageTk.PhotoImage(Image.open('D:/Education Related/Python_Code_Base/Tkinter_Module/images/batman1.jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('D:/Education Related/Python_Code_Base/Tkinter_Module/images/batman2.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('D:/Education Related/Python_Code_Base/Tkinter_Module/images/batman3.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('D:/Education Related/Python_Code_Base/Tkinter_Module/images/batman4.jpg'))
my_img5 = ImageTk.PhotoImage(Image.open('D:/Education Related/Python_Code_Base/Tkinter_Module/images/batman5.jpg'))
my_img6 = ImageTk.PhotoImage(Image.open('D:/Education Related/Python_Code_Base/Tkinter_Module/images/batman6.jpg'))

img_list = [my_img1, my_img2, my_img3, my_img4, my_img5,my_img6]

status = Label(root, text="Image 1 of " + str(len(img_list)), border=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img1)                                                                                                                                                                                                                                                                                                                                                                     
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=img_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda:forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda:back(image_number-1))
    
    if image_number == 6:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    #update status bar
    status = Label(root, text="Image "+ str(image_number) +" of " + str(len(img_list)), border=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=img_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda:forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda:back(image_number-1))
    
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    #update status bar
    status = Label(root, text="Image "+ str(image_number) +" of " + str(len(img_list)), border=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_quit=Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda:forward(2))

button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)
root.mainloop() 