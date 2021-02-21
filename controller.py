import os
import pygame

from state import State

# screens
from menu import MainMenu
from game import Game
from credits import Credits
from options import Options
from pause import Pause

from music import Music

class Controller:
	def __init__(self, w, h, win):
		self.w = w
		self.h = h
		self.win = win
		self.screen = None
		self.running = True
		self.music = Music ()
		self.music.play ()

	def change(self, state, origin_state = None, lvl_to_load = None):
		if self.screen is not None:
			self.screen.end ()

		if state == State.MENU:
			self.screen = MainMenu (self.w, self.h, self.win, self)
			self.screen.start ()

		if state == State.GAME and lvl_to_load is not None:
			self.screen = Game (self.w, self.h, self.win, self)
			self.screen.start (lvl_to_load)

		if state == State.CREDITS:
			self.screen = Credits (self.w, self.h, self.win, self)
			self.screen.start ()

		if state == State.OPCIONES and origin_state is not None:
			self.screen = Options (self.w, self.h, self.win, self, self.screen)
			self.screen.start ()

		if state == State.PAUSE and origin_state is not None:
			self.screen = Pause (self.w, self.h, self.win, self, self.screen)
			self.screen.start ()

	def reload_screen(self, load_screen):
		self.screen = load_screen

	def quit(self):
		self.running = False

	def run(self):
		clock = pygame.time.Clock()
		while self.running:
			self.screen.run ()
			self.screen.draw ()

			clock.tick(60)

		pygame.quit()
