from tkinter import *

win = Tk()

win.geometry("500x300")
win.title("Smart Calculator")
win.configure(bg='black')

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
e1.place(x=100, y=165)

b1 = Button(win, text="Just This")
b1.place(x=215, y=200)

listBox = Listbox(win, width=30, height=3)
listBox.place(x=150, y=230)

win.mainloop()
