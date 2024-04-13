from tkinter import *

root = Tk()
root.geometry("300x200")

myLabel1 = Label(root, text="Hello, World!", foreground="white", background="#488cff")
myLabel2 = Label(root, text="Меня зовут Женя", foreground="white", background="#488cff")
myLabel1.grid(row=1, column=1)
myLabel2.grid(row=2, column=2)
root.mainloop()
