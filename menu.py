import pygame
import os

class MainMenu:
	def __init__(self, w, h, win):
		self.width = w
		self.height = h
		self.win = win
		self.bg = None
		# self.bg = pygame.transform.scale(self.bg, (self.width, self.height))

	def run(self):
		run = True

		clock = pygame.time.Clock()
		while run:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False

				if event.type == pygame.MOUSEBUTTONUP:
					# check if hit start btn
					x, y = pygame.mouse.get_pos()
					# TODO: init game

			self.draw()

			clock.tick(60)

		pygame.quit()

	def draw(self):
		# TODO: draw sprites
		# self.win.blit(self.bg, (0,0))
		pygame.display.update()