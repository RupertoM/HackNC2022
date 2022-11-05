import os
from random import choice, randint

import pygame

from settings import *


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.width = 80 #BIRD_WIDTH
        self.height = 80 #BIRD_HEIGHT
        self.x = x #BIRD_INITIAL_X
        self.y = y #BIRD_INITIAL_Y