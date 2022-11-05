import os
import pygame
from settings import *

# WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
# WIN.blit(yellow_health_text, (10, 10))


class Score(pygame.sprite.Sprite):
    def __init__(self, color, value):
        self.score = value
        SCORE_FONT = pygame.font.SysFont('comicsans', 40)
        self.score_sprite = SCORE_FONT.render(str(self.score), 1, color)
