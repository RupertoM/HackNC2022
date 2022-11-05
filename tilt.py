HOR_SPEED_TILT4 = 4.6
HOR_SPEED_TILT3 = 3.6
HOR_SPEED_TILT2 = 2.4
HOR_SPEED_TILT1 = 1.2

VERT_SPEED_TILT4 = 1
VERT_SPEED_TILT3 = 2
VERT_SPEED_TILT2 = 3
VERT_SPEED_TILT1 = 4
VERT_SPEED_DOWN = 5


def obs_move_up(vert_speed, walls,walls_repeat,WALLS_HEIGHT):
    if (walls.y <= -(WALLS_HEIGHT)):
        walls.y = WALLS_HEIGHT
    if (walls_repeat.y <= -(WALLS_HEIGHT)):
        walls_repeat.y = WALLS_HEIGHT
    walls.y -= vert_speed
    walls_repeat.y -= vert_speed

def bird_move_hor(hor_speed,bird):
    bird.x += hor_speed


def moving(direction,vel,walls,walls_repeat,WALLS_HEIGHT,bird):
    if (direction == -4):
        moving_l4(vel,walls,walls_repeat,WALLS_HEIGHT,bird)
    elif (direction == -3):
        moving_l3(vel,walls,walls_repeat,WALLS_HEIGHT,bird)
    elif (direction == -2):
        moving_l2(vel,walls,walls_repeat,WALLS_HEIGHT,bird)
    elif (direction == -1):
        moving_l1(vel,walls,walls_repeat,WALLS_HEIGHT,bird)
    elif (direction == 0):
        moving_d(vel,walls,walls_repeat,WALLS_HEIGHT,bird)
    elif (direction == 1):
        moving_r1(vel,walls,walls_repeat,WALLS_HEIGHT,bird)
    elif (direction == 2):
        moving_r2(vel,walls,walls_repeat,WALLS_HEIGHT,bird)
    elif (direction == 3):
        moving_r3(vel,walls,walls_repeat,WALLS_HEIGHT,bird)
    elif (direction == 4):
        moving_r4(vel,walls,walls_repeat,WALLS_HEIGHT,bird)

def moving_l4(vel,walls,walls_repeat,WALLS_HEIGHT,bird):
    hor_speed = -(HOR_SPEED_TILT4);
    vert_speed = VERT_SPEED_TILT4 * vel
    obs_move_up(vert_speed,walls,walls_repeat,WALLS_HEIGHT)
    bird_move_hor(hor_speed, bird)

def moving_l3(vel,walls,walls_repeat,WALLS_HEIGHT,bird):
    hor_speed = -(HOR_SPEED_TILT3);
    vert_speed = VERT_SPEED_TILT3 * vel
    obs_move_up(vert_speed,walls,walls_repeat,WALLS_HEIGHT)
    bird_move_hor(hor_speed, bird)

def moving_l2(vel,walls,walls_repeat,WALLS_HEIGHT,bird):
    hor_speed = -(HOR_SPEED_TILT2);
    vert_speed = VERT_SPEED_TILT2 * vel
    obs_move_up(vert_speed,walls,walls_repeat,WALLS_HEIGHT)
    bird_move_hor(hor_speed, bird)

def moving_l1(vel,walls,walls_repeat,WALLS_HEIGHT,bird):
    hor_speed = -(HOR_SPEED_TILT1);
    vert_speed = VERT_SPEED_TILT1 * vel
    obs_move_up(vert_speed,walls,walls_repeat,WALLS_HEIGHT)
    bird_move_hor(hor_speed, bird)

def moving_d(vel,walls,walls_repeat,WALLS_HEIGHT,bird):
    hor_speed = 0;
    vert_speed = VERT_SPEED_DOWN * vel
    obs_move_up(vert_speed,walls,walls_repeat,WALLS_HEIGHT)
    bird_move_hor(hor_speed, bird)
    
def moving_r1(vel,walls,walls_repeat,WALLS_HEIGHT,bird):
    hor_speed = HOR_SPEED_TILT1;
    vert_speed = VERT_SPEED_TILT1 * vel
    obs_move_up(vert_speed,walls,walls_repeat,WALLS_HEIGHT)
    bird_move_hor(hor_speed, bird)
    
def moving_r2(vel,walls,walls_repeat,WALLS_HEIGHT,bird):
    hor_speed = HOR_SPEED_TILT2;
    vert_speed = VERT_SPEED_TILT2 * vel
    obs_move_up(vert_speed,walls,walls_repeat,WALLS_HEIGHT)
    bird_move_hor(hor_speed, bird)

def moving_r3(vel,walls,walls_repeat,WALLS_HEIGHT,bird):
    hor_speed = HOR_SPEED_TILT3;
    vert_speed = VERT_SPEED_TILT3 * vel
    obs_move_up(vert_speed,walls,walls_repeat,WALLS_HEIGHT)
    bird_move_hor(hor_speed, bird)

def moving_r4(vel,walls,walls_repeat,WALLS_HEIGHT,bird):
    hor_speed = HOR_SPEED_TILT4;
    vert_speed = VERT_SPEED_TILT4 * vel
    obs_move_up(vert_speed,walls,walls_repeat,WALLS_HEIGHT)
    bird_move_hor(hor_speed, bird)

