import os
import pygame

from state import State
from screen import Screen
from Enemies.towers import DemonTower, SkellyTower
from Characters.elf import Elf
from Characters.dino import Dino
from Characters.orc import Orc
from Characters.wizard import Wizard
from Levels.levelstate import LevelState

voice = os.path.join("Assets/Sounds", "IntroAudio.wav")


class Cinematic(Screen):
    def __init__(self, w, h, win, controller):
        super().__init__(w, h, win)
        self.bg = pygame.image.load(os.path.join("Assets/Sprites/Screens", "Cinematic.png"))
        self.bg.set_clip(pygame.Rect(0, 0, 1080, 720))
        self.image = self.bg.subsurface(self.bg.get_clip())
        self.rect = self.image.get_rect()
        self.frame = 0
        self.states = {0: (0, 0, 2400, 720)}

        self.controller = controller
        self.clock = pygame.time.Clock()
        self.salidaPos = (940, 0)
        self.salida = pygame.image.load(os.path.join("Assets/Sprites/Screens/Botones", "exit.png"))
        self.salida = pygame.transform.scale(self.salida, (135, 58))

        self.intro_voice = pygame.mixer.Sound(voice)
        self.intro_voice.set_volume(0.5)

        self.enemies = []
        self.characters = []

    def start(self):
        print("Credits state!")
        self.fade()
        self.enemies.append(SkellyTower((1962, 135), True))
        self.enemies.append(DemonTower((2166, 185), True))
        self.enemies.append(SkellyTower((2285, 320), True))
        self.enemies.append(DemonTower((2042, 500), True))
        self.characters.append(Elf((1936,352), None))
        self.characters.append(Orc((2129,350), None))
        self.characters.append(Wizard((1879,502), None))
        self.characters.append(Dino((1935,434), None))
        self.characters.append(Elf((1900,300), None))
        self.characters.append(Orc((2100,450), None))
        self.characters.append(Wizard((1850,275), None))
        self.characters.append(Dino((1900,367), None))
        self.characters.append(Wizard((1800,407), None))
        self.characters.append(Orc((2100,450), None))
        self.characters.append(Wizard((1850,275), None))
        self.characters.append(Dino((1900,367), None))
        self.characters.append(Wizard((1800,407), None))
        self.characters.append(Dino((1900,467), None))
        self.characters.append(Elf((2100,400), None))
        self.characters.append(Orc((1940,500), None))
        self.characters.append(Orc((1920,400), None))
        self.characters.append(Wizard((1870,465), None))
        self.characters.append(Dino((1950,401), None))
        self.characters.append(Wizard((1990,375), None))
        self.characters.append(Wizard((1850,275), None))
        self.characters.append(Dino((2020,467), None))
        self.characters.append(Wizard((2240,497), None))
        self.characters.append(Orc((2100,510), None))
        self.characters.append(Wizard((2030,525), None))
        self.intro_voice.play()

    def run(self):
        for event in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                self.controller.quit()
            if self.salidaPos[0] <= x <= self.salidaPos[0] + self.salida.get_width():
                if self.salidaPos[1] <= y <= self.salidaPos[1] + self.salida.get_height():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.intro_voice.stop()
                        self.controller.change(State.GAME, None, LevelState.TUTORIAL)
                        print("Salida")
        Scroll = True
        if Scroll == True and self.rect.x > -2400+1080:
            self.clip(self.states)
            self.rect.x -= 3
        else:
            self.controller.change(State.GAME, None, LevelState.TUTORIAL)
        self.image = self.bg.subsurface(self.bg.get_clip())

    def draw(self):
        self.win.blit(self.image, self.rect)
        self.clock.tick(20)
        self.win.blit(self.salida, self.salidaPos)
        for enemy in self.enemies:
            if enemy.posx > -2400+1080:
                enemy.posx -=3
            enemy.draw(self.win)
        for character in self.characters:
            if enemy.posx > -2400+1080:
                character.x -=3
            character.draw(self.win)       
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

    def fade(self):
        fade = pygame.Surface((self.width, self.height))
        fade.fill((50, 50, 50))
        for alpha in range(0, 300):
            fade.set_alpha(alpha)
            self.win.blit(fade, (0, 0))
            pygame.display.update()
            pygame.time.delay(5)