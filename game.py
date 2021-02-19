import pygame
import os

from screen import Screen
from Levels.levelstate import LevelState

#Level loads
from Levels.tutorial import Tutorial
from Levels.rebelion import Rebelion
from Levels.esperanza import Esperanza

class Game (Screen):
	def __init__(self, w, h, win, controller):
		self.width = w
		self.height = h
		self.win = win

		self.controller = controller
		self.level = None

	def start(self, lvl_to_load):
		print ("Game state!")
		if lvl_to_load == LevelState.TUTORIAL:
			self.change(LevelState.TUTORIAL)

		if lvl_to_load == LevelState.REBELION:
			self.change(LevelState.REBELION)

		if lvl_to_load == LevelState.ESPERANZA:
			self.change(LevelState.ESPERANZA)

	def change(self, state):
		if self.level is not None:
			self.level.end ()

		if state == LevelState.TUTORIAL:
			self.level = Tutorial (self.width, self.height, self.win, self)
			self.level.start ()

		if state == LevelState.REBELION:
			self.level = Rebelion (self.width, self.height, self.win, self)
			self.level.start ()

		if state == LevelState.ESPERANZA:
			self.level = Esperanza (self.width, self.height, self.win, self)
			self.level.start ()

	def quit(self):
		self.controller.quit ()


	def run(self):
		self.level.run()
		self.draw()

	def draw(self):
		self.level.draw()
		pygame.display.update()