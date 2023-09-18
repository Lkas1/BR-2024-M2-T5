import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD, DAGGER_TYPE, DUCKING_DAGGER, JUMPING_DAGGER, RUNNING_DAGGER, HOURGLASS_TYPE

X_POS = 80
Y_POS = 300
JUMP_VEL = 8.5
Y_POS_DUCK = 320
Y_POS_DAGGER = 325

DUCK_IMG = { DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, DAGGER_TYPE: DUCKING_DAGGER, HOURGLASS_TYPE: DUCKING }
JUMP_IMG = { DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, DAGGER_TYPE: JUMPING_DAGGER, HOURGLASS_TYPE: JUMPING }
RUN_IMG = { DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD,DAGGER_TYPE: RUNNING_DAGGER, HOURGLASS_TYPE: RUNNING }

class Dinosaur(Sprite):
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.duck_index = 0
        self.jump_vel = JUMP_VEL
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.setup_state()

        self.jump_sound = pygame.mixer.Sound('dino_runner/assets/Sounds/JumpSound.ogg')
        self.jump_sound.set_volume(0.2)

    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.dagger = False
        self.hourglass = False
        self.show_text = False
        self.power_up_time = 0    

    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
            self.jump_sound.play()
        
            
            

        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_jump = False
            self.dino_run = False
            self.dino_duck = True
        elif not self.dino_jump and not self.dino_duck:
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck = False

        if self.type == DEFAULT_TYPE and self.step_index >= len(RUNNING):
            self.step_index = 0
        if self.type == DAGGER_TYPE and self.step_index >= len(RUNNING_DAGGER):
            self.step_index = 0
        if self.type == SHIELD_TYPE and self.step_index >= len(RUNNING_SHIELD):
            self.step_index = 0
        if self.type == HOURGLASS_TYPE and self.step_index >= len(RUNNING):
            self.step_index = 0
        
        if self.type == DEFAULT_TYPE and self.duck_index >= len(DUCKING):
            self.duck_index = 0
        if self.type == DAGGER_TYPE and self.duck_index >= len(DUCKING_DAGGER):
            self.duck_index = 0
        if self.type == SHIELD_TYPE and self.duck_index >= len(DUCKING_SHIELD):
            self.duck_index = 0
        if self.type == HOURGLASS_TYPE and self.duck_index >= len(DUCKING):
            self.duck_index = 0
        



    def run(self):        
        self.image = RUN_IMG[self.type][int(self.step_index)]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 0.3

        if self.type == DAGGER_TYPE:
            self.dino_rect.y = Y_POS_DAGGER


    def jump(self):
        self.image = JUMP_IMG[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL   
            

    def duck(self):
        self.image = DUCK_IMG[self.type][int(self.duck_index)]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS_DUCK
        self.duck_index += 0.3
        self.dino_duck = False

              
        
             

    def draw (self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))