from tkinter import *
from PIL import ImageTk, Image

root = Tk()

def show():
    my_label = Label(root, text = clicked.get()).pack()

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"

]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

my_button = Button(root, text = "Show selection", command = show).pack()


root.mainloop()