import os
from random import choice, randint
import random

import pygame

from settings import *


def generate_walls(obs): #method for generating obstacles
    obs = []

    i = 0
    local = 590

    while i < 60:
        obstacle = pygame.Rect(0,local + 600,300,1)
        obstacle2 = pygame.Rect(300,local + 850,300,1)

        obs.append(obstacle)
        obs.append(obstacle2)

        local += 500
        i += 1

    return obs