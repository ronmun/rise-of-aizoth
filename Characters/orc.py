from os import listdir
from os.path import isfile, join
import pygame
import os

from .entity import Entity, SCALE, ORC_COST

ENTITY_WIDTH = 32
ENTITY_HEIGHT = 32

path = os.path.join ("Assets/Sprites/Characters/Orc")
files = [f for f in listdir (path) if isfile (join (path, f))]

imgs = []
for f in files:
	print (f)
	imgs.append (
		pygame.transform.scale (
			pygame.image.load (join (path, f)),
			(int(ENTITY_WIDTH*SCALE), int(ENTITY_HEIGHT*SCALE))
		)
	)

class Orc (Entity):
	def __init__(self, pos, path):
		super().__init__(pos, path)
		self.name = "orc"
		self.cost = ORC_COST
		self.imgs = imgs[:]
		self.max_health = 25
		self.health = self.max_health
		self.vel = 1
