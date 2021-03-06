import pygame
import math
import os
from os import listdir
from os.path import isfile, join

from Enemies.enemy import Enemy, OFFSETX, OFFSETY
from Enemies.particles import AttackParticle

path = os.path.join ("Assets/Sprites/Characters/DemonTower")
sprites = [f for f in listdir (path) if isfile (join (path, f))]

path2 = os.path.join ("Assets/Sprites/Characters/SkellyTower")
sprites2 = [f for f in listdir (path2) if isfile (join (path2, f))]

path3 = os.path.join("Assets/Sounds", "shoot.wav")


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
		self.particles = AttackParticle()
		self.shoot_sound = pygame.mixer.Sound(path3)
		self.shoot_sound.set_volume(0.05)

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
				self.particles_ON = True
				self.shoot_sound.play()
				if first_ally.hit(self.damage) == True:
					allies.remove(first_ally)

		if self.particles_ON and int(self.shoot_count) == 4:
			self.particles_ON = False


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
		if self.particles_ON:
			self.particles.add_particles((self.posx + OFFSETX, self.posy + OFFSETY-15))
			self.particles.emit(win,pygame.Color('Yellow'))



class SkellyTower (Enemy):
	def __init__(self, pos, rotated):
		super().__init__(pos, rotated)
		self.nombre = "Skelly Tower"
		self.imgs = imgs2[:]
		self.damage = 1
		self.range = 150
		self.rotate()
		self.particles = AttackParticle()
		self.shoot_sound = pygame.mixer.Sound(path3)
		self.shoot_sound.set_volume(0.1)

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
				self.particles_ON = True
				self.shoot_sound.play()
				if first_ally.hit(self.damage) == True:
					allies.remove(first_ally)

		if self.particles_ON and int(self.shoot_count) == 4:
			self.particles_ON = False


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
		if self.particles_ON:
			self.particles.add_particles((self.posx + OFFSETX, self.posy + OFFSETY-15))
			self.particles.emit(win,(214,74,255))