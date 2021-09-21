import tkinter as tk
from tkinter import messagebox

def add_digit(digit):
    value = calk.get()
    try:
        if value[0] == "0" and len(value) == 1:
            value = value[1:]
    except IndexError:
        value = value[1:]
    calk.delete(0, tk.END)
    calk.insert(0,value+digit)

def add_operation(oper):
    value = calk.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    elif "+" in value or "-" in value or "*" in value or "/" in value or "**(1/2)" in value or "%" in value:
        calculate()
        value = calk.get()
    calk.delete(0, tk.END)
    calk.insert(0,value+oper)

def calculate():
    value = calk.get()
    if value[-1] in '+-*/':
        value = value + value[:-1]
    calk.delete(0, tk.END)
    try:
        calk.insert(0,eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo("WARNING!","You need to print only digits!")
        calk.insert(0,0)
    except (ZeroDivisionError):
        messagebox.showinfo("WARNING!","Zero Division Error!")
        calk.insert(0,0)

def clear():
    calk.delete(0,tk.END)
    calk.insert(0,0)

def delete():
    value = calk.get()
    if len(value) == 1:
        clear()
    calk.delete(len(value)-1,tk.END)


def make_digit_button(digit):
    return tk.Button(text=digit, font=("Areal", 13), bg="black", fg="white", command=lambda:add_digit(digit))

def make_operation_button(operation):
    return tk.Button(text=operation, font=("Areal", 13),bg="black", fg="red", command=lambda:add_operation(operation))

def make_calc_button(calc):
    return tk.Button(text=calc, font=("Areal", 13),bg="black", fg="green", command=calculate)

def make_clear_button(calc):
    return tk.Button(text=calc, font=("Areal", 13),bg="black", fg="green", command=clear)

def delete_button(calc):
    return tk.Button(text=calc, font=("Areal", 13),bg="black", fg="green", command=delete)

def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()

win = tk.Tk()
win.title("Calculator")
photo = tk.PhotoImage(file="clc.png")
win.iconphoto(False, photo)
win.geometry("308x285")
win.resizable(False,False)
win.config(bg="black")
win.bind('<Key>', press_key)

calk = tk.Entry(win, justify=tk.RIGHT, font=("Arial", 19), width=15)
calk.grid(row=0, column=0, columnspan=5, sticky="we", pady=5, padx=10)
calk.insert(0,"0")
calk.config(bg="black", fg="white")

