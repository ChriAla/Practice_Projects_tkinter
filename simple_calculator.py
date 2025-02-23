from tkinter import *

root = Tk()
root.title("Simple Clculator")

e = Entry(root, width =35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

def buttonClick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number)) 

def buttonClear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global math
    math = "addition"
    global f_num 
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        e.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        e.insert(0, f_num * int(second_number))
    elif math == "division":
        e.insert(0, f_num / int(second_number))

def button_subtract():
    first_number = e.get()
    global math
    math = "subtraction"
    global f_num 
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global math
    math = "multiplication"
    global f_num 
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global math
    math = "division"
    global f_num 
    f_num = int(first_number)
    e.delete(0, END)


myButton1 = Button(root, text ="1",padx = 40, pady = 20, command = lambda: buttonClick(1))
myButton1.grid(row = 3, column = 0)
myButton2 = Button(root, text ="2",padx = 40, pady = 20, command = lambda: buttonClick(2))
myButton2.grid(row = 3, column = 1)
myButton3 = Button(root, text ="3",padx = 40, pady = 20, command = lambda: buttonClick(3))
myButton3.grid(row = 3, column = 2)
myButton4 = Button(root, text ="4",padx = 40, pady = 20, command = lambda: buttonClick(4))
myButton4.grid(row = 2, column = 0)
myButton5 = Button(root, text ="5",padx = 40, pady = 20, command = lambda: buttonClick(5))
myButton5.grid(row = 2, column = 1)
myButton6 = Button(root, text ="6",padx = 40, pady = 20, command = lambda: buttonClick(6))
myButton6.grid(row = 2, column = 2)
myButton7 = Button(root, text ="7",padx = 40, pady = 20, command = lambda: buttonClick(7))
myButton7.grid(row = 1, column = 0)
myButton8 = Button(root, text ="8",padx = 40, pady = 20, command = lambda: buttonClick(8))
myButton8.grid(row = 1, column = 1)
myButton9 = Button(root, text ="9",padx = 40, pady = 20, command = lambda: buttonClick(9))
myButton9.grid(row = 1, column = 2)
myButton0 = Button(root, text ="0",padx = 40, pady = 20, command = lambda: buttonClick(0))
myButton0.grid(row = 4, column = 0)
myButton_add = Button(root, text ="+",padx = 39, pady = 20, command = button_add)
myButton_add.grid(row = 5, column = 0)
myButton_equal = Button(root, text ="=",padx = 88, pady = 20, command = button_equal)
myButton_equal.grid(row = 5, column = 1, columnspan = 2)
myButton_clear = Button(root, text ="Clear",padx = 78, pady = 20, command = buttonClear)
myButton_clear.grid(row = 4, column = 1, columnspan = 2)
myButton_subtract = Button(root, text ="-",padx = 41, pady = 20, command = button_subtract)
myButton_subtract.grid(row = 6, column = 0)
myButton_multiply = Button(root, text ="*",padx = 40, pady = 20, command = button_multiply)
myButton_multiply.grid(row = 6, column = 1)
myButton_divide = Button(root, text ="/",padx = 41, pady = 20, command = button_divide)
myButton_divide.grid(row = 6, column = 2)



root.mainloop()