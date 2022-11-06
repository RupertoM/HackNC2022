HOR_SPEED_TILT4 = 4.6
HOR_SPEED_TILT3 = 3.6
HOR_SPEED_TILT2 = 2.4
HOR_SPEED_TILT1 = 1.2

VERT_SPEED_TILT4 = 1
VERT_SPEED_TILT3 = 2
VERT_SPEED_TILT2 = 3
VERT_SPEED_TILT1 = 4
VERT_SPEED_DOWN = 5

VERTICAL_SPEED = 0


def obs_move_up(vert_speed, walls,walls_repeat,WALLS_HEIGHT, obstacles):
    global VERTICAL_SPEED
    if (walls.y <= -(WALLS_HEIGHT)):
        walls.y = WALLS_HEIGHT
    if (walls_repeat.y <= -(WALLS_HEIGHT)):
        walls_repeat.y = WALLS_HEIGHT
    VERTICAL_SPEED = vert_speed
    walls.y -= vert_speed * 1.1
    walls_repeat.y -= vert_speed

    for obstacle in obstacles:
        obstacle.y -= vert_speed

def bird_move_hor(hor_speed,bird):
    bird.x += hor_speed


def moving(direction,vel,walls,walls_repeat,WALLS_HEIGHT, bird, obstacles):
    if (direction == -4):
        moving_l4(vel,walls,walls_repeat,WALLS_HEIGHT,bird, obstacles)
    elif (direction == -3):
        moving_l3(vel,walls,walls_repeat,WALLS_HEIGHT,bird, obstacles)
    elif (direction == -2):
        moving_l2(vel,walls,walls_repeat,WALLS_HEIGHT,bird, obstacles)
    elif (direction == -1):
        moving_l1(vel,walls,walls_repeat,WALLS_HEIGHT,bird, obstacles)
    elif (direction == 0):
        moving_d(vel,walls,walls_repeat,WALLS_HEIGHT,bird, obstacles)
    elif (direction == 1):
        moving_r1(vel,walls,walls_repeat,WALLS_HEIGHT,bird, obstacles)
    elif (direction == 2):
        moving_r2(vel,walls,walls_repeat,WALLS_HEIGHT,bird, obstacles)
    elif (direction == 3):
        moving_r3(vel,walls,walls_repeat,WALLS_HEIGHT,bird, obstacles)
    elif (direction == 4):
        moving_r4(vel,walls,walls_repeat,WALLS_HEIGHT,bird, obstacles)

    return VERTICAL_SPEED

def moving_l4(vel,walls,walls_repeat,WALLS_HEIGHT,bird, obstacles):
    hor_speed = -(HOR_SPEED_TILT4) * vel
    vert_speed = VERT_SPEED_TILT4 * vel
    obs_move_up(vert_speed,walls,walls_repeat,WALLS_HEIGHT, obstacles)
    bird_move_hor(hor_speed, bird)

def moving_l3(vel,walls,walls_repeat,WALLS_HEIGHT,bird, obstacles):
    hor_speed = -(HOR_SPEED_TILT3) * vel
    vert_speed = VERT_SPEED_TILT3 * vel
    obs_move_up(vert_speed,walls,walls_repeat,WALLS_HEIGHT, obstacles)
    bird_move_hor(hor_speed, bird)

def moving_l2(vel,walls,walls_repeat,WALLS_HEIGHT,bird, obstacles):
    hor_speed = -(HOR_SPEED_TILT2) * vel
    vert_speed = VERT_SPEED_TILT2 * vel
    obs_move_up(vert_speed,walls,walls_repeat,WALLS_HEIGHT, obstacles)
    bird_move_hor(hor_speed, bird)

def moving_l1(vel,walls,walls_repeat,WALLS_HEIGHT,bird, obstacles):
    hor_speed = -(HOR_SPEED_TILT1) * vel
    vert_speed = VERT_SPEED_TILT1 * vel
    obs_move_up(vert_speed,walls,walls_repeat,WALLS_HEIGHT, obstacles)
    bird_move_hor(hor_speed, bird)

def moving_d(vel,walls,walls_repeat,WALLS_HEIGHT,bird, obstacles):
    hor_speed = 0 * vel
    vert_speed = VERT_SPEED_DOWN * vel
    obs_move_up(vert_speed,walls,walls_repeat,WALLS_HEIGHT, obstacles)
    bird_move_hor(hor_speed, bird)
    
def moving_r1(vel,walls,walls_repeat,WALLS_HEIGHT,bird, obstacles):
    hor_speed = HOR_SPEED_TILT1 * vel
    vert_speed = VERT_SPEED_TILT1 * vel
    obs_move_up(vert_speed,walls,walls_repeat,WALLS_HEIGHT, obstacles)
    bird_move_hor(hor_speed, bird)
    
def moving_r2(vel,walls,walls_repeat,WALLS_HEIGHT,bird, obstacles):
    hor_speed = HOR_SPEED_TILT2 * vel
    vert_speed = VERT_SPEED_TILT2 * vel
    obs_move_up(vert_speed,walls,walls_repeat,WALLS_HEIGHT, obstacles)
    bird_move_hor(hor_speed, bird)

def moving_r3(vel,walls,walls_repeat,WALLS_HEIGHT,bird, obstacles):
    hor_speed = HOR_SPEED_TILT3 * vel
    vert_speed = VERT_SPEED_TILT3 * vel
    obs_move_up(vert_speed,walls,walls_repeat,WALLS_HEIGHT, obstacles)
    bird_move_hor(hor_speed, bird)

def moving_r4(vel,walls,walls_repeat,WALLS_HEIGHT,bird, obstacles):
    hor_speed = HOR_SPEED_TILT4 * vel
    vert_speed = VERT_SPEED_TILT4 * vel
    obs_move_up(vert_speed,walls,walls_repeat,WALLS_HEIGHT, obstacles)
    bird_move_hor(hor_speed, bird)

