from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()

#showinfo,showerror,showwarning,askquestion,askokcancel,askyesno

def popup():
    response = messagebox.askquestion("This is my popup", "Hello World")
    Label(root, text = response).pack()
    #if response == 1:
     #   Label(root, text = "You Clicked Yes!").pack()
    #if response == 0:
     #   Label(root, text = "You Clicked No!").pack()

Button(root, text = "Popup", command = popup).pack()


root.mainloop()