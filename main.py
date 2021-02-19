import pygame

from controller import Controller
from state import State

WIDTH = 960
HEIGHT = 720

if __name__ == "__main__":
	pygame.init()
	win = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption ('Rise of Aizoth')

	controller = Controller (WIDTH, HEIGHT, win)
	controller.change (State.MENU, None)
	controller.run ()
