from os import listdir
from os.path import isfile, join
import pygame

from .entity import Entity, ENTITY_WIDTH, ENTITY_HEIGHT

path = join ("Assets/Sprites/Characters/", "Dino")
files = [f for f in listdir (path) if isfile (join (path, f))]

imgs = []
for f in files:
	print (f)
	imgs.append (
		pygame.transform.scale (
			pygame.image.load (join (path, f)).convert_alpha (),
			(ENTITY_WIDTH, ENTITY_HEIGHT)
		)
	)

class Dino (Entity):
	def __init__ (self):
		super ().__init__ ()
		self.name = "dino"
		self.money = 5
		self.imgs = imgs[:]
		self.max_health = 5
		self.health = self.max_health
