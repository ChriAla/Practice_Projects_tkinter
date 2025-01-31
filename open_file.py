from tkinter import *
from PIL import ImageTk,Image 
from tkinter import filedialog

root = Tk()

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir = "images", title = "Select a File", filetypes = (("png", "*.png"),("all files", "*.*"))) 
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image = my_image).pack()

my_button = Button(root, text = "Open File", command = open).pack()

root.mainloop()