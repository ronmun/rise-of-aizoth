import pygame

OFFSETX = 56
OFFSETY = 95

class Enemy:
    def __init__(self, pos, rotated):
        self.posx = pos[0]
        self.posy = pos[1]
        self.rotation = rotated
        self.animation_count = 0
        self.shoot_count = 0

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

        win.blit(surface, ((self.posx + OFFSETX) - self.range, (self.posy + OFFSETY) - self.range))

    def shoot_delay(self):
        self.shoot_count += 0.25
        if self.shoot_count > 5:
            self.shoot_count = 0