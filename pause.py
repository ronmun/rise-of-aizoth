import pygame
import os

from screen import Screen
from state import State

class Pause(Screen):
    def __init__(self, w, h, win, controller, State):
        super().__init__(w, h, win)
        self.bg = pygame.image.load(os.path.join("Assets/Sprites/Screens", "PantallaMenu.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.controller = controller
        self.win = win
        self.State = State
        self.reanudarPos = (390, 168)
        self.opcionesPos = (390, 296)
        self.menuPos = (390, 424)

        self.reanudar = pygame.image.load(os.path.join("Assets/Sprites/Screens/Botones", "reanudar.png"))
        self.opciones = pygame.image.load(os.path.join("Assets/Sprites/Screens/Botones", "opciones.png"))
        self.menu = pygame.image.load(os.path.join("Assets/Sprites/Screens/Botones", "menu.png"))

        self.reanudar = pygame.transform.scale(self.reanudar, (180, 78))
        self.opciones = pygame.transform.scale(self.opciones, (180, 78))
        self.menu = pygame.transform.scale(self.menu, (180, 78))

    def draw(self):
        self.win.blit(self.bg, (0, 0))
        self.win.blit(self.reanudar, self.reanudarPos)
        self.win.blit(self.opciones, self.opcionesPos)
        self.win.blit(self.menu, self.menuPos)
        pygame.display.update()

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                self.reanudarCheck(x, y)
                self.opcionesCheck(x, y)
                self.menuCheck(x, y)

    def reanudarCheck(self, x, y):
        if self.reanudarPos[0] <= x <= self.reanudarPos[0] + self.reanudar.get_width():
            if self.reanudarPos[1] <= y <= self.reanudarPos[1] + self.reanudar.get_height():
                self.controller.reload_screen(self.State)

    def opcionesCheck(self, x, y):
        if self.opcionesPos[0] <= x <= self.opcionesPos[0] + self.opciones.get_width():
            if self.opcionesPos[1] <= y <= self.opcionesPos[1] + self.opciones.get_height():
                self.controller.change(State.OPCIONES, self)

    def menuCheck(self, x, y):
        if self.menuPos[0] <= x <= self.menuPos[0] + self.menu.get_width():
            if self.menuPos[1] <= y <= self.menuPos[1] + self.menu.get_height():
                self.controller.change(State.MENU)

