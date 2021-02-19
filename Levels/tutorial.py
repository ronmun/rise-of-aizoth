import os
import pygame

from Levels.levelstate import LevelState
from Levels.level import Level
from Enemies.towers import DemonTower, SkellyTower


class Tutorial (Level):
    def __init__(self, w, h, win, game):
        super ().__init__(w,h,win)
        self.bg = pygame.image.load(os.path.join("Assets/Sprites/Screens", "01_Tutorial.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.game = game

    def start(self):
        print("Tutorial Starts")
        self.enemies.append(DemonTower(100,100,False))
        self.enemies.append(DemonTower(300,100,True))
        self.enemies.append(DemonTower(500,100,False))
        self.enemies.append(SkellyTower(0,0,False))

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.quit()

            if event.type == pygame.MOUSEBUTTONUP:
                # check if hit start btn
                x, y = pygame.mouse.get_pos()
                self.game.change(LevelState.REBELION)

    def draw(self):
        self.win.blit(self.bg, (0,0))
        for enemy in self.enemies:
            enemy.draw(self.win)
        #update not necesary bc it updates in game