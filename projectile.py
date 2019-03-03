from tkinter import *
from collider import Collider

class Projectile:

    def __init__(self, w, pos_x, pos_y, dir, targets, color):

        self.targets = targets
        self.col = Collider('projectile', 4, 16)

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dir = dir

        self.w = w

        self.graphic = Frame()
        self.graphic.config(bg=color, width=4, height=16)

        self.move()

    def move(self):

        self.pos_y += .5 * self.dir

        self.col.set_position(self.pos_x, self.pos_y)

        if self.targets is not None:
            for target in self.targets:
                if target.col.enabled is True:
                    if self.col.check_collision(target.col) is True:
                        self.graphic.destroy()
                        target.damage()
                        return

        self.graphic.place(x=self.pos_x, y=self.pos_y)

        if self.pos_y < self.w.winfo_height() and self.pos_y > 0:
            self.w.after(1, lambda: self.move())
        else:
            self.graphic.destroy()
            del self
