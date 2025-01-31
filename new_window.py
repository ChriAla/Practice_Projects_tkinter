from tkinter import *
from PIL import ImageTk,Image 

root = Tk()

def open():
    top = Toplevel()
    top.title('My second window')
    my_label = Label(top, text = "niceee!!!").pack()

button = Button(root, text = "Open second window", command = open).pack()

root.mainloop()