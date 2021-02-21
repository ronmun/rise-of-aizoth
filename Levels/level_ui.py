import pygame
import os


class LevelUi:
    def __init__(self, win):
        self.pausePos = (10, 10)
        self.pause = pygame.image.load(os.path.join("Assets/Sprites/Screens/Botones", "pausa.png"))
        self.pause = pygame.transform.scale(self.pause, (180, 78))
        self.win = win

    def draw(self):
        self.win.blit(self.pause, self.pausePos)

    def pauseCheck(self, x, y):
        if self.pausePos[0] <= x <= self.pausePos[0] + self.pause.get_width():
            if self.pausePos[1] <= y <= self.pausePos[1] + self.pause.get_height():
                print("Pausa")
                return True

    def elfCheck(self, x, y):
        if 957 <= x <= 1068:
            if 196 <= y <= 308:
                return True

    def dinoCheck(self, x, y):
        if 957 <= x <= 1068:
            if 330 <= y <= 445:
                return True

    def orcCheck(self, x, y):
        if 957 <= x <= 1068:
            if 467 <= y <= 580:
                return True

    def wizardCheck(self, x, y):
        if 957 <= x <= 1068:
            if 600 <= y <= 709:
                return True