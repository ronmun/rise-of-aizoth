import pygame


class Enemy:
    def __init__(self, x, y, rotated):
        self.posx = x
        self.posy = y
        self.rotation = rotated
        self.animation_count = 0
        self.clock = pygame.time.Clock()

# modifcar la llamada de sprite movement
    def sprite_movement(self):
        self.animation_count += 0.09
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0

    def rotate(self):
        pass

    def draw(self):
        pass