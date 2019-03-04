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

        # -ENEMIES VAR
        self.cur_time_y = 0
        self.g_dir = 1
        self.g_speed = .15
        self.go_down = False

        # -ELEMENTS

        # score
        self.score_label = Label()
        self.score_label.place(x=8, y=8)
        self.scored(0)

        # health
        self.health_label = Label()
        self.health_label.place(x=8, y=32)
        self.health_label.lift()

        self.enemies = []
        self.projectiles = []

        max_enemies_x = 10
        max_enemies_y = 5

        spacing = 60
        initial_y = 38

        for x in range(max_enemies_x):
            for y in range(max_enemies_y):
                e = Enemy(self.w, 45 + spacing * (x+1), initial_y + initial_y * y, max_enemies_y - y + 1, self)
                self.enemies.append(e)

        w.after(2000, lambda: self.choose_random_enemy_to_shoot())

        self.player = Player(w, width/2, 500, self)
        self.player.on_player_damage = self.on_player_damage
        self.player.enemies = self.enemies

        self.update_health_ui(self.player.health)

        self.fixed_update()

        w.mainloop()

    def fixed_update(self):

        self.player.move()
        self.enemies_movement()
        self.projectiles_movement()

        self.w.after(10, self.fixed_update)

    def enemies_movement(self):

        if self.enemies is not None:

            correct_pos = False

            for e in self.enemies:

                if e.pos_x > 700:
                    self.g_dir = -1
                    self.go_down = True
                    correct_pos = True
                    break

                elif e.pos_x <= 100:
                    self.g_dir = 1
                    self.go_down = True
                    correct_pos = True
                    break

            for e in self.enemies:

                if correct_pos is True:
                    e.pos_x += 1 * self.g_dir

                if self.go_down is False:
                    e.pos_x += self.g_speed * self.g_dir
                else:
                    e.pos_y += self.g_speed

                e.render()

            if self.go_down is True:
                self.cur_time_y += 1
                if self.cur_time_y > 100:
                    self.cur_time_y = 0
                    self.go_down = False

    def projectiles_movement(self):

        for p in self.projectiles:
            p.move()


    def get_player(self):
        if self.player.is_dead():
            return []

        return [self.player]

    def update_enemies(self):

        valid_enemies = []

        for enemy in self.enemies:
            if enemy.health > 0:
                valid_enemies.append(enemy)

        if len(valid_enemies) is 0:
            self.end_game(True)
            self.enemies = None
            return self.enemies

        self.enemies = valid_enemies
        return self.enemies

    def choose_random_enemy_to_shoot(self):

        if self.enemies is not None:
            enemy = random.choice(self.enemies)
            enemy.shoot()
        else:
            return

        self.w.after(random.randrange(500, 2000), lambda: self.choose_random_enemy_to_shoot())

    def scored(self, amt):
        self.score += amt
        self.score_label.config(text='SCORE: {}'.format(self.score))

    def on_player_damage(self):
        self.scored(-5)
        self.update_health_ui(self.player.health)

    def on_enemy_die(self):
        self.scored(15)
        self.update_enemies()

    def update_health_ui(self, v):

        if v <= 0:
            v = 0
            self.end_game(False)

        self.health_label.config(text='HP: {}'.format(v))

    def end_game(self, win):

        self.game_ended = True

        if win is True:
            print('You Won!')
        else:
            print('You Loose!')


Main()
