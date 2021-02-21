import math
import pygame

ENTITY_WIDTH = 16
ENTITY_HEIGHT = 28
SCALE = 1.75

class Entity:
	def __init__(self, x, y):
		self.width = ENTITY_WIDTH
		self.height = ENTITY_HEIGHT
		self.animation_count = 0
		self.health = 1
		self.vel = 3
		self.path = [(-50, 200), (780, 200), (780, 560), (180, 560), (180, 775)]
		self.x = x
		self.y = y
		self.img = None
		self.dis = 0
		self.path_pos = 0
		self.move_count = 0
		self.move_dis = 0
		self.imgs = []
		self.flipped = False
		self.max_health = 0
		self.speed_increase = 1.2

	def draw (self, win):
		self.img = self.imgs[int(self.animation_count)]
		self.sprite_movement()
		win.blit (self.img, (self.x - self.img.get_width () / 2, self.y - self.img.get_height () / 2 - 35))

	def sprite_movement(self):
		self.animation_count += 0.09
		if self.animation_count >= len(self.imgs):
			self.animation_count = 0

	def collide (self, X, Y):
		"""
		Returns if position has hit the entity
		:param x: int
		:param y: int
		:return: Bool
		"""
		if X <= self.x + self.width and X >= self.x:
			if Y <= self.y + self.height and Y >= self.y:
				return True
		return False

	def move (self):
		self.sprite_movement ()

		x1, y1 = self.path[self.path_pos]
		if self.path_pos + 1 >= len (self.path):
			x2, y2 = (0,0 )
		else:
			x2, y2 = self.path[self.path_pos + 1]

		dirn = ((x2-x1)*2, (y2-y1)*2)
		length = math.sqrt((dirn[0])**2 + (dirn[1])**2)
		dirn = (dirn[0]/length, dirn[1]/length)

		if dirn[0] < 0 and not(self.flipped):
			self.flipped = True
			for x, img in enumerate(self.imgs):
				self.imgs[x] = pygame.transform.flip(img, True, False)

		move_x, move_y = ((self.x + dirn[0]), (self.y + dirn[1]))

		self.x = move_x
		self.y = move_y
		print ("x " + str (self.x) + " - y " + str (self.y))

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