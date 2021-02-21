from os import listdir
from os.path import isfile, join
import pygame
import os

from .entity import Entity, ENTITY_WIDTH, ENTITY_HEIGHT, SCALE, WIZARD_COST

path = os.path.join ("Assets/Sprites/Characters/Wizard")
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

class Wizard (Entity):
	def __init__(self, pos, path):
		super().__init__(pos, path)
		self.name = "wizard"
		self.cost = WIZARD_COST
		self.imgs = imgs[:]
		self.max_health = 8
		self.health = self.max_health
		self.vel = 1.25
		self.regen_timer = 0

	def regen(self):
		if self.health < self.max_health and int(self.regen_timer) == 5:
			if self.health + 2.5 > self.max_health:
				self.health = self.max_health
			else:
				self.health += 2.5
		self.regen_delay()

	def regen_delay(self):
		self.regen_timer += 0.025
		if self.regen_timer > 5.1:
			self.regen_timer = 0
