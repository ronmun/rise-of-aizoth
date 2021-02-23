import os
import pygame

from state import State
from screen import Screen
from menu_ui import MenuUi
from Levels.levelstate import LevelState

from Characters.elf import Elf
from Characters.dino import Dino
from Characters.orc import Orc
from Characters.wizard import Wizard

class MainMenu(Screen):
    def __init__(self, w, h, win, controller):
        super().__init__(w, h, win)
        self.bg = pygame.image.load(os.path.join("Assets/Sprites/Screens", "PantallaMenu.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.title = pygame.image.load(os.path.join("Assets/Sprites/Screens", "GameTitle.png")).convert_alpha()
        self.controller = controller
        self.interface = MenuUi(win)
        self.path = [(-50, 595),(1100, 595)]
        self.characters = [Dino((-800, 595), self.path),
                           Elf((-250, 595), self.path),
                           Orc((-575, 595), self.path),
                           Wizard((-620, 595), self.path),
                           Dino((2000, 595), self.path[::-1]),
                           Elf((1670, 595), self.path[::-1]),
                           Orc((1425, 595), self.path[::-1]),
                           Wizard((1325, 595), self.path[::-1])]

    def start(self):
        print("Menu state!")

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.controller.quit()

            if event.type == pygame.MOUSEBUTTONUP:
                # check if hit start btn
                x, y = pygame.mouse.get_pos()
                print(x, y)

                if self.interface.level1Check(x, y):
                    self.controller.change(State.CINEMATIC)
                elif self.interface.level2Check(x, y):
                    self.controller.change(State.GAME, None, LevelState.REBELION)
                elif self.interface.level3Check(x, y):
                    self.controller.change(State.GAME, None, LevelState.ESPERANZA)
                elif self.interface.opcionesCheck(x, y):
                    self.controller.change(State.OPCIONES, State.MENU)
                elif self.interface.creditosCheck(x, y):
                    self.controller.change(State.CREDITS)
                elif self.interface.salidaCheck(x, y):
                    self.controller.quit()

    def draw(self):
        self.win.blit(self.bg, (0, 0))
        self.win.blit(self.title, (self.width / 2 - self.title.get_width() / 2, 50))
        for ally in self.characters:
            ally.move()
            ally.draw(self.win)
        self.interface.draw()
        pygame.display.update()
