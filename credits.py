import os
import pygame

from state import State
from screen import Screen

BG_IMAGE = pygame.image.load(os.path.join("Assets/Sprites/Screens", "CreditsBg.png"))
EXIT_BUTTON = pygame.image.load(os.path.join("Assets/Sprites/Screens/Botones", "exit.png"))

class Credits(Screen):
    def __init__(self, w, h, win, controller):
        super().__init__(w, h, win)
        self.bg = BG_IMAGE
        self.bg.set_clip(pygame.Rect(0, 0, 1080, 720))
        self.image = self.bg.subsurface(self.bg.get_clip())
        self.rect = self.image.get_rect()
        self.frame = 0
        self.states = {0: (0, 0, 1080, 5464 - 720)}

        self.controller = controller
        self.clock = pygame.time.Clock()
        self.salidaPos = (940, 0)
        self.salida = EXIT_BUTTON
        self.salida = pygame.transform.scale(self.salida, (135, 58))

    def start(self):
        print("Credits state!")

    def run(self):
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                self.controller.quit()
            if self.salidaPos[0] <= x <= self.salidaPos[0] + self.salida.get_width():
                if self.salidaPos[1] <= y <= self.salidaPos[1] + self.salida.get_height():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.controller.change(State.MENU)
                        print("Salida")
        Scroll = True
        if Scroll == True and self.rect.y > -3500:
            self.clip(self.states)
            self.rect.y -= 5
        else:
            self.controller.change(State.MENU, None)
        self.image = self.bg.subsurface(self.bg.get_clip())

    def draw(self):
        self.win.blit(self.image, self.rect)
        self.clock.tick(20)
        self.win.blit(self.salida, self.salidaPos)
        pygame.display.update()

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.bg.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.bg.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect