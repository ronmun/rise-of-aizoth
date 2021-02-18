import os
import pygame

class MainMenu:
	def __init__(self, w, h, win):
		self.width = w
		self.height = h
		self.win = win
		self.bg = pygame.image.load (os.path.join ("Assets/Sprites/Screens", "PantallaMenu.png"))
		self.bg = pygame.transform.scale (self.bg, (self.width, self.height))
		self.title = pygame.image.load (os.path.join ("Assets/Sprites/Screens", "GameTitle.png")).convert_alpha()

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
		self.win.blit(self.bg, (0,0))
		self.win.blit(self.title, (self.width / 2 - self.title.get_width() / 2, 120))
		pygame.display.update()