import os

import pygame

pygame.font.init()
pygame.mixer.init()

# Window Properties
WIDTH, HEIGHT = 225, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Learn to Fly!")

# Movement Properties
STARTING_VELOCITY = 2

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# PYGAME FPS
FPS = 60

# Assets ------------------
BIRD_DOWN = pygame.image.load("assets/Bird_Down.png")
rect = BIRD_DOWN.get_rect()

OBS = pygame.Rect(30, 30, 80, 80)


# Wall Sprite Properties
WALLS_WIDTH, WALLS_HEIGHT = WIDTH, HEIGHT
WALLS_INITIAL_X, WALLS_INITIAL_Y = 0,0
WALLS_REPEAT_INITIAL_Y = HEIGHT
# Wall Sprite
SCROLLING_WALL = pygame.image.load(os.path.join('assets', 'Scrolling Walls.png'))
SCROLLING_WALL = pygame.transform.rotate(pygame.transform.scale(SCROLLING_WALL, (WALLS_WIDTH, WALLS_HEIGHT)), 0)
SCROLLING_WALL_REPEAT = pygame.transform.rotate(pygame.transform.scale(SCROLLING_WALL, (WALLS_WIDTH, WALLS_HEIGHT)), 0)


def obs_move_up(vel, walls,walls_repeat):
    if (walls.y <= -(WALLS_HEIGHT)):
        walls.y = WALLS_HEIGHT
    if (walls_repeat.y <= -(WALLS_HEIGHT)):
        walls_repeat.y = WALLS_HEIGHT

    walls.y -= vel
    walls_repeat.y -= vel


def draw_window(walls,walls_repeat):
    WIN.fill(WHITE)
    WIN.blit(SCROLLING_WALL,(WALLS_INITIAL_X,walls.y))  #x,y
    WIN.blit(SCROLLING_WALL_REPEAT,(WALLS_INITIAL_X,walls_repeat.y))

    WIN.blit(BIRD_DOWN, rect)

    if rect.colliderect(OBS):
        pygame.draw.rect(WIN, (100,200,0), OBS, 4)
        pygame.draw.rect(WIN, (0,200,180), rect, 4)
    else:
        pygame.draw.rect(WIN, (200,20,0), OBS, 4)

    pygame.display.update()

def main():
    # these are rects
    obstacle_branch = pygame.Rect(30,30, 10, 5)

    walls = pygame.Rect(WALLS_INITIAL_X, WALLS_INITIAL_Y, WALLS_WIDTH, WALLS_HEIGHT)
    walls_repeat = pygame.Rect(WALLS_INITIAL_X, WALLS_REPEAT_INITIAL_Y , WALLS_WIDTH, WALLS_HEIGHT)

    vel = STARTING_VELOCITY
    pVel = 6
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_LEFT]:
            rect.x -= pVel
        if userInput[pygame.K_RIGHT]:
            rect.x += pVel
        if userInput[pygame.K_UP]:
            rect.y -= pVel
        if userInput[pygame.K_DOWN]:
            rect.y += pVel

        obs_move_up(vel,walls,walls_repeat)
        draw_window(walls,walls_repeat)
        

    pygame.quit()


if __name__ == "__main__":
    main()


# # Border
# BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)



# # Movement Properties
# VELOCITY = 2

# # Sprite Properties







# def draw_window(walls):
#     WIN.blit(SCROLLING_WALL, (0, walls.x))

#     pygame.display.update()


# def obs_move_up(vel, walls):
#     walls.y -= vel

# def main():
#     WIN.fill(WHITE)
    
#     walls = pygame.Rect(700, 300, WALLS_WIDTH, WALLS_HEIGHT)



#     clock = pygame.time.Clock()
#     run = True
#     while run:
#         clock.tick(FPS)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#                 pygame.quit()

#         obs_move_up(VELOCITY, walls)

#         draw_window(walls)

#     main()


# if __name__ == "__main__":
#     main()