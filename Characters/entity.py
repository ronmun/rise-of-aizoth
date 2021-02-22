import math
import pygame
import os

ENTITY_WIDTH = 16
ENTITY_HEIGHT = 28
SCALE = 1.75
ORC_COST = 10
ELF_COST = 2
DINO_COST = 5
WIZARD_COST = 15

path2 = os.path.join("Assets/Sounds", "die.wav")

class Entity:
	def __init__(self, pos, path):
		self.width = ENTITY_WIDTH
		self.height = ENTITY_HEIGHT
		self.animation_count = 0
		self.health = 1
		self.vel = 1
		self.path = path
		self.x = pos[0]
		self.y = pos[1]
		self.img = None
		self.path_pos = 0
		self.move_count = 0
		self.imgs = []
		self.flipped = False
		self.max_health = 0
		self.arrived = False
		self.die_sound = pygame.mixer.Sound(path2)
		self.die_sound.set_volume(0.2)

	def draw (self, win):
		self.img = self.imgs[int(self.animation_count)]
		self.sprite_movement()
		win.blit (self.img, (self.x - self.img.get_width () / 2, self.y - self.img.get_height () / 2 - 35))

	def sprite_movement(self):
		self.animation_count += 0.09
		if self.animation_count >= len(self.imgs):
			self.animation_count = 0

	def flip(self):
		for x, img in enumerate(self.imgs):
			self.imgs[x] = pygame.transform.flip(img, True, False)


	def move (self):
		self.sprite_movement ()

		if self.path_pos + 1 > len(self.path):
			if self.path_pos == len(self.path):
				self.path_pos = 0
			x1, y1 = self.path[self.path_pos]
		else:
			x1, y1 = self.path[self.path_pos]


		if self.path_pos + 1 >= len (self.path):
			x2, y2 = self.path[0]
			self.arrived = True
		else:
			x2, y2 = self.path[self.path_pos + 1]

		dirn = ((x2-x1)*2, (y2-y1)*2)
		length = math.sqrt((dirn[0])**2 + (dirn[1])**2)
		dirn = (dirn[0]/length, dirn[1]/length)

		if dirn[0] < 0 and not(self.flipped):
			self.flipped = True
			self.flip()

		if dirn[0] > 0 and self.flipped:
			self.flipped = False
			self.flip()

		move_x, move_y = ((self.x + dirn[0]*self.vel), (self.y + dirn[1]*self.vel))

		self.x = move_x
		self.y = move_y
		# Go to next point
		if dirn[0] >= 0: # moving right
			if dirn[1] >= 0: # moving down
				if self.x >= x2 and self.y >= y2:
					self.path_pos += 1
			else:
				if self.x >= x2 and self.y <= y2:
					self.path_pos += 1

		else: # moving left
			if dirn[1] >= 0:  # moving down
				if self.x <= x2 and self.y >= y2:
					self.path_pos += 1
			else:
				if self.x <= x2 and self.y >= y2:
					self.path_pos += 1

	def hit(self, damage):
		self.health -= damage
		if self.health <= 0:
			self.die_sound.play()
			return True
		return False

	def draw_health_bar(self, win):
		length = 50
		move_by = round(length / self.max_health)
		health_bar = move_by * self.health

		pygame.draw.rect(win, (255, 0, 0), (self.x - 30, self.y - 75, length, 10), 0)
		pygame.draw.rect(win, (0, 255, 0), (self.x - 30, self.y - 75, health_bar, 10), 0)