from tkinter import *
from projectile import Projectile
from collider import Collider
from window_shake import Shake
import time

class Enemy:

    def __init__(self, w, pos_x, pos_y, health, get_player):

        self.health = health
        self.get_player = get_player
        self.col = Collider('enemy', 48, 28)
        self.w = w
        self.speed = .75
        self.img = PhotoImage(file='sprites/enemy.png')
        self.size = (self.img.width(), self.img.height())
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.graphic = Frame(width=self.size[0], height=self.size[1], bg='black')
        self.sprite = Label(self.graphic, image=self.img, bg='black')
        self.sprite.pack()

        self.btn = Label(self.graphic, bg='black', fg='white')
        self.btn.pack()

        self.update_health_ui()

        self.go_down = False
        self.t_x = 0
        self.t_y = 0
        self.dir = 1

        self.update()

    def update(self):

        my_width = self.graphic.winfo_width()
        my_height = self.graphic.winfo_height()

        if self.health > 0:
            self.movement()


        self.w.after(50, lambda: self.update())

    def movement(self):
        self.t_x += 1

        if self.t_x is 75 and self.go_down is False:
            self.t_x = 0
            self.dir *= -1
            self.go_down = True

        if self.go_down is True:
            self.t_y += 1
            self.pos_y += self.speed * 1.5
            if self.t_x is 10:
                self.go_down = False

        if self.go_down is False:
            self.pos_x += self.speed * self.dir

        self.col.set_position(self.pos_x, self.pos_y)
        self.graphic.place(x=self.pos_x, y=self.pos_y)

    def shoot(self):
        Projectile(self.w, self.pos_x + self.size[0]/2, self.pos_y, 1, self.get_player(), 'red')

    def damage(self):
        self.health -= 1

        if self.health <= 0:
            self.die(True)
            return
        self.update_health_ui()

    def update_health_ui(self):
        self.btn.config(text='HP: {}'.format(self.health))

    def die(self, score):

        self.health = 0
        if score is True:
            Shake(self.w, 5, 10)
            self.on_die(15)
        self.col.enabled = False
        self.btn.destroy()
        self.sprite.destroy()
        self.graphic.destroy()


