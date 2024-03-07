from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I Clicked a Button!!")
    myLabel.pack()

myButton = Button(root, text="Click me!", command=myClick)
#myButton = Button(root, text="Click me!", padx=10, pady=10, fg="blue", bg="red")
myButton.pack()

root.mainloop()