from tkinter import *
import random
class Shake:
    def __init__(self, window, ticks, force):

        self.start_x = window.winfo_x()
        self.start_y = window.winfo_y()

        self.shake(window, ticks, force)

    def shake(self, window, ticks, force):

        if ticks > 0:
            x = window.winfo_x() + random.randrange(-force, force)
            y = window.winfo_y() + random.randrange(-force, force)

            window.geometry('{}x{}+{}+{}'.format(window.winfo_width(), window.winfo_height(), x, y))

            window.after(10, lambda: self.shake(window, ticks-1, force))
        else:
            window.geometry('{}x{}+{}+{}'.format(window.winfo_width(), window.winfo_height(), self.start_x, self.start_y))
