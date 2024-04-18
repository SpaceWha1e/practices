import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

t = np.arange(0.0, 0.2, 0.1)
y1 = 2*np.sin(2*np.pi*t)
y2 = 4*np.sin(2*np.pi*2*t)

class Main:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        plotFrame = tk.Frame(master)
        plotFrame.pack()

        f = Figure(figsize=(5,4),dpi=100)
        self.ax = f.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(f, master=plotFrame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
        self.canvas.mpl_connect('button_press_event', self.onpick)

        line1, = self.ax.plot(t, y1, lw=2, color='red', label='1 HZ')
        line2, = self.ax.plot(t, y2, lw=2, color='blue', label='2 HZ')
        leg = self.ax.legend(loc='upper left', fancybox=True, shadow=True)
        leg.get_frame().set_alpha(0.4)

        # we will set up a dict mapping legend line to orig line, and enable
        # picking on the legend line
        """lines = [line1, line2]
        self.lined = dict()
        for legline, origline in zip(leg.get_lines(), lines):
            legline.set_picker(5)  # 5 pts tolerance
            self.lined[legline] = origline"""

    def onpick(self, event):
        print('you pressed', event.button, event.xdata, event.ydata)
        print("im here")
        # on the pick event, find the orig line corresponding to the
        # legend proxy line, and toggle the visibility
        legline = event.artist
        origline = self.lined[legline]
        vis = not origline.get_visible()
        origline.set_visible(vis)
        # Change the alpha on the line in the legend so we can see what lines
        # have been toggled
        if vis:
            legline.set_alpha(1.0)
        else:
            legline.set_alpha(0.2)
        self.canvas.draw()




root = tk.Tk()
my_gui = Main(root)
root.mainloop()