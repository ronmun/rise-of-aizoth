import pygame, random

class AttackParticle:
    def __init__(self):
        self.particles = []

    def emit(self, win, color):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                particle[0][1] += particle[2][0]
                particle[0][0] += particle[2][1]
                particle[1] -= 0.2
                pygame.draw.circle(win,color,particle[0], int(particle[1]))

    def add_particles(self, pos):
        pos_x = pos[0]
        pos_y = pos[1]
        radius = 3
        direction_x = random.randint(-3,3)
        direction_y = random.randint(-3,3)
        particle_circle = [[pos_x,pos_y],radius,[direction_x,direction_y]]
        self.particles.append(particle_circle)

    def delete_particles(self):
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy