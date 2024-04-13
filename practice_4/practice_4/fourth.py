from tkinter import *


def myClick():
    myLabel = Label(root, text="Привет, " + myEntry.get())
    myLabel.pack()


root = Tk()
root.geometry("300x200")

myEntry = Entry(root, width=50, bg="blue", fg="white", borderwidth=5)
myEntry.pack()
myEntry.insert(0, "Введите Ваше имя")

myButton = Button(root, text="Жмите", command=myClick, fg="blue", bg="white")
myButton.pack()

root.mainloop()
