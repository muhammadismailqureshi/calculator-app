"""This a module for calculator app"""
from tkinter import *


#this is a module for the functions for calculator

#defining the basic functions
def add(num1, num2):
    """adds to numbers"""

    return num1 + num2


def substract(num1, num2):
    """Substract two numbers"""
    return num1 - num2


def multiply(num1, num2):
    """Multiplies two numbers"""
    return num1 * num2

def divide(num1, num2):
    """devides two numbers"""

    return num1 / num2

#Defining the functions for the user prompt

def calculate():
    """Takes user input and performs calculation"""
    operation = input("What do you want to do (+, -, x, /): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))


    if operation == "+":
        print(num1, "+", num2, "=",add(num1, num2))
    elif operation == "-":
        print(num1, "-", num2, "=", substract(num1, num2))
    elif operation == "x":
        print(num1, "x", num2, "=", multiply(num1, num2))
    elif operation == "/":
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid input")
    



root = Tk()

root.title("Calculator")

e = Entry(root, width=35, borderwidth=5)

e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    """Adds number to the entry box"""
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    """Clears the entry box"""
    e.delete(0, END)

def button_add():
    """Adds the two numbers in the entry box"""
    first_num = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    e.delete(0, END)


def button_equal():
    """Performs the appropriate calculation"""
    second_num = e.get()
    e.delete(0, END)

    if math =="addition":
        e.insert(0, f_num + int(second_num))
    elif math == "substraction":
        e.insert(0, f_num - int(second_num))
    elif math == "multiplication":
        e.insert(0, f_num * int(second_num))
    elif math == "division":
        e.insert(0, f_num / int(second_num))

def button_subtract():
    """Subtracts the  two numbers in the entry box"""
    first_num = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_num)
    e.delete(0, END)

def button_multiply():
    """Multiplies the two numbers in the entry box"""
    first_num = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_num)
    e.delete(0, END)

def button_divide():
    """Divides the two numbers in the entry box"""
    first_num =e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_num)
    e.delete(0, END)



# Defining buttons


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = Button(root, text="x", padx=40, pady=20, command=button_multiply)
button_divide= Button(root, text="/", padx=41, pady=20, command=button_divide)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)


#Display buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=3, column=1)
button_divide.grid(row=6, column=2)


root.mainloop()