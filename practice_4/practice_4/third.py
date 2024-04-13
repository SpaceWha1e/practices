from tkinter import *


def myClick():
    myLabel = Label(root, text="КТО ЖМАЛ")
    myLabel.pack()


root = Tk()
root.geometry("300x200")

myButton = Button(root, text="Жмите", command=myClick, fg="blue", bg="white")
myButton.pack()

root.mainloop()
