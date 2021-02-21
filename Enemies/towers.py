import pygame
import math
import os
from os import listdir
from os.path import isfile, join
import pygame

from Enemies.enemy import Enemy, OFFSETX, OFFSETY

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
	def __init__(self, pos, rotated):
		super().__init__(pos, rotated)
		self.nombre = "Demon Tower"
		self.imgs = imgs[:]
		self.damage = 2
		self.range = 200
		self.rotate()

	def attack(self, allies):

		ally_closest = []
		for ally in allies:
			x = ally.x
			y = ally.y

			try:
				dis = math.sqrt(((self.posx + OFFSETX) - ally.img.get_width()/2 - x)**2 + ((self.posy + OFFSETY) - ally.img.get_height()/2 - y)**2)
				if dis < self.range:
					ally_closest.append(ally)
			except:
				pass

		ally_closest.sort(key=lambda x: x.path_pos)
		ally_closest = ally_closest[::-1]
		if len(ally_closest) > 0:
			first_ally = ally_closest[0]
			if int(self.shoot_count) == 5:
				if first_ally.hit(self.damage) == True:
					allies.remove(first_ally)

			"""
			Aqui se puede hacer un flip, preguntando si la x de ally pasó la x + mitad de al torre
			"""

	def rotate(self):
		if self.rotation == True:
			i = 0
			while i < len(self.imgs):
				self.imgs[i] = pygame.transform.flip(self.imgs[i],True,False)
				i += 1

	def draw(self, win):
		#super().draw_radius(win)
		self.shoot_delay()
		img = self.imgs[int(self.animation_count)]
		self.sprite_movement()
		win.blit(img, (self.posx, self.posy))



class SkellyTower (Enemy):
	def __init__(self, pos, rotated):
		super().__init__(pos, rotated)
		self.nombre = "Skelly Tower"
		self.imgs = imgs2[:]
		self.damage = 1
		self.range = 150
		self.rotate()

	def attack(self, allies):

		ally_closest = []
		for ally in allies:
			x = ally.x
			y = ally.y

			try:
				dis = math.sqrt(((self.posx + OFFSETX) - ally.img.get_width() / 2 - x) ** 2 + (
							(self.posy + OFFSETY) - ally.img.get_height() / 2 - y) ** 2)
				if dis < self.range:
					ally_closest.append(ally)
			except:
				pass

		ally_closest.sort(key=lambda x: x.path_pos)
		ally_closest = ally_closest[::-1]
		if len(ally_closest) > 0:
			first_ally = ally_closest[0]
			if int(self.shoot_count) == 5:
				if first_ally.hit(self.damage) == True:
					allies.remove(first_ally)

			"""
			Aqui se puede hacer un flip, preguntando si la x de ally pasó la x + mitad de al torre
			"""

	def rotate(self):
		if self.rotation == True:
			i = 0
			while i < len(self.imgs):
				self.imgs[i] = pygame.transform.flip(self.imgs[i],True,False)
				i += 1

	def draw(self, win):
		#super().draw_radius(win)
		self.shoot_delay()
		img = self.imgs[int(self.animation_count)]
		self.sprite_movement()
		win.blit(img, (self.posx, self.posy))