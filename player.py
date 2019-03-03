from tkinter import *
from collider import Collider
from pynput import keyboard
from projectile import Projectile
from window_shake import Shake

class Player:

    def __init__(self, w, pos_x, pos_y, get_enemies, on_hit, on_hit1):

        self.health = 100
        self.get_enemies = get_enemies
        self.w = w

        self.img = PhotoImage(file='sprites/player.png')
        self.size = (self.img.width(), self.img.height())
        self.pos_x = pos_x - self.size[0]/2
        self.pos_y = pos_y
        self.speed = 18
        self.reload_time = 200
        self.can_fire = True

        self.col = Collider('player', self.size[0], self.size[1])

        self.graphic = Frame(width=self.size[0], height=self.size[1])
        Label(self.graphic, image=self.img, bg='black').pack()

        self.on_hit = on_hit
        self.on_hit1 = on_hit1
        self.on_hit(self.health)

        keyboard.Listener(on_press=self.on_press).start()

        self.move()

    def move(self):

        self.col.set_position(self.pos_x, y=self.pos_y)
        self.graphic.place(x=self.pos_x, y=self.pos_y)
        self.w.after(1, lambda: self.move())

    def on_press(self, key):
        try:
            if key.char is 'd':
                self.pos_x += self.speed
            elif key.char is 'a':
                self.pos_x -= self.speed

        except AttributeError:
            if str(key) == 'Key.space':
                self.shoot()

    def shoot(self):
        if self.can_fire is True:
            self.can_fire = False
            Projectile(self.w, self.pos_x + self.size[0] / 2, self.pos_y, -1, self.get_enemies(), 'yellow')
            self.w.after(self.reload_time, self.reload_weapon)

    def reload_weapon(self):
        self.can_fire = True

    def damage(self):
        Shake(self.w, 5, 10)

        self.health -= 15
        self.on_hit(self.health)

        if self.health <= 0:
            self.die()
            self.on_hit1(-5)
            return
        pass

    def die(self):
        self.graphic.destroy()
        del self
