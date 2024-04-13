from tkinter import *

root = Tk()
root.geometry("300x200")

myLabel = Label(root, text="Hello, World!", foreground="white", background="#488cff")
myLabel.pack(anchor=CENTER, expand=1)

root.mainloop()
