import pygame
import os
pygame.init()


FPS = 60
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

ARROW_IMG = pygame.image.load(os.path.join('assets','arrow.png'))


SKYBLUE = (121,242,250)

class Player:
    def __init__(self,x,y):
        #movement
        self.x = x 
        self.y = y
    

def main():
    run = True
    while run: 
        WINDOW.fill(SKYBLUE)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                run = False
        pygame.display.update()

        keys = pygame.key.get_pressed()

    pygame.quit()

if __name__ == "__main__":
    main()