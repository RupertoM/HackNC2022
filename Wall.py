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
        if ((i % 10) == 0) and (i != 0):
            obstacle = pygame.Rect(-100,local + 600,300,1)
            obstacle2 = pygame.Rect(400,local + 600,300,1)

            obstacle3 = pygame.Rect(-100,local + 700,300,1)
            obstacle4 = pygame.Rect(400,local + 700,300,1)

            obstacle5 = pygame.Rect(-100,local + 800,300,1)
            obstacle6 = pygame.Rect(400,local + 800,300,1)

            obstacle7 = pygame.Rect(-100,local + 900,300,1)
            obstacle8 = pygame.Rect(400,local + 900,300,1)


            obs.append(obstacle)
            obs.append(obstacle2)
            obs.append(obstacle3)
            obs.append(obstacle4)
            obs.append(obstacle5)
            obs.append(obstacle6)
            obs.append(obstacle7)
            obs.append(obstacle8)
            local += 400

        else:
            obstacle = pygame.Rect(0,local + 600,300,1)
            obstacle2 = pygame.Rect(300,local + 850,300,1)

            obs.append(obstacle)
            obs.append(obstacle2)

        local += 500
        i += 1

    return obs