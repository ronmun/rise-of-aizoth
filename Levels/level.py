import os
import pygame

from Levels.level_ui import LevelUi

class Level:
    def __init__(self, w, h, win):
        self.width = w
        self.height = h
        self.win = win
        self.bg = None
        self.enemies = []
        self.characters = []
        self.start_pos = ()
        self.end_pos = ()
        self.level_ui = LevelUi(win)

    def start(self):
        pass

    def run(self):
        pass

    def character_movement(self):
        for c in self.characters:
            c.move()

    def enemy_attacks(self):
        for e in self.enemies:
            e.attack(self.characters)

    def draw(self):
        self.win.blit(self.bg, (0, 0))
        for enemy in self.enemies:
            enemy.draw(self.win)
        for ally in self.characters:
            ally.draw(self.win)
            if ally.health != ally.max_health:
                ally.draw_health_bar(self.win)
        self.level_ui.draw()
        # update not necesary bc it updates in game

    def end(self):
        pass