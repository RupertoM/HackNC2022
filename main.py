import os

import pygame

import tilt
import Wall
import highscore
from Bird import Bird
from Score import Score
from settings import *
import csv



pygame.font.init()
pygame.mixer.init()

pygame.mixer.music.load(os.path.join('assets', 'music.mp3'))
pygame.mixer.music.play(-1)

#Game Over Tracker
game_over = False


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
SKY_BLUE = (135,206,235)

# Assets ------------------
# High Score


# Wall Sprite Properties
WALLS_INITIAL_X, WALLS_INITIAL_Y = 0,0
WALLS_REPEAT_INITIAL_Y = WINDOW_HEIGHT

# Wall Sprite
BG_IMAGE = pygame.image.load(os.path.join('assets', 'background.png'))
HEIGHT_SF = WINDOW_HEIGHT / (BG_IMAGE.get_height())
WIDTH_SF = WINDOW_WIDTH / (BG_IMAGE.get_width())
TRUE_HEIGHT = BG_IMAGE.get_height() * (HEIGHT_SF)
TRUE_WIDTH = BG_IMAGE.get_width() * WIDTH_SF
BG_WALL = pygame.transform.rotate(pygame.transform.scale(BG_IMAGE, (TRUE_WIDTH, TRUE_HEIGHT + 20)), 0)
BG_WALL_REPEAT = pygame.transform.rotate(pygame.transform.scale(BG_IMAGE, (TRUE_WIDTH, TRUE_HEIGHT + 20)), 0)

#Collision Rects for sides
L_side = pygame.Rect(0, 0, 1, WINDOW_HEIGHT)
R_side = pygame.Rect(WINDOW_WIDTH - 1,0,1,WINDOW_HEIGHT)


def bird_handle_movement(keys_pressed, direction,Score_Obj):
    if keys_pressed[pygame.K_LEFT] and direction > -4:  # LEFT
        direction -= 1
    elif keys_pressed[pygame.K_RIGHT] and direction < 4: # RIGHT
        direction += 1
    elif keys_pressed[pygame.K_SPACE]:
        Score_Obj.increment()
    return direction,Score_Obj

def draw_window(walls,walls_repeat,birdRect, Bird, Score_Obj, obs):
    WIN.fill(SKY_BLUE)
    WIN.blit(BG_WALL_REPEAT,(WALLS_INITIAL_X,walls_repeat.y))
    WIN.blit(BG_WALL,(WALLS_INITIAL_X,walls.y))
    
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

    tree_obs = pygame.image.load(os.path.join('assets','Tree_Branch.png'))
    flip = True

    for obstacle in obs:
        if flip:
            #pygame.draw.rect(WIN, (0,0,0), obstacle) #draw hitbox
            left_tree = pygame.transform.scale(tree_obs, (350,80))
            WIN.blit(left_tree, (obstacle.x, obstacle.y-20))
        else:
            pygame.draw.rect(WIN, (0,0,0), obstacle)
            right_tree_flip = pygame.transform.flip(tree_obs, True, False)
            right_tree = pygame.transform.scale(right_tree_flip, (350,80))
            WIN.blit(right_tree, (obstacle.x-40, obstacle.y-30))
        flip = (not flip)

        if birdRect.colliderect(obstacle):
            restart_game()
            

    #collision with wall state
    if birdRect.colliderect(L_side) or birdRect.colliderect(R_side):
        restart_game()
    #else:
        #pygame.draw.rect(WIN, (200,20,0), L_side)
        #pygame.draw.rect(WIN, (200,20,0), R_side)

    #Score Render
    WIN.blit(Score_Obj.score_sprite,(WINDOW_WIDTH/2 - 35,15))

    #Highscore Render
    highscore_font = pygame.font.SysFont('comicsans', 20)
    highscore_text = highscore_font.render("Highscore: " + str(highscore.get_highscore()), 1, YELLOW)
    WIN.blit(highscore_text, (0, 10))

    pygame.display.update()

def restart_game():
    global game_over
    game_over = True
    endgame_font = pygame.font.SysFont("arial", 60)
    restart_font = pygame.font.SysFont("arial", 20)
    #pygame.draw.rect(WIN, (100,200,0), L_side)
    #pygame.draw.rect(WIN, (100,200,0), R_side)
    GAME_OVER_TEXT = endgame_font.render("GAME OVER", True, BLACK, None)
    WIN.blit(GAME_OVER_TEXT, (WINDOW_WIDTH/2 - 170, WINDOW_HEIGHT/4))
    RESTART_TEXT = restart_font.render("PRESS SPACE TO TRY AGAIN", True, BLACK, None)
    WIN.blit(RESTART_TEXT, (WINDOW_WIDTH/2 - 130, WINDOW_HEIGHT/2))


    pygame.display.update()

    stop_game()


def unstop_game():
    global game_over
    game_over = False

def stop_game():
    global game_over
    while  game_over == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    unstop_game()
                    main()

def main():
    global direction

    obstacles = []

    obstacles = Wall.generate_walls(obstacles)

    walls = pygame.Rect(WALLS_INITIAL_X, WALLS_INITIAL_Y, TRUE_WIDTH, TRUE_HEIGHT)
    walls_repeat = pygame.Rect(WALLS_INITIAL_X, WALLS_REPEAT_INITIAL_Y , TRUE_WIDTH, TRUE_HEIGHT)
    
    #Declare bird object
    BirdC = Bird((TRUE_WIDTH / 2.5),(TRUE_HEIGHT / 10))
    birdRect = pygame.Rect(BirdC.x, BirdC.y, BirdC.width, BirdC.height)

    v_vel = STARTING_VARY_VELOCITY
    score_val = 0
    Score_Obj = Score(BLACK, score_val)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        

        keys_pressed = pygame.key.get_pressed()

        direction, Score_Obj = bird_handle_movement(keys_pressed, direction,Score_Obj)
        v_vel = 1 + Score_Obj.get_score() / 20
        highscore.set_highscore(Score_Obj.get_score())
        tilt.moving(direction,v_vel,walls,walls_repeat,TRUE_HEIGHT, birdRect, obstacles)
        
        draw_window(walls,walls_repeat,birdRect,BirdC, Score_Obj, obstacles)
        

    pygame.quit()


if __name__ == "__main__":
    main()