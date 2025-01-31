from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn to code')


my_img = ImageTk.PhotoImage(Image.open("images/Scary-Drawings.jpg"))
my_Label = Label(image = my_img)
my_Label.pack()


button_quit = Button(root, text = "Exit Program", command = root.quit)
button_quit.pack()



root.mainloop()