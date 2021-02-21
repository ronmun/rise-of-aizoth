import pygame
import os

from Characters.entity import ORC_COST, ELF_COST, DINO_COST, WIZARD_COST
POSX_DOBLE_DIGITO = 1029
POSX_UN_DIGITO = 1040

class LevelUi:
    def __init__(self, win):
        self.pausePos = (953.5, 20)
        self.gemsTextPos = (1000, 90)
        self.elfTextPos = (POSX_UN_DIGITO, 196)
        self.dinoTextPos = (POSX_DOBLE_DIGITO, 330)
        self.orcTextPos = (POSX_DOBLE_DIGITO, 467)
        self.wizardTextPos = (POSX_UN_DIGITO, 600)
        self.pause = pygame.image.load(os.path.join("Assets/Sprites/Screens/Botones", "pausa.png"))
        self.pause = pygame.transform.scale(self.pause, (120, 52))
        self.font = pygame.font.Font(os.path.join("Assets/Fonts","m3x6.ttf"),80)
        self.win = win

    def draw(self, gems):
        self.win.blit(self.pause, self.pausePos)
        gems_text = self.font.render(str(gems), True, (183, 73, 232))
        elf_text = self.font.render(str(ELF_COST), True, (183, 73, 232))
        orc_text = self.font.render(str(ORC_COST), True, (183, 73, 232))
        dino_text = self.font.render(str(DINO_COST), True, (183, 73, 232))
        wizzard_text = self.font.render(str(WIZARD_COST), True, (183, 73, 232))
        self.win.blit(gems_text, self.gemsTextPos)
        self.win.blit(orc_text, self.orcTextPos)
        self.win.blit(dino_text, self.dinoTextPos)
        self.win.blit(wizzard_text, self.wizardTextPos)
        self.win.blit(elf_text, self.elfTextPos)

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