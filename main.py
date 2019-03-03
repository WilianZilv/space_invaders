from tkinter import *
from enemy import Enemy
from player import Player
import random


class Main:

    def __init__(self):

        width = 800
        height = 600

        # -WINDOW INITIALIZE
        w = Tk()
        w.title('Space Invaders')
        w['bg'] = 'black'
        w.geometry('{}x{}'.format(width, height))
        w.minsize(width=width, height=height)
        w.maxsize(width=width, height=height)

        self.w = w

        # -STATS
        self.score = 0
        self.game_ended = False

        # -ELEMENTS

        # score
        self.score_label = Label()
        self.score_label.place(x=8, y=8)
        self.score_label.lift()
        self.update_score_ui()

        # health
        self.health_label = Label()
        self.health_label.place(x=8, y=32)
        self.health_label.lift()

        self.enemies = []

        max_enemies_x = 8
        max_enemies_y = 5

        initial_x = width / max_enemies_x
        initial_y = 40

        for x in range(max_enemies_x):
            for y in range(max_enemies_y):
                e = Enemy(self.w, initial_x/10 + initial_x * x, initial_y + initial_y * y, max_enemies_y - y + 1, lambda: self.get_player())
                e.on_die = self.scored
                self.enemies.append(e)

        w.after(2000, lambda: self.choose_random_enemy_to_shoot())

        self.player = Player(w, width/2, 500, self.get_enemies, self.update_health_ui, self.scored)


        w.mainloop()

    def get_player(self):
        return [self.player]

    def get_enemies(self):

        valid_enemies = []

        for enemy in self.enemies:
            if enemy.health > 0:
                valid_enemies.append(enemy)

        if valid_enemies is None:
            self.end_game(True)
            self.enemies = None
            return self.enemies

        self.enemies = valid_enemies
        return self.enemies

    def pack_targets(self):
        pass

    def choose_random_enemy_to_shoot(self):

        enemies = self.get_enemies()

        if enemies is not None:
            enemy = random.choice(enemies)
            enemy.shoot()
        else:
            return

        self.w.after(random.randrange(500, 2000), lambda: self.choose_random_enemy_to_shoot())

    def scored(self, amt):
        self.score += amt
        self.update_score_ui()

    def update_score_ui(self):
        self.score_label.config(text='SCORE: {}'.format(self.score))

    def update_health_ui(self, v):

        if v <= 0:
            v = 0
            self.end_game(False)

        self.health_label.config(text='HP: {}'.format(v))

    def end_game(self, win):

        if self.enemies is not None:
            for e in self.enemies:
                e.die(False)

        if win is True:
            print('You Won!')
        else:
            print('You Loose!')


Main()
