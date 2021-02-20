import os
import pygame

from screen import Screen

class Game (Screen):
	def __init__(self, w, h, win, controller):
		self.width = w
		self.height = h
		self.win = win
		self.bg = pygame.image.load (os.path.join ("Assets/Sprites/Screens", "PantallaMenu.png"))
		self.bg = pygame.transform.scale (self.bg, (self.width, self.height))
		self.controller = controller

	def start(self):
		print ("Game state!")

	def run(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.controller.quit ()

	def draw(self):
		self.win.blit(self.bg, (0,0))
		pygame.display.update()