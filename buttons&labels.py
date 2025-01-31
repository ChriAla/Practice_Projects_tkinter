from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text = "I clicked a button!").grid(row = 4, column = 0)


# Create a Label widget
myLabel1 = Label(root, text = "Hello world").grid(row = 0, column = 0)
myLabel2 = Label(root, text = "my name is ").grid(row = 1, column = 1)

#shoving it onto the screen
#myLabel1.grid(row = 0, column = 0)


myButton = Button(root, text = "Click Me!", padx = 50, pady = 50, command = myClick).grid(row = 2, column = 0)
#myButton.pack()

root.mainloop()