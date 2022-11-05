import pygame
import os
import tilt

pygame.font.init()
pygame.mixer.init()


# Window Properties
WIDTH, HEIGHT = 225, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Learn to Fly!")

# Movement Properties
STARTING_VARY_VELOCITY = 1
direction = 0

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# PYGAME FPS
FPS = 30

# Assets ------------------
# Bird Sprite Properties
BIRD_WIDTH, BIRD_HEIGHT = 100, 100
BIRD_INITIAL_X, BIRD_INITIAL_Y = 112,40
# BIRD SPRITE
BIRD_TILT_1 = pygame.image.load(os.path.join('assets','Bird_Tilt_1.png'))
BIRD_TILT_2 = pygame.image.load(os.path.join('assets','Bird_Tilt_2.png'))
BIRD_TILT_3 = pygame.image.load(os.path.join('assets','Bird_Tilt_3.png'))
BIRD_TILT_4 = pygame.image.load(os.path.join('assets','Bird_Tilt_4.png'))

BIRD_RIGHT_1 = pygame.transform.flip(pygame.transform.rotate(pygame.transform.scale(BIRD_TILT_1, (BIRD_WIDTH, BIRD_HEIGHT)), 0),0,0)
BIRD_LEFT_1 = pygame.transform.flip(pygame.transform.rotate(pygame.transform.scale(BIRD_TILT_1, (BIRD_WIDTH, BIRD_HEIGHT)), 0),1,0)

BIRD_RIGHT_2 = pygame.transform.flip(pygame.transform.rotate(pygame.transform.scale(BIRD_TILT_2, (BIRD_WIDTH, BIRD_HEIGHT)), 0),0,0)
BIRD_LEFT_2 = pygame.transform.flip(pygame.transform.rotate(pygame.transform.scale(BIRD_TILT_2, (BIRD_WIDTH, BIRD_HEIGHT)), 0),1,0)

BIRD_RIGHT_3 = pygame.transform.flip(pygame.transform.rotate(pygame.transform.scale(BIRD_TILT_3, (BIRD_WIDTH, BIRD_HEIGHT)), 0),0,0)
BIRD_LEFT_3 = pygame.transform.flip(pygame.transform.rotate(pygame.transform.scale(BIRD_TILT_3, (BIRD_WIDTH, BIRD_HEIGHT)), 0),1,0)

BIRD_RIGHT_4 = pygame.transform.flip(pygame.transform.rotate(pygame.transform.scale(BIRD_TILT_4, (BIRD_WIDTH, BIRD_HEIGHT)), 0),0,0)
BIRD_LEFT_4 = pygame.transform.flip(pygame.transform.rotate(pygame.transform.scale(BIRD_TILT_4, (BIRD_WIDTH, BIRD_HEIGHT)), 0),1,0)

BIRD_DOWN = pygame.image.load(os.path.join('assets','Bird_Down.png'))
BIRD_DOWN = pygame.transform.rotate(pygame.transform.scale(BIRD_DOWN, (BIRD_WIDTH, BIRD_HEIGHT)), 0)

# Wall Sprite Properties
WALLS_WIDTH, WALLS_HEIGHT = WIDTH, HEIGHT
WALLS_INITIAL_X, WALLS_INITIAL_Y = 0,0
WALLS_REPEAT_INITIAL_Y = HEIGHT
# Wall Sprite
SCROLLING_WALL = pygame.image.load(os.path.join('assets', 'Scrolling Walls.png'))
SCROLLING_WALL = pygame.transform.rotate(pygame.transform.scale(SCROLLING_WALL, (WALLS_WIDTH, WALLS_HEIGHT)), 0)
SCROLLING_WALL_REPEAT = pygame.transform.rotate(pygame.transform.scale(SCROLLING_WALL, (WALLS_WIDTH, WALLS_HEIGHT)), 0)

def bird_handle_movement(keys_pressed, direction):
    if keys_pressed[pygame.K_a] and direction > -4:  # LEFT
        direction -= 1
    elif keys_pressed[pygame.K_d] and direction < 4: # RIGHT
        direction += 1
    return direction


def draw_window(walls,walls_repeat,bird):
    WIN.fill(WHITE)
    WIN.blit(SCROLLING_WALL,(WALLS_INITIAL_X,walls.y))  #x,y
    WIN.blit(SCROLLING_WALL_REPEAT,(WALLS_INITIAL_X,walls_repeat.y))
    if direction == -4:
        WIN.blit(BIRD_LEFT_4,(bird.x,BIRD_INITIAL_Y))
    elif direction == -3:
        WIN.blit(BIRD_LEFT_3,(bird.x,BIRD_INITIAL_Y))
    elif direction == -2:
        WIN.blit(BIRD_LEFT_2,(bird.x,BIRD_INITIAL_Y))
    elif direction == -1:
        WIN.blit(BIRD_LEFT_1,(bird.x,BIRD_INITIAL_Y))
    elif direction == 0:
        WIN.blit(BIRD_DOWN,(bird.x,BIRD_INITIAL_Y))
    elif direction == 1:
        WIN.blit(BIRD_RIGHT_1,(bird.x,BIRD_INITIAL_Y))
    elif direction == 2:
        WIN.blit(BIRD_RIGHT_2,(bird.x,BIRD_INITIAL_Y))
    elif direction == 3:
        WIN.blit(BIRD_RIGHT_3,(bird.x,BIRD_INITIAL_Y))
    elif direction == 4:
        WIN.blit(BIRD_RIGHT_4,(bird.x,BIRD_INITIAL_Y))
        
    pygame.display.update()

def main():
    global direction
    walls = pygame.Rect(WALLS_INITIAL_X, WALLS_INITIAL_Y, WALLS_WIDTH, WALLS_HEIGHT)
    walls_repeat = pygame.Rect(WALLS_INITIAL_X, WALLS_REPEAT_INITIAL_Y , WALLS_WIDTH, WALLS_HEIGHT)
    bird = pygame.Rect(BIRD_INITIAL_X,BIRD_INITIAL_Y,BIRD_WIDTH,BIRD_HEIGHT)

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
        tilt.moving(direction,v_vel,walls,walls_repeat,WALLS_HEIGHT,bird)
        
        draw_window(walls,walls_repeat,bird)
        

    pygame.quit()


if __name__ == "__main__":
    main()