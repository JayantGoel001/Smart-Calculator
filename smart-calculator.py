from tkinter import *


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def mod(a, b):
    return a % b


def LCM(a, b):
    L = a if a > b else b
    while L <= a * b:
        if L % a == 0 and L % b == 0:
            return L
        L += 1


def HCF(a, b):
    H = a if a < b else b
    while H >= 1:
        if a % H == 0 and b % H == 0:
            return H
        H -= 1


def extractNumbers(text):
    listOfNumbers = []
    for t in text.split():
        try:
            listOfNumbers.append(float(t))
        except ValueError:
            pass
    return listOfNumbers


def calculate():
    text = textIn.get()
    listOfNumbers = extractNumbers(text)
    for word in text.split():
        if word.upper() in operations.keys():
            try:
                result = operations[word.upper()](listOfNumbers[0], listOfNumbers[1])
                listBox.delete(0, END)
                listBox.insert(END, result)
            except ValueError:
                listBox.delete(0, END)
                listBox.insert(END, "Something Went Wrong!!")
            finally:
                break
        else:
            listBox.delete(0, END)
            listBox.insert(END, "Something Went Wrong!!")


operations = {
    'ADD': add, 'ADDITION': add, 'SUM': add, 'PLUS': add,
    'SUB': subtract, 'DIFFERENCE': subtract, 'MINUS': subtract, 'SUBTRACT': subtract,
    'LCM': LCM, 'HCF': HCF,
    'PRODUCT': multiply, 'MULTIPLICATION': multiply, 'MUL': multiply,
    'DIV': divide, 'DIVISION': divide, 'DIVIDE': divide,
    'MOD': mod, 'REMAINDER': mod, 'MODULUS': mod
}

win = Tk()

win.geometry("500x300")
win.title("Smart Calculator")
win.configure(bg='lightskyblue')

l1 = Label(win, text="I am a Smart Calculator", width=30, padx=3)
l1.configure(fg="black", bg='white', font=("Bold", 11))
l1.place(x=100, y=10)

l2 = Label(win, text="Created and Maintained By Jarvis", padx=3)
l2.configure(fg="black", bg='white', font=("Bold", 11))
l2.place(x=130, y=40)

l3 = Label(win, text="How Can I Help You?", padx=3)
l3.configure(fg="black", bg='white', font=("Bold", 11))
l3.place(x=170, y=130)

textIn = StringVar()
e1 = Entry(win, width=50, text="Enter Here", textvariable=textIn)
e1.configure(fg="black", bg='white')
e1.place(x=100, y=165)

b1 = Button(win, text="Just This", command=calculate)
b1.configure(fg="black", bg='white')
b1.place(x=215, y=200)

listBox = Listbox(win, width=30, height=3)
listBox.configure(fg="black", bg='white')
listBox.place(x=150, y=230)

win.mainloop()
