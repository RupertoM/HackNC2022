import os
from random import choice, randint

import pygame

from settings import *


def generate_walls(obs): #method for generating obstacles
    obs = []

    i = 0
    local = 590

    while i < 20:
        obstacle = pygame.Rect(0,local + 590,300,30)
        obstacle2 = pygame.Rect(300,local + 800,300,30)

        obs.append(obstacle)
        obs.append(obstacle2)

        local += 400
        i += 1

    return obs
    
"""
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.width = 80
        self.height = 80
        self.x = x #BIRD_INITIAL_X
        self.y = y #BIRD_INITIAL_Y
"""