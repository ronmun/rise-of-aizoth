from os import listdir
from os.path import isfile, join
import pygame

from .entity import Entity, ENTITY_WIDTH, ENTITY_HEIGHT

path = join ("Assets/Sprites/Characters/", "Elf")
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

class Elf (Entity):
	def __init__ (self):
		super ().__init__ ()
		self.name = "elf"
		self.money = 5
		self.imgs = imgs[:]
		self.max_health = 5
		self.health = self.max_health
