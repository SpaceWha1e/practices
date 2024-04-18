import tkinter as tk
import copy
import math
# noinspection PyTypeChecker
from tkinter import Tk
import config
import delone_triangulation

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from ErrorWindow import ErrorWindow


class DiagramWindow(tk.Tk):

    def __init__(self, values):
        super().__init__()
        self.values = values
        self.plot2 = None
        self.dots = None
        self.tri = None
        self.canvas = None
        self.diagram()

    def diagram(self):
        print('im diagram')

        fig = Figure(figsize=(5, 5), dpi=100)
        self.plot2 = fig.add_subplot(111)
        self.plot2.plot([i for i in range(0, 20)], self.values, color='black')
        self.plot2.set_xlabel("Точки")
        self.plot2.set_ylabel("R")
        self.plot2.set(xticks=range(0, 20, 5), xticklabels=range(0, 20, 5), yticks=range(int(min(self.values)), int(max(self.values) + 1), 2), yticklabels=range(int(min(self.values)), int(max(self.values) + 1), 2))
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

        toolbar = NavigationToolbar2Tk(self.canvas, self)
        toolbar.update()
        self.canvas.get_tk_widget().pack()
