import os
import pygame

from state import State
from screen import Screen
from menu_ui import MenuUi
from Levels.levelstate import LevelState


class MainMenu(Screen):
    def __init__(self, w, h, win, controller):
        super().__init__(w, h, win)
        # self.width = w
        # self.height = h
        # self.win = win
        self.bg = pygame.image.load(os.path.join("Assets/Sprites/Screens", "PantallaMenu.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.title = pygame.image.load(os.path.join("Assets/Sprites/Screens", "GameTitle.png")).convert_alpha()
        self.controller = controller
        self.interface = MenuUi(win)

    def start(self):
        print("Menu state!")

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.controller.quit()

            if event.type == pygame.MOUSEBUTTONUP:
                # check if hit start btn
                x, y = pygame.mouse.get_pos()

                if self.interface.level1Check(x, y):
                    self.controller.change(State.GAME, LevelState.TUTORIAL)
                elif self.interface.level2Check(x, y):
                    self.controller.change(State.GAME, LevelState.REBELION)
                elif self.interface.level3Check(x, y):
                    self.controller.change(State.GAME, LevelState.ESPERANZA)
                elif self.interface.opcionesCheck(x, y):
                    self.controller.change(State.OPCIONES, None)
                elif self.interface.creditosCheck(x, y):
                    self.controller.change(State.CREDITS, None)
                elif self.interface.salidaCheck(x, y):
                    self.controller.quit()

    def draw(self):
        self.win.blit(self.bg, (0, 0))
        self.win.blit(self.title, (self.width / 2 - self.title.get_width() / 2, 50))
        self.interface.draw()
        pygame.display.update()
