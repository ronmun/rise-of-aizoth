import pygame

ENTITY_WIDTH = 16
ENTITY_HEIGHT = 28

class Entity:
	def __init__(self):
		self.width = ENTITY_WIDTH
		self.height = ENTITY_HEIGHT
		self.animation_count = 0
		self.health = 1
		self.vel = 3
		self.path = []
		self.x = 0
		self.y = 0
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
		# self.img = self.imgs[self.animation_count]
		# win.blit (self.img, (self.x - self.img.get_width () / 2, self.y - self.img.get_height () / 2 - 35))
		pass

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
		pass