import os
import pygame

from state import State
from screen import Screen

class Credits(Screen):
    def __init__(self, w, h, win, controller):
        super().__init__(w, h, win)
        self.bg = pygame.image.load(os.path.join("Assets/Sprites/Screens", "CreditsBg.png"))
        #self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.title = pygame.image.load(os.path.join("Assets/Sprites/Screens", "GameTitle.png")).convert_alpha()
        self.controller = controller

    def start(self):
        print("Credits state!")

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.controller.quit()

            if event.type == pygame.MOUSEBUTTONUP:
                # check if hit start btn
                x, y = pygame.mouse.get_pos()

    def draw(self):
        self.win.blit(self.bg, (0, 0))
        self.win.blit(self.title, (self.width / 2 - self.title.get_width() / 2, 50))
        self.interface.draw()
        pygame.display.update()