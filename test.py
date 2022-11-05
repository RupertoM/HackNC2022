import pygame
import os
from pygame.locals import *

WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Testing Caption")

ARROW_IMG = pygame.image.load(os.path.join('img','arrow.png' ))

FPS = 60
SKYBLUE = (121,242,250)
RED = (229,25,25)

class Player:
    def __init__(self,x,y):
        #movement
        self.x = x 
        self.y = y


def draw_window():
    WINDOW.fill(SKYBLUE)
    WINDOW.blit(SMILE, (SMILE.x,SMILE.y))
    pygame.display.update()
    

def main():

    run = True
    clock = pygame.time.Clock()

    while run: 
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                run = False
        draw_window()
        

    pygame.quit()

if __name__ == "__main__":
    main()