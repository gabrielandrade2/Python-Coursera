# Implementation of classic arcade game Pong

import simplegui
import random
import math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

PAD_SPEED = 15

paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    v0 = random.randrange(5, 6)
    v1 = random.randrange(3, 5)
    if(direction):#If it is right
        ball_vel = [v0, -v1]
    else:
        ball_vel = [-v0, -v1]
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball(RIGHT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw scores
    canvas.draw_text(str(score1),[140,50],45,"White")
    canvas.draw_text(str(score2),[440,50],45,"White")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    #Check collision TOP DOWN
    if(ball_pos[1] <= BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
    elif(ball_pos[1] >= HEIGHT - BALL_RADIUS - 1):
        ball_vel[1] = -ball_vel[1]
        
    #Check collision gutter and then check for the paddler
    if(ball_pos[0] <= PAD_WIDTH + BALL_RADIUS):
        if((ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT) and (ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT)):
            ball_vel[0] = -ball_vel[0] * 1.10
        else:
            score2 += 1
            spawn_ball(RIGHT)
    elif(ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS - 1):
        if((ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT) and (ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT)):
            ball_vel[0] = -ball_vel[0] * 1.10
        else:
            score1 += 1
            spawn_ball(LEFT)
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    if(paddle1_pos <= HALF_PAD_HEIGHT):
        paddle1_pos = HALF_PAD_HEIGHT
    elif(paddle1_pos >= HEIGHT - HALF_PAD_HEIGHT -1):
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT -1
    
    if(paddle2_pos <= HALF_PAD_HEIGHT):
        paddle2_pos = HALF_PAD_HEIGHT
    elif(paddle2_pos >= HEIGHT - HALF_PAD_HEIGHT -1):
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT -1
    
    # draw paddles
    canvas.draw_polygon([[0,paddle1_pos + HALF_PAD_HEIGHT], [0,paddle1_pos - HALF_PAD_HEIGHT],[PAD_WIDTH,paddle1_pos - HALF_PAD_HEIGHT],[PAD_WIDTH,paddle1_pos + HALF_PAD_HEIGHT]],1,"White","White")
    canvas.draw_polygon([[WIDTH - PAD_WIDTH - 1,paddle2_pos - HALF_PAD_HEIGHT],[WIDTH - 1,paddle2_pos - HALF_PAD_HEIGHT],[WIDTH ,paddle2_pos + HALF_PAD_HEIGHT],[WIDTH - PAD_WIDTH - 1,paddle2_pos + HALF_PAD_HEIGHT]],1,"White","White")   
                     
    
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if(key == simplegui.KEY_MAP["w"]):
       paddle1_vel += -PAD_SPEED
    if(key == simplegui.KEY_MAP["s"]):
        paddle1_vel += PAD_SPEED
    if(key == simplegui.KEY_MAP["up"]):
        paddle2_vel += -PAD_SPEED
    if(key == simplegui.KEY_MAP["down"]):
        paddle2_vel += PAD_SPEED
       
def keyup(key):
    global paddle1_vel, paddle2_vel
    if(key == simplegui.KEY_MAP["w"]):
        paddle1_vel += PAD_SPEED
    if(key == simplegui.KEY_MAP["s"]):
        paddle1_vel += -PAD_SPEED
    if(key == simplegui.KEY_MAP["up"]):
        paddle2_vel += PAD_SPEED
    if(key == simplegui.KEY_MAP["down"]):
        paddle2_vel += -PAD_SPEED
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button = frame.add_button("Reset",new_game,100)

# start frame
new_game()
frame.start()
