import pygame, random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.cactus import LargeCactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_TREE, LARGE_CACTUS, BAT, DAGGER_TYPE, HOURGLASS_TYPE


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                self.obstacles.append(Cactus(SMALL_TREE))
            elif random.randint(0, 2) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                self.obstacles.append(Bird(BAT))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
                elif game.player.has_power_up and game.player.type == DAGGER_TYPE:
                    self.obstacles.remove(obstacle)
                elif game.player.has_power_up and game.player.type == HOURGLASS_TYPE:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break     
                else:
                    game.playing = True

    def reset_obstacles(self):
        self.obstacles = []
        

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
