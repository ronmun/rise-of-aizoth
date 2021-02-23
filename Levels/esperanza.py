import os
import pygame

from Levels.levelstate import LevelState
from Levels.level import Level
from Enemies.towers import DemonTower, SkellyTower

class Esperanza (Level):
    def __init__(self, w, h, win, game):
        super ().__init__(w,h,win)
        self.bg = pygame.image.load(os.path.join("Assets/Sprites/Screens", "03_Esperanza.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.game = game
        self.max_gems = 300
        self.gems = self.max_gems
        self.start_pos = (-50, 150)
        self.end_pos = (-30, 650)
        self.path = [(-50, 140), (490, 140), (490, 310), (850, 310), (850, 530), (330, 530), (330, 670), (230, 670), (230, 645), (-50, 645)]

    def start(self):
        print("Esperanza Starts")
        self.enemies.append(DemonTower((300, 125), True))
        self.enemies.append(DemonTower((550, 50), True))
        self.enemies.append(DemonTower((500, 300), True))
        self.enemies.append(DemonTower((700, 300), False))
        self.enemies.append(DemonTower((500, 520), False))
        self.enemies.append(SkellyTower((220,500), False))

        self.initial_troop()

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.quit()

            if event.type == pygame.MOUSEBUTTONUP:
                # check if hit start btn
                x, y = pygame.mouse.get_pos()
                if self.level_ui.pauseCheck(x, y):
                    self.game.change(LevelState.PAUSE)
                print(x, y)

                self.check_character_buy(x, y)

                if self.level_ui.won:
                    if self.level_ui.nextCheck(x, y):
                        self.game.change_to_credits()
                if self.level_ui.lost:
                    if self.level_ui.retryCheck(x, y):
                        self.game.change(LevelState.ESPERANZA)

        self.character_movement()
        self.enemy_attacks()
        if not self.check_win():
            self.check_lose()