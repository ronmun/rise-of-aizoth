import os
import pygame

from state import State

# screens
from menu import MainMenu
from game import Game

class Controller:
	def __init__(self, w, h, win):
		self.w = w
		self.h = h
		self.win = win
		self.screen = None
		self.running = True

	def change(self, state):
		if self.screen is not None:
			self.screen.end ()

		if state == State.MENU:
			self.screen = MainMenu (self.w, self.h, self.win, self)
			self.screen.start ()

		if state == State.GAME:
			self.screen = Game (self.w, self.h, self.win, self)
			self.screen.start ()

	def quit(self):
		self.running = False

	def run(self):
		clock = pygame.time.Clock()
		while self.running:
			self.screen.run ()
			self.screen.draw ()

			clock.tick(60)

		pygame.quit()
