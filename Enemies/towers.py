import pygame
import math
import os
from os import listdir
from os.path import isfile, join
import pygame

from Enemies.enemy import Enemy

path = os.path.join ("Assets/Sprites/Characters/DemonTower")
sprites = [f for f in listdir (path) if isfile (join (path, f))]

path2 = os.path.join ("Assets/Sprites/Characters/SkellyTower")
sprites2 = [f for f in listdir (path2) if isfile (join (path2, f))]

#Escala original de las imagenes es 64x80
imgs = []
for i in sprites:
	imgs.append(pygame.transform.scale(pygame.image.load (os.path.join (path, i)),(112, 140)))

imgs2 = []
for i in sprites2:
	imgs2.append(pygame.transform.scale(pygame.image.load (os.path.join (path2, i)),(112, 140)))

class DemonTower (Enemy):
	def __init__(self, x, y, rotated):
		super().__init__(x, y, rotated)
		self.nombre = "Demon Tower"
		self.imgs = imgs[:]
		self.damage = 3
		self.range = 20
		self.rotate()

	def rotate(self):
		if self.rotation == True:
			i = 0
			while i < len(self.imgs):
				self.imgs[i] = pygame.transform.flip(self.imgs[i],True,False)
				i += 1

	def draw(self, win):
		img = self.imgs[self.animation_count]
		win.blit(img, (self.posx, self.posy))



class SkellyTower (Enemy):
	def __init__(self, x, y, rotated):
		super().__init__(x, y, rotated)
		self.nombre = "Skelly Tower"
		self.imgs = imgs2[:]
		self.damage = 3
		self.range = 20
		self.rotate()

	def rotate(self):
		if self.rotation == True:
			i = 0
			while i < len(self.imgs):
				self.imgs[i] = pygame.transform.flip(self.imgs[i],True,False)
				i += 1

	def draw(self, win):
		img = self.imgs[self.animation_count]
		win.blit(img, (self.posx, self.posy))