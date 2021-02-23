import os
import pygame

from Levels.levelstate import LevelState
from Levels.level import Level
from Enemies.towers import DemonTower, SkellyTower


class Rebelion (Level):
    def __init__(self, w, h, win, game):
        super ().__init__(w,h,win)
        self.bg = pygame.image.load(os.path.join("Assets/Sprites/Screens", "02_Rebelion.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.game = game
        self.max_gems = 200
        self.gems = self.max_gems
        self.start_pos = (-50, 140)
        self.end_pos = (850, 800)
        self.path = [(-50, 140), (370, 140), (370, 260), (565, 260), (565, 520), (850, 520), (850, 800)]

    def start(self):
        print("Rebelion Starts")
        self.enemies.append(DemonTower((575, 345), True))
        self.enemies.append(DemonTower((380, 80), True))
        self.enemies.append(SkellyTower((100, 100), True))
        self.enemies.append(SkellyTower((850, 345), True))
        self.enemies.append(SkellyTower((400, 250), False))

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
                        self.game.change(LevelState.ESPERANZA)
                elif self.level_ui.lost:
                    if self.level_ui.retryCheck(x, y):
                        self.game.change(LevelState.REBELION)

        self.character_movement()
        self.enemy_attacks()
        if not self.check_win():
            self.check_lose()