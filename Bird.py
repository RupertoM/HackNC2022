import os
from random import choice, randint

import pygame

from settings import *


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.width = 80 #BIRD_WIDTH
        self.height = 80 #BIRD_HEIGHT
        self.x = x #BIRD_INITIAL_X
        self.y = y #BIRD_INITIAL_Y

        #Tilt attributes
        self.T1 = pygame.image.load(os.path.join('assets','Bird_Tilt_1.png')) #BIRD_TILT_1
        self.T2 = pygame.image.load(os.path.join('assets','Bird_Tilt_2.png'))
        self.T3 = pygame.image.load(os.path.join('assets','Bird_Tilt_3.png'))
        self.T4 = pygame.image.load(os.path.join('assets','Bird_Tilt_4.png'))

        #Directional attirbutes
        #previously BIRD_RIGHT_1 and BIRD_LEFT_1
        self.right_1 = pygame.transform.flip(pygame.transform.rotate(pygame.transform.scale(self.T1, (self.width, self.height)), 0),0,0)
        self.left_1 = pygame.transform.flip(pygame.transform.rotate(pygame.transform.scale(self.T1, (self.width, self.height)), 0),1,0)

        #previously BIRD_RIGHT_2 and BIRD_LEFT_2
        self.right_2 = pygame.transform.flip(pygame.transform.rotate(pygame.transform.scale(self.T2, (self.width, self.height)), 0),0,0)
        self.left_2 = pygame.transform.flip(pygame.transform.rotate(pygame.transform.scale(self.T2, (self.width, self.height)), 0),1,0)
        
        #previously BIRD_RIGHT_3 and BIRD_LEFT_3
        self.right_3 = pygame.transform.flip(pygame.transform.rotate(pygame.transform.scale(self.T3, (self.width, self.height)), 0),0,0)
        self.left_3 = pygame.transform.flip(pygame.transform.rotate(pygame.transform.scale(self.T3, (self.width, self.height)), 0),1,0)
        
        #previously BIRD_RIGHT_4 and BIRD_LEFT_4
        self.right_4 = pygame.transform.flip(pygame.transform.rotate(pygame.transform.scale(self.T4, (self.width, self.height)), 0),0,0)
        self.left_4 = pygame.transform.flip(pygame.transform.rotate(pygame.transform.scale(self.T4, (self.width, self.height)), 0),1,0)
        
        
        #previously BIRD DOWN
        BIRD_DOWN_SURFACE = pygame.image.load(os.path.join('assets','Bird_Down.png'))
        self.down = pygame.transform.rotate(pygame.transform.scale(BIRD_DOWN_SURFACE, (self.width, self.height)), 0)