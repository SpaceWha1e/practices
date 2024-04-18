import config
import csv
import tkinter as tk
from tkinter import filedialog

import ErrorWindow
import GraphWindow


class MainApp(tk.Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.count = 2
        self.button1 = tk.Button(self, text='Выбрать файл',
                                 width=25, command=self.load_file)
        self.button1.pack()
        self.button2 = tk.Button(self, text='Визуализация',
                                 width=25, command=self.graph)
        self.button2.pack()

    def load_file(self):

        filepath = filedialog.askopenfilename()
        if filepath != "":
            config.data = []
            with open(filepath, encoding='utf-8') as r_file:
                file_reader = csv.reader(r_file, delimiter=",")
                count = 0
                for row in file_reader:
                    print(count)
                    if count == 0:
                        if len(row) != 3:
                            ErrorWindow.ErrorWindow(self, config.errorTextImport)
                            break
                    else:
                        l = []
                        for num in row:
                            l.append(int(num))
                        print(l)
                        config.data.append(l)
                    count += 1
        else:
            ErrorWindow.ErrorWindow(self, config.errorTextImport)

    def graph(self):

        config.gW = GraphWindow.GraphWindow()
        config.gW.title = 'Окно визуализации'
