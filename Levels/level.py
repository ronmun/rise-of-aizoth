import os
import pygame

from Characters.entity import ORC_COST, ELF_COST, DINO_COST, WIZARD_COST
from Levels.level_ui import LevelUi
from Characters.elf import Elf
from Characters.dino import Dino
from Characters.ogre import Ogre
from Characters.wizard import Wizard

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
        self.gems = 0

    def start(self):
        pass

    def run(self):
        pass

    def check_character_buy(self, x, y):
        if self.level_ui.elfCheck(x, y) and self.gems - ELF_COST >= 0:
            self.characters.append(Elf(self.start_pos, self.path))
            self.gems -= ELF_COST
        if self.level_ui.dinoCheck(x, y) and self.gems - DINO_COST >= 0:
            self.characters.append(Dino(self.start_pos, self.path))
            self.gems -= DINO_COST
        if self.level_ui.orcCheck(x, y) and self.gems - ORC_COST >= 0:
            self.characters.append(Ogre(self.start_pos, self.path))
            self.gems -= ORC_COST
        if self.level_ui.wizardCheck(x, y) and self.gems - WIZARD_COST >= 0:
            self.characters.append(Wizard(self.start_pos, self.path))
            self.gems -= WIZARD_COST

    def initial_troop(self):
        self.characters.append(Elf(self.start_pos, self.path))

    def character_movement(self):
        for c in self.characters:
            c.move()
            if c.name == "wizard":
                c.regen()

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
        self.level_ui.draw(self.gems)
        # update not necesary bc it updates in game

    def end(self):
        pass