from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn To Code at Codemy.com')

frame = LabelFrame(root, text = "This is my Frame ...", padx = 5, pady = 5)
frame.pack(padx = 10, pady = 10)

b = Button(frame, text = "Dont click here")
b.grid(row = 0, column = 0)


root.mainloop()