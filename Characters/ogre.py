from os import listdir
from os.path import isfile, join
import pygame
import os

from .entity import Entity, SCALE

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

class Ogre (Entity):
	def __init__ (self, x, y):
		super ().__init__ (x, y)
		self.name = "ogre"
		self.money = 5
		self.imgs = imgs[:]
		self.max_health = 5
		self.health = self.max_health
		self.vel = 0.75
