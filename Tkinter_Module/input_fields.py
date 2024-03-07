from tkinter import *

root = Tk()

entry = Entry(root, width=50)
entry.pack()
entry.insert(0, "Enter your name")

def myClick():
    hello = "Hello " + entry.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter Your Name ", command=myClick)
#myButton = Button(root, text="Click me!", padx=10, pady=10, fg="blue", bg="red")
myButton.pack()

root.mainloop()