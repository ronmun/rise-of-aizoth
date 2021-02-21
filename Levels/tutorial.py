import os
import pygame
import sys, inspect

from Levels.levelstate import LevelState
from Levels.level import Level
from Enemies.towers import DemonTower, SkellyTower
from Levels.level_ui import LevelUi

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from state import  State

class Tutorial (Level):
    def __init__(self, w, h, win, game):
        super ().__init__(w,h,win)
        self.bg = pygame.image.load(os.path.join("Assets/Sprites/Screens", "01_Tutorial.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.game = game
        self.level_ui = LevelUi(win)

    def start(self):
        print("Tutorial Starts")
        self.enemies.append(DemonTower(660, 370, False))
        self.enemies.append(SkellyTower(300, 150, True))
        self.enemies.append(SkellyTower(120, 370, False))
        self.enemies.append(SkellyTower(500, 0, True))

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.quit()

            if event.type == pygame.MOUSEBUTTONUP:
                # check if hit start btn
                x, y = pygame.mouse.get_pos()
                #self.game.change(LevelState.REBELION)
                if self.level_ui.pauseCheck(x, y):
                    self.game.controller.change(State.PAUSE, self)


    def draw(self):
        self.win.blit(self.bg, (0,0))
        self.level_ui.draw()
        for enemy in self.enemies:
            enemy.draw(self.win)
        #update not necesary bc it updates in game