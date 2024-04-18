import copy
import math
# noinspection PyTypeChecker
from tkinter import Tk
import tkinter as tk
import config
import delone_triangulation
import DiagramWindow

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from ErrorWindow import ErrorWindow


class GraphWindow(Tk):
    def __init__(self):
        super().__init__()
        self.data = np.array(config.data)
        self.point1 = None
        self.point2 = None
        self.point1Bool = True
        self.drawLine = None
        self.drawLineLen = None
        self.drawLineBool = False
        self.point1Scatter = None
        self.button1 = None
        self.point2Scatter = None
        self.dW = None
        self.dots = None
        self.tri = None
        self.canvas = None
        if self.data.shape[0] == 0:
            ErrorWindow(config.mainApp, config.errorData)
            self.destroy()
        else:
            if self.data.shape[1] != 3:
                ErrorWindow(config.mainApp, config.errorDataImport)
                self.destroy()
            else:
                self.graph()

    def graph(self):

        fig = Figure(figsize=(5, 5), dpi=100)
        self.plot1 = fig.add_subplot(111)

        self.s = 10
        x = self.data[:, 0].flatten()
        y = self.data[:, 1].flatten()
        colors = [self.data[:, 2].flatten()]
        scatter = self.plot1.scatter(x, y, c=colors, s=self.s, cmap='viridis')
        legend1 = self.plot1.legend(*scatter.legend_elements(), loc="upper right", title="R")
        self.plot1.add_artist(legend1)
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()
        self.canvas.mpl_connect('button_press_event', self.onpick)
        self.canvas.get_tk_widget().pack()

        toolbar = NavigationToolbar2Tk(self.canvas, self)
        toolbar.update()
        self.canvas.get_tk_widget().pack()

    def onpick(self, event):
        print('you pressed', event.button, event.xdata, event.ydata, round(event.xdata), round(event.ydata))
        print("im here")
        if self.point1Bool:
            self.point1 = [round(event.xdata), round(event.ydata)]
            self.point1Bool = False
        elif not self.point2:
            self.point2 = [round(event.xdata), round(event.ydata)]
            self.drawLineLen = GraphWindow.lenn(self.point1, self.point2)
            self.drawLine = self.plot1.plot([self.point1[0], self.point2[0]], [self.point1[1], self.point2[1]], color='grey', alpha=0.3)
            self.dots = np.array([self.point1, *([self.point1[0] + i * self.drawLineLen[0], self.point1[1] + i * self.drawLineLen[1]] for i in range(1, 19)), self.point2])
            print(self.drawLineLen)
            print(self.point1)
            print(self.point2)
            print(self.dots)
            self.tri = delone_triangulation.delone_triangulation(self, self.data[:, 0:2], self.data[:, 2], self.dots, 2)
            print(self.tri)
            x = self.dots[:, 0].flatten()
            y = self.dots[:, 1].flatten()
            colors = [self.tri.flatten()]
            scatter2 = self.plot1.scatter(x, y, c=colors, s=self.s, cmap='viridis')
            self.button1 = tk.Button(self, text='Эпюра', width=25, height=5, command=self.diagram).pack()
        """        else:
            for x in self.drawLine:
                x.remove()
            self.point1 = [round(event.xdata), round(event.ydata)]
            self.point2 = None"""

        self.canvas.draw()

    @staticmethod
    def lenn(point1, point2):
        return [(point2[0] - point1[0])/19, (point2[1] - point1[1])/19]

    def diagram(self):
        self.dW = DiagramWindow.DiagramWindow(self.tri)
        self.dW.title = 'Эпюра'
