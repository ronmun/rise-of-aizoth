import pygame


class Enemy:
    def __init__(self, x, y, rotated):
        self.posx = x
        self.posy = y
        self.rotation = rotated
        self.animation_count = 0
        self.clock = pygame.time.Clock()    #creo que no lo necesita, verificar

# modifcar la llamada de sprite movement
    def sprite_movement(self):
        self.animation_count += 0.09
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0

    def rotate(self):
        pass

    def draw(self):
        pass

    def draw_radius(self, win):
        # draw range circle
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)

        win.blit(surface, ((self.posx + 56) - self.range, (self.posy + 95) - self.range))