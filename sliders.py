from tkinter import *
from PIL import ImageTk, Image 

root = Tk()

root.geometry("400x400")

vertical = Scale(root, from_ = 0, to = 200)
vertical.pack()

horizontal = Scale(root, from_ = 0, to = 400, orient = HORIZONTAL)
horizontal.pack()

def clicked():
    my_label = Label(root, text = horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x400")

my_button = Button(root, text = "Click me!", command = clicked).pack()
root.mainloop()