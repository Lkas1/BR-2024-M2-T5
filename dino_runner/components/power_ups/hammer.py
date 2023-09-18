from dino_runner.utils.constants import DAGGER, DAGGER_TYPE
from dino_runner.components.power_ups.power_up import PowerUp

class Hammer(PowerUp):
    def __init__(self):
        self.image = DAGGER
        self.type = DAGGER_TYPE
        super().__init__(self.image, self.type)