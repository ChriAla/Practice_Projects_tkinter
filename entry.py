from tkinter import *

root = Tk()

e = Entry(root)
e.grid(row = 0, column = 0)
e.insert(0, "Enter your Name:")

def myClick():
    hello = "Hello "
    myLabel = Label(root, text = hello + e.get())
    myLabel.grid(row = 3, column = 0)

myButton = Button(root, text = "Enter your name", command = myClick)
myButton.grid(row = 2, column = 0)

root.mainloop()