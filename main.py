import pygame
import os

from controller import Controller
from state import State

WIDTH = 1080
HEIGHT = 720
ICON = pygame.image.load(os.path.join("Assets/Sprites", "Icon.png"))

if __name__ == "__main__":
	pygame.init()
	win = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption ('Rise of Aizoth')
	pygame.display.set_icon(ICON)

	controller = Controller (WIDTH, HEIGHT, win)
	controller.change (State.MENU)
	controller.run ()
