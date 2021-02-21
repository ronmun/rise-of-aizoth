import pygame
import os

from screen import Screen
from state import State

REANUDAR = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Sprites/Screens/Botones", "reanudar.png")), (180, 78))
OPCIONES = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Sprites/Screens/Botones", "opciones.png")), (180, 78))
MENU = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Sprites/Screens/Botones", "menu.png")), (180, 78))
BG = pygame.image.load(os.path.join("Assets/Sprites/Screens", "PantallaMenu.png"))

class Pause(Screen):
    def __init__(self, w, h, win, controller, game, level):
        super().__init__(w, h, win)
        self.bg = BG
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.game = game
        self.controller = controller
        self.win = win
        self.Level = level
        self.reanudarPos = (450, 168)
        self.opcionesPos = (450, 296)
        self.menuPos = (450, 424)

        self.reanudar = REANUDAR
        self.opciones = OPCIONES
        self.menu = MENU


    def draw(self):
        self.win.blit(self.bg, (0, 0))
        self.win.blit(self.reanudar, self.reanudarPos)
        self.win.blit(self.opciones, self.opcionesPos)
        self.win.blit(self.menu, self.menuPos)
        pygame.display.update()

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.controller.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                self.reanudarCheck(x, y)
                self.opcionesCheck(x, y)
                self.menuCheck(x, y)

    def reanudarCheck(self, x, y):
        if self.reanudarPos[0] <= x <= self.reanudarPos[0] + self.reanudar.get_width():
            if self.reanudarPos[1] <= y <= self.reanudarPos[1] + self.reanudar.get_height():
                self.game.reload_level(self.Level)

    def opcionesCheck(self, x, y):
        if self.opcionesPos[0] <= x <= self.opcionesPos[0] + self.opciones.get_width():
            if self.opcionesPos[1] <= y <= self.opcionesPos[1] + self.opciones.get_height():
                self.controller.change(State.OPCIONES, self)

    def menuCheck(self, x, y):
        if self.menuPos[0] <= x <= self.menuPos[0] + self.menu.get_width():
            if self.menuPos[1] <= y <= self.menuPos[1] + self.menu.get_height():
                self.controller.change(State.MENU)

