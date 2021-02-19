import os
import pygame

from state import State

# screens
from menu import MainMenu
from game import Game
from credits import Credits

class Controller:
	def __init__(self, w, h, win):
		self.w = w
		self.h = h
		self.win = win
		self.screen = None
		self.running = True

	def change(self, state, lvl_to_load):
		if self.screen is not None:
			self.screen.end ()

		if state == State.MENU:
			self.screen = MainMenu (self.w, self.h, self.win, self)
			self.screen.start ()

		if state == State.GAME:
			self.screen = Game (self.w, self.h, self.win, self)
			self.screen.start (lvl_to_load)

		if state == State.CREDITS:
			self.screen = Credits (self.w, self.h, self.win, self)
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
