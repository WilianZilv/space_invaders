from tkinter import *
from projectile import Projectile
from collider import Collider
import time

class Enemy:

    def __init__(self, w, pos_x, pos_y, health, g_controller):

        self.g_controller = g_controller
        self.health = health
        self.w = w
        self.img = PhotoImage(file='sprites/enemy.png')
        self.size = (self.img.width(), self.img.height())
        self.col = Collider('enemy', self.size[0], self.size[1])
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.graphic = Frame(width=self.size[0], height=self.size[1], bg='black')
        Label(self.graphic, image=self.img, bg='black').pack()

        self.health_ui = Label(self.graphic, fg='white', bg='black')
        self.health_ui.pack()

        self.update_health_ui()

    def update(self):

        if self.health > 0:
            self.movement()
        else:
            return

    def render(self):

        render_pos = (self.pos_x - self.size[0]/2, self.pos_y - self.size[1]/2)
        self.col.set_position(render_pos[0], render_pos[1])
        self.graphic.place(x=render_pos[0], y=render_pos[1])

    def shoot(self):
        Projectile(self.w, self.pos_x, self.pos_y + self.size[1]/2, 1, self.g_controller.get_player(), 'red', self.g_controller)

    def damage(self):
        self.health -= 1

        if self.health <= 0:
            self.die(True)
            return
        self.update_health_ui()

    def update_health_ui(self):
        self.health_ui['text'] = 'HP: {}'.format(self.health)


    def die(self, score):

        self.health = 0
        if score is True:
            self.g_controller.on_enemy_die()

        self.col.enabled = False
        self.graphic.destroy()


