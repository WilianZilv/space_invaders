from tkinter import *
from collider import Collider
from projectile import Projectile

class Player:

    def __init__(self, w, pos_x, pos_y, g_controller):

        self.g_controller = g_controller
        self.health = 100
        self.w = w

        self.img = PhotoImage(file='sprites/player.png')
        self.size = (self.img.width(), self.img.height())
        self.pos_x = pos_x - self.size[0]/2
        self.pos_y = pos_y
        self.speed = 18
        self.reload_time = 200
        self.can_fire = True

        self.col = Collider('player', self.size[0], self.size[1])

        self.graphic = Frame(width=self.size[0], height=self.size[1], bg='black')
        Label(self.graphic, image=self.img, bg='black').pack()

        w.bind('<KeyPress>', self.on_press)

        self.move()

    def move(self):

        if self.is_dead() is True:
            return

        self.col.set_position(self.pos_x, y=self.pos_y)
        self.graphic.place(x=self.pos_x, y=self.pos_y)


    def on_press(self, key):

        if self.is_dead() is True:
            return

        try:
            if key.char is 'd':
                self.pos_x += self.speed
            elif key.char is 'a':
                self.pos_x -= self.speed
            elif key.char is ' ':
                self.shoot()

        except AttributeError:
            pass

    def shoot(self):
        if self.can_fire is True:
            self.can_fire = False
            Projectile(self.w, self.pos_x + self.size[0] / 2, self.pos_y, -1, self.enemies, 'yellow', self.g_controller)
            self.w.after(self.reload_time, self.reload_weapon)

    def reload_weapon(self):
        self.can_fire = True

    def damage(self):

        self.health -= 15
        self.on_player_damage()

        if self.health <= 0:
            self.die()
            return
        pass

    def die(self):
        self.graphic.destroy()

    def is_dead(self):
        return self.health <= 0
