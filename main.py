import os

import pygame

import tilt
from Bird import Bird
from settings import *

pygame.font.init()
pygame.mixer.init()


# Window Properties
WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Learn to Fly!")

# Movement Properties
STARTING_VARY_VELOCITY = 1
direction = 0

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Assets ------------------

# Wall Sprite Properties
WALLS_INITIAL_X, WALLS_INITIAL_Y = 0,0
WALLS_REPEAT_INITIAL_Y = WINDOW_HEIGHT

# Wall Sprite
BG_IMAGE = pygame.image.load(os.path.join('assets', 'background.png')).convert()
HEIGHT_SF = WINDOW_HEIGHT / (BG_IMAGE.get_height())
WIDTH_SF = WINDOW_WIDTH / (BG_IMAGE.get_width())
TRUE_HEIGHT = BG_IMAGE.get_height() * (HEIGHT_SF)
TRUE_WIDTH = BG_IMAGE.get_width() * WIDTH_SF
BG_WALL = pygame.transform.rotate(pygame.transform.scale(BG_IMAGE, (TRUE_WIDTH, TRUE_HEIGHT + 20)), 0)
BG_WALL_REPEAT = pygame.transform.rotate(pygame.transform.scale(BG_IMAGE, (TRUE_WIDTH, TRUE_HEIGHT + 20)), 0)

def bird_handle_movement(keys_pressed, direction):
    if keys_pressed[pygame.K_LEFT] and direction > -4:  # LEFT
        direction -= 1
    elif keys_pressed[pygame.K_RIGHT] and direction < 4: # RIGHT
        direction += 1
    return direction

def draw_window(walls,walls_repeat,birdRect, Bird):
    WIN.fill(WHITE)
    WIN.blit(BG_WALL,(WALLS_INITIAL_X,walls.y))  #x,y
    WIN.blit(BG_WALL_REPEAT,(WALLS_INITIAL_X,walls_repeat.y))
    
    if direction == -4:
        WIN.blit(Bird.left_4,(birdRect.x,Bird.y))
    elif direction == -3:
        WIN.blit(Bird.left_3,(birdRect.x,Bird.y))
    elif direction == -2:
        WIN.blit(Bird.left_2,(birdRect.x,Bird.y))
    elif direction == -1:
        WIN.blit(Bird.left_1,(birdRect.x,Bird.y))
    elif direction == 0:
        WIN.blit(Bird.down,(birdRect.x,Bird.y))
    elif direction == 1:
        WIN.blit(Bird.right_1,(birdRect.x,Bird.y))
    elif direction == 2:
        WIN.blit(Bird.right_2,(birdRect.x,Bird.y))
    elif direction == 3:
        WIN.blit(Bird.right_3,(birdRect.x,Bird.y))
    elif direction == 4:
        WIN.blit(Bird.right_4,(birdRect.x,Bird.y))
        
    pygame.display.update()

def main():
    global direction
    walls = pygame.Rect(WALLS_INITIAL_X, WALLS_INITIAL_Y, TRUE_WIDTH, TRUE_HEIGHT)
    walls_repeat = pygame.Rect(WALLS_INITIAL_X, WALLS_REPEAT_INITIAL_Y , TRUE_WIDTH, TRUE_HEIGHT)
    
    #Declare bird object
    BirdC = Bird((TRUE_WIDTH / 2.5),(TRUE_HEIGHT / 30))
    birdRect = pygame.Rect(BirdC.x, BirdC.y, BirdC.width, BirdC.height)

    v_vel = STARTING_VARY_VELOCITY
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        
        direction = bird_handle_movement(keys_pressed, direction)
        tilt.moving(direction,v_vel,walls,walls_repeat,TRUE_HEIGHT,birdRect)
        
        draw_window(walls,walls_repeat,birdRect,BirdC)
        

    pygame.quit()


if __name__ == "__main__":
    main()