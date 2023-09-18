import pygame
import os

# Global Constants
TITLE = "Goblin Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Character/tile001.png"))
DEAD_GOBLIN = pygame.image.load(os.path.join(IMG_DIR, "Other/DeadCharacter.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Character/tile000.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Character/tile001.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Character/tile002.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Character/tile003.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Character/tile004.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Character/tile005.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Character/tile006.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Character/tile007.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Character/tile000_shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Character/tile001.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Character/tile002_shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Character/tile003.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Character/tile004_shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Character/tile005.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Character/tile006_shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Character/tile007.png")),
]

RUNNING_DAGGER = [
    pygame.image.load(os.path.join(IMG_DIR, "Character/tile002_dagger.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Character/tile001_dagger.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Character/tile003_jump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Character/tile003_shield.png"))
JUMPING_DAGGER = pygame.image.load(os.path.join(IMG_DIR, "Character/tile003_jump_dagger.png"))

DUCKING = pygame.image.load(os.path.join(IMG_DIR, "Character/tile001_duck.png")),

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Character/tile001_duck_shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Character/tile001_duck.png")),
]

DUCKING_DAGGER = [
    pygame.image.load(os.path.join(IMG_DIR, "Character/tile001_duck_dagger.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Character/tile001_duck.png")),
]

SMALL_TREE = [
    pygame.image.load(os.path.join(IMG_DIR, "Background/Trees/SmallTree.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Background/Trees/SmallTree2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Background/Trees/SmallTree3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
    
]

BAT = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/bat1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/bat2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/bat3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/bat4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/bat5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/bat6.png")),
]

BG1 = pygame.image.load(os.path.join(IMG_DIR, 'Background/1.png'))
MOON = pygame.image.load(os.path.join(IMG_DIR, 'Background/2.png'))
CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Background/3.png'))
CLOUD2 = pygame.image.load(os.path.join(IMG_DIR, 'Background/4.png'))
GROUND = pygame.image.load(os.path.join(IMG_DIR, 'Background/ground.png'))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
DAGGER = pygame.image.load(os.path.join(IMG_DIR, 'Other/dagger.png'))
HOURGLASS = pygame.image.load(os.path.join(IMG_DIR, 'Hourglass/Hourglass.png'))

#BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
DAGGER_TYPE = "dagger"
HOURGLASS_TYPE = "hourglass"