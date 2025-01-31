from tkinter import *
from PIL import ImageTk,Image

root = Tk()

#r = IntVar()
#r.set("2")

TOPPINGS =[
    ("pepperoni", "pepperoni"),
    ("cheese", "cheese"),
    ("mushroom", "mushroon"),
    ("onion", "onion")
]

pizza = StringVar()
pizza.set("pepperoni")

for text, topping in TOPPINGS:
    Radiobutton(root, text = text, variable = pizza, value = topping).pack(anchor = W)

def clicked(value):
    mylabel = Label(root, text = value)
    mylabel.pack()

#Radiobutton(root, text = "Option 1", variable = r, value = 1, command = lambda: clicked(r.get())).pack()
#Radiobutton(root, text = "Option 2", variable = r, value = 2, command = lambda: clicked(r.get())).pack()

mybutton = Button(root, text = "Click me", command = lambda: clicked(pizza.get()))
mybutton.pack()

#mylabel = Label(root, text = r.get())
#mylabel.pack()

root.mainloop()