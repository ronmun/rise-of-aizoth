import pygame
import os

LEVEL_01 = pygame.image.load(os.path.join("Assets/Sprites/Screens/Botones", "Nivel_1.png"))
LEVEL_02 = pygame.image.load(os.path.join("Assets/Sprites/Screens/Botones", "Nivel_2.png"))
LEVEL_03 = pygame.image.load(os.path.join("Assets/Sprites/Screens/Botones", "Nivel_3.png"))
OPCIONES = pygame.image.load(os.path.join("Assets/Sprites/Screens/Botones", "opciones.png"))
CREDITOS = pygame.image.load(os.path.join("Assets/Sprites/Screens/Botones", "creditos.png"))
SALIDA = pygame.image.load(os.path.join("Assets/Sprites/Screens/Botones", "exit.png"))

class MenuUi:
    def __init__(self, win):
        self.win = win
        self.level1Pos = (450, 300)
        self.level2Pos = (450, 403)
        self.level3Pos = (450, 506)
        self.opcionesPos = (450, 609)
        self.creditosPos = (50, 609)
        self.salidaPos = (850, 609)
        self.level1 = LEVEL_01
        self.level2 = LEVEL_02
        self.level3 = LEVEL_03
        self.opciones = OPCIONES
        self.creditos = CREDITOS
        self.salida = SALIDA

        self.level1 = pygame.transform.scale(self.level1, (180, 78))
        self.level2 = pygame.transform.scale(self.level2, (180, 78))
        self.level3 = pygame.transform.scale(self.level3, (180, 78))
        self.opciones = pygame.transform.scale(self.opciones, (180, 78))
        self.creditos = pygame.transform.scale(self.creditos, (180, 78))
        self.salida = pygame.transform.scale(self.salida, (180, 78))

    def draw(self):
        self.win.blit(self.level1, self.level1Pos)
        self.win.blit(self.level2, self.level2Pos)
        self.win.blit(self.level3, self.level3Pos)
        self.win.blit(self.opciones, self.opcionesPos)
        self.win.blit(self.creditos, self.creditosPos)
        self.win.blit(self.salida, self.salidaPos)


    def level1Check(self, x, y):
        if self.level1Pos[0] <= x <= self.level1Pos[0] + self.level1.get_width():
            if self.level1Pos[1] <= y <= self.level1Pos[1] + self.level1.get_height():
                print("Level1")
                return True
        return False

    def level2Check(self, x, y):
        if self.level2Pos[0] <= x <= self.level2Pos[0] + self.level2.get_width():
            if self.level2Pos[1] <= y <= self.level2Pos[1] + self.level2.get_height():
                print("Level2")
                return True
        return False

    def level3Check(self, x, y):
        if self.level3Pos[0] <= x <= self.level3Pos[0] + self.level3.get_width():
            if self.level3Pos[1] <= y <= self.level3Pos[1] + self.level3.get_height():
                print("Level3")
                return True
        return False

    def opcionesCheck(self, x, y):
        if self.opcionesPos[0] <= x <= self.opcionesPos[0] + self.opciones.get_width():
            if self.opcionesPos[1] <= y <= self.opcionesPos[1] + self.opciones.get_height():
                print("Opciones")
                return True
        return False

    def creditosCheck(self, x, y):
        if self.creditosPos[0] <= x <= self.creditosPos[0] + self.creditos.get_width():
            if self.creditosPos[1] <= y <= self.creditosPos[1] + self.creditos.get_height():
                print("Creditos")
                return True
        return False

    def salidaCheck(self, x, y):
        if self.salidaPos[0] <= x <= self.salidaPos[0] + self.salida.get_width():
            if self.salidaPos[1] <= y <= self.salidaPos[1] + self.salida.get_height():
                print("Salida")
                return True
        return False
