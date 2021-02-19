import os
import pygame

from state import State
from screen import Screen

class Credits(Screen):
    def __init__(self, w, h, win, controller):
        super().__init__(w, h, win)
        self.bg = pygame.image.load(os.path.join("Assets/Sprites/Screens", "CreditsBg.png"))
        self.bg.set_clip(pygame.Rect(0, 0, 1024, 760))
        self.image = self.bg.subsurface(self.bg.get_clip())
        self.rect = self.image.get_rect()
        self.frame = 0
        self.states = { 0: (0, 0, 1024, 3828) }

        self.controller = controller
        self.clock = pygame.time.Clock()

        
    def start(self):
        print("Credits state!")

        
    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.controller.quit()
        e=5
        if e == 5:
            self.clip(self.states)
            self.rect.y -= 5
        self.image = self.bg.subsurface(self.bg.get_clip())
        
    def draw(self):
        self.win.blit(self.image, self.rect)
        self.clock.tick(20)
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

    
        