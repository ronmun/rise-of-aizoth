import pygame

from menu import MainMenu

WIDTH = 1280
HEIGHT = 720

if __name__ == "__main__":
	pygame.init()
	win = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption ('Rise of Aizoth')
	mainMenu = MainMenu(WIDTH, HEIGHT, win)
	mainMenu.run()
