from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BAT

class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 210
        self.index = 0

    def draw(self, screen):
        if self.index >= len(BAT):
            self.index = 0
        screen.blit(self.image[self.index], self.rect)
        self.index += 1
        