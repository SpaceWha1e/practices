import tkinter as tk


class ErrorWindow:
    def __init__(self, root, label):
        self.top = tk.Toplevel(root)
        self.top.geometry('500x50')
        self.top.title("ОШИБКА")
        tk.Label(self.top, text=label).pack()
        self.top.buttonEx = (tk.Button(self.top, text='okay', command=self.top.destroy))
        self.top.buttonEx.pack()
        self.top.grab_set()
        self.top.focus_set()
        self.top.wait_window()
