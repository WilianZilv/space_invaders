from tkinter import *
from collider import Collider
from window_shake import Shake

class Projectile:

    def __init__(self, w, pos_x, pos_y, dir, targets, color, g_controller):

        self.g_controller = g_controller
        self.targets = targets
        self.col = Collider('projectile', 4, 16)

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dir = dir

        self.w = w

        self.graphic = Frame()
        self.graphic.config(bg=color, width=4, height=16)

        self.move()

        self.g_controller.projectiles.append(self)

    def move(self):

        self.pos_y += 4 * self.dir

        self.col.set_position(self.pos_x, self.pos_y)

        if self.targets is not None:
            for target in self.targets:
                if target.col.enabled is True:
                    if self.col.check_collision(target.col):
                        target.damage()
                        Shake(self.w, 5, 10)
                        self.destroy_p()
                        return

        if self.pos_y > self.w.winfo_height() or self.pos_y < 0:
            self.destroy_p()
            return

        self.graphic.place(x=self.pos_x, y=self.pos_y)

    def destroy_p(self):
        self.graphic.destroy()

        p = self.g_controller.projectiles
        for id in range(len(p)):
            if p[id] is self:
                self.g_controller.projectiles.pop(id)
                return

