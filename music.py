import pygame
from pygame import mixer

class Music:
    def __init__(self):
        mixer.init()
        mixer.music.load("Assets/Music/Azureflux - Strike Witches Get Bitches.mp3")
        mixer.music.set_volume(.04)

    def playMusic(self):
        mixer.music.play(-1)

    def stopMusic(self):
        mixer.music.stop()
