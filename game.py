import pygame

from screen import Screen
from state import State
from Levels.levelstate import LevelState
from Levels.pause import Pause

#Level loads
from Levels.tutorial import Tutorial
from Levels.rebelion import Rebelion
from Levels.esperanza import Esperanza

class Game (Screen):
	def __init__(self, w, h, win, controller):
		super().__init__(w, h, win)
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

		if state == LevelState.PAUSE:
			self.level = Pause (self.width, self.height, self.win, self.controller, self, self.level)
			self.level.start()

		if state != LevelState.PAUSE:
			self.fade()

	def reload_level(self, load_level):
		self.level = load_level

	def change_to_credits(self):
		self.controller.change(State.CREDITS)

	def fade(self):
		fade = pygame.Surface((self.width, self.height))
		fade.fill((50, 50, 50))
		for alpha in range(0, 300):
			fade.set_alpha(alpha)
			self.win.blit(fade, (0, 0))
			pygame.display.update()
			pygame.time.delay(5)

	def quit(self):
		self.controller.quit ()

	def run(self):
		self.level.run()
		self.draw()

	def draw(self):
		self.level.draw()
		pygame.display.update()