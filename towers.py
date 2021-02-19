import pygame
import math
import os
from os import listdir
from os.path import isfile, join
import pygame

path = os.path.join ("Assets/Sprites/Characters/DemonTower")
sprites = [f for f in listdir (path) if isfile (join (path, f))]

path2 = os.path.join ("Assets/Sprites/Characters/SkellyTower")
sprites2 = [f for f in listdir (path2) if isfile (join (path2, f))]

imgs = []
for i in sprites:
	imgs.append(pygame.transform.scale(pygame.image.load (os.path.join (path, i)),(16, 28)))

imgs2 = []
for i in sprites2:
	imgs.append(pygame.transform.scale(pygame.image.load (os.path.join (path2, i)),(16, 28)))

class DemonTower ():
	def __init__(self):
		self.nombre = "Demon Tower"
		self.imgs = imgs[:]
		self.damage = 3
		self.range = 20
		self.posx = 0
		self.posy = 0
		self.animation_count = 0

#modifcar la llamada de sprite movement
	def sprite_movement(self):
		self.animation_count += 1
		if self.animation_count > len(self.imgs):
			self.animation_count = 0

	def draw(self, win, x, y, rotation):

		if rotation == True:
			self.imgs[self.animation_count] = pygame.transform.flip(self.imgs[self.animation_count])

		img = self.imgs[self.animation_count]
		win.blit(img, (x, y))





	"""def posicion_torre (self, opc, win):
		if opc == 1:
			self.posx = self.posx + 1
			self.posy = self.posy + 1

			DemonTower.draw(win, self.posx, self.posy)

		if opc == 2:
			self.posx = self.posx + 2
			self.posy = self.posy + 2

			DemonTower.draw(win, self.posx, self.posy)

			self.posx = self.posx + 2
			self.posy = self.posy + 2

			DemonTower.draw(win, self.posx, self.posy)

		if opc == 3:
			self.posx = self.posx + 3
			self.posy = self.posy + 3

			DemonTower.draw(win, self.posx, self.posy)

			self.posx = self.posx + 3
			self.posy = self.posy + 3

			DemonTower.draw(win, self.posx, self.posy)

class SkellyTower ():
	def __init__(self):
		self.nombre = "Skelly Tower"
		self.imgs2 = imgs2[:]
		self.damage = 3
		self.range = 20
		self.posx = 1
		self.posy = 1

	def draw(self, win, x, y):

		img = self.imgs2[:]
		win.blit(img, (x, y))

	def posicion_torre(self, opc, win):
		if opc == 1:
			self.posx = self.posx + 1
			self.posy = self.posy + 1

			DemonTower.draw(win, self.posx, self.posy)

		if opc == 2:
			self.posx = self.posx + 2
			self.posy = self.posy + 2

			DemonTower.draw(win, self.posx, self.posy)

			self.posx = self.posx + 2
			self.posy = self.posy + 2

			DemonTower.draw(win, self.posx, self.posy)

		if opc == 3:
			self.posx = self.posx + 3
			self.posy = self.posy + 3

			DemonTower.draw(win, self.posx, self.posy)

			self.posx = self.posx + 3
			self.posy = self.posy + 3

			DemonTower.draw(win, self.posx, self.posy)
	"""