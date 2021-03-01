import pygame
import os

RETRY = pygame.image.load(os.path.join("Assets/Sprites/Screens/Botones", "retry.png"))
PAUSE = pygame.image.load(os.path.join("Assets/Sprites/Screens/Botones", "pausa.png"))
NEXT = pygame.image.load(os.path.join("Assets/Sprites/Screens/Botones", "next.png"))

from Characters.entity import ORC_COST, ELF_COST, DINO_COST, WIZARD_COST
POSX_DOBLE_DIGITO = 1029
POSX_UN_DIGITO = 1040

class LevelUi:
    def __init__(self, win):
        self.pausePos = (953.5, 20)
        self.gemsTextPos = (1000, 90)
        self.elfTextPos = (POSX_UN_DIGITO, 196)
        self.dinoTextPos = (POSX_UN_DIGITO, 330)
        self.orcTextPos = (POSX_DOBLE_DIGITO, 467)
        self.wizardTextPos = (POSX_DOBLE_DIGITO, 600)
        self.loseTextPos = (250, 200)
        self.winTextPos = (250, 200)
        self.tuto_text_pos = (200, 600)
        self.nextbuttonpos = (420, 400)
        self.retrybuttonpos = (420, 400)
        self.lost = False
        self.won = False
        self.delay_tuto_text = 0
        self.pause = PAUSE
        self.pause = pygame.transform.scale(self.pause, (120, 52))
        self.retry = RETRY
        self.retry = pygame.transform.scale(self.retry, (120, 52))
        self.next = NEXT
        self.next = pygame.transform.scale(self.next, (120, 52))
        self.font = pygame.font.Font(os.path.join("Assets/Fonts","m3x6.ttf"),80)
        self.messageFont = pygame.font.Font(os.path.join("Assets/Fonts","m3x6.ttf"),250)
        self.win = win

    def draw(self, name, gems):
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
        if name == "Tutorial" and not self.Tuto_Text_Delay():
            tutorial_text1 = self.font.render("Spend the gems on ally troops",True, pygame.Color('White'))
            tutorial_text2 = self.font.render("30 % of the gems must arrive", True, pygame.Color('White'))
            self.win.blit(tutorial_text1, self.tuto_text_pos)
            self.win.blit(tutorial_text2, (self.tuto_text_pos[0],self.tuto_text_pos[1]+50))

        if self.won:
            win_text = self.messageFont.render("YOU WON!", True, (255, 246, 0))
            self.win.blit(win_text, self.winTextPos)
            self.win.blit(self.next, self.nextbuttonpos)

        if self.lost:
            lose_text = self.messageFont.render("YOU LOST", True, (255, 32, 53))
            self.win.blit(lose_text, self.loseTextPos)
            self.win.blit(self.retry, self.retrybuttonpos)

    def pauseCheck(self, x, y):
        if self.pausePos[0] <= x <= self.pausePos[0] + self.pause.get_width():
            if self.pausePos[1] <= y <= self.pausePos[1] + self.pause.get_height():
                print("Pause")
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

    def nextCheck(self, x, y):
        if self.nextbuttonpos[0] <= x <= self.nextbuttonpos[0] + self.next.get_width():
            if self.nextbuttonpos[1] <= y <= self.nextbuttonpos[1] + self.next.get_height():
                return True

    def retryCheck(self, x, y):
        if self.retrybuttonpos[0] <= x <= self.retrybuttonpos[0] + self.retry.get_width():
            if self.retrybuttonpos[1] <= y <= self.retrybuttonpos[1] + self.retry.get_height():
                return True

    def Tuto_Text_Delay(self):
        if self.delay_tuto_text < 500:
            self.delay_tuto_text += 1
            if self.delay_tuto_text >= 500:
                return True
        else:
            return True