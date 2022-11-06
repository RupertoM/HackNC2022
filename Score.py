import pygame

from settings import *


class Score():
    def __init__(self, color, value):
        self.score = value
        SCORE_FONT = pygame.font.SysFont('impact', 40)
        self.score_sprite = SCORE_FONT.render(three_digit(self.score), 1, color)

    def increment(self):
        self.score += 1
        SCORE_FONT = pygame.font.SysFont('impact', 40)
        self.score_sprite = SCORE_FONT.render(three_digit(self.score), 1, (0,0,0))
    def get_score(self):
        return self.score


def three_digit(number):
    
    if len(str(number)) == 1:
        return "00" + str(number)
    
    elif len(str(number)) == 2:
        return "0" + str(number)
    
    else:
        return str(number)