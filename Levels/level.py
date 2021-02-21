import os
import pygame

class Level:
    def __init__(self, w, h, win):
        self.width = w
        self.height = h
        self.win = win
        self.bg = None
        self.enemies = []
        self.characters = []

    def start(self):
        pass

    def run(self):
        pass

    def draw(self):
        self.win.blit(self.bg, (0, 0))
        for ally in self.characters:
            ally.draw(self.win)
        for enemy in self.enemies:
            enemy.draw(self.win)
        # update not necesary bc it updates in game

    def end(self):
        pass