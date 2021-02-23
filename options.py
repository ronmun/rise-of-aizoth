import pygame
import os

from screen import Screen

BG_IMAGE = pygame.image.load(os.path.join("Assets/Sprites/Screens", "PantallaMenu.png"))
MUSICA_ON = pygame.image.load(os.path.join("Assets/Sprites/Screens/Botones", "musica_on.png"))
MUSICA_OFF = pygame.image.load(os.path.join("Assets/Sprites/Screens/Botones", "music_off.png"))
EXIT = pygame.image.load(os.path.join("Assets/Sprites/Screens/Botones", "exit.png"))

class Options(Screen):
    def __init__(self, w, h, win, controller, State):
        super().__init__(w, h, win)
        self.bg = BG_IMAGE
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.controller = controller
        self.win = win
        self.State = State
        self.musicOnPos = (450, 168)
        self.musicOffPos = (450, 296)
        self.exitPos = (450, 424)

        self.musicOn = MUSICA_ON
        self.musicOff = MUSICA_OFF
        self.exit = EXIT

        self.musicOn = pygame.transform.scale(self.musicOn, (180, 78))
        self.musicOff = pygame.transform.scale(self.musicOff, (180, 78))
        self.exit = pygame.transform.scale(self.exit, (180, 78))

    def draw(self):
        self.win.blit(self.bg, (0, 0))
        self.win.blit(self.musicOn, self.musicOnPos)
        self.win.blit(self.musicOff, self.musicOffPos)
        self.win.blit(self.exit, self.exitPos)
        pygame.display.update()

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.controller.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                self.musicOnCheck(x, y)
                self.musicOffCheck(x, y)
                self.exitCheck(x, y)

    def musicOnCheck(self, x, y):
        if self.musicOnPos[0] <= x <= self.musicOnPos[0] + self.musicOn.get_width():
            if self.musicOnPos[1] <= y <= self.musicOnPos[1] + self.musicOn.get_height():
                print("Music on")
                self.controller.music.play ()

    def musicOffCheck(self, x, y):
        if self.musicOffPos[0] <= x <= self.musicOffPos[0] + self.musicOff.get_width():
            if self.musicOffPos[1] <= y <= self.musicOffPos[1] + self.musicOff.get_height():
                print("Music off")
                self.controller.music.stop ()

    def exitCheck(self, x, y):
        if self.exitPos[0] <= x <= self.exitPos[0] + self.exit.get_width():
            if self.exitPos[1] <= y <= self.exitPos[1] + self.exit.get_height():
                print("exit")
                self.controller.reload_screen(self.State)

