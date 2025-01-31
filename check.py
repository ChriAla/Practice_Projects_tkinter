from tkinter import *
from PIL import ImageTk, Image

def show():
    my_label = Label(root, text = var.get()).pack()

root = Tk()

var = IntVar()

c = Checkbutton(root, text = "Check this box!", variable = var)
c.pack()


my_button = Button(root, text = "Show selection!", command = show).pack()



root.mainloop()