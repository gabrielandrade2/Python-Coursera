# template for "Stopwatch: The Game"

import simplegui

# define global variables
running = False
time = 0
points = 0
tries = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    #Separate the digits
    a = str(t / 600)
    b = str(t / 100 % 6)
    c = str(t / 10 % 10)
    d = str(t % 10)
    
    #Merges everything into one string
    return a + ":" + b + c + "." + d
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global running
    timer.start()
    running = True
    
def stop():
    global running, tries, points
    timer.stop()
    if(running):
        tries += 1
        if(time % 10 == 0):
            points += 1
    running = False

def reset():
    global running, time, points, tries
    timer.stop()
    running = False
    time = 0
    points = 0
    tries = 0     
    
# define event handler for timer with 0.1 sec interval
def timer():
    global time
    time += 1
   
# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), [70,120], 52 , "White")
    canvas.draw_text(str(points) + "/" + str(tries), [220,25], 24, "Green")
    
# create frame
frame = simplegui.create_frame('Stopwatch', 300, 200)

# register event handlers
timer = simplegui.create_timer(100,timer)
frame.set_draw_handler(draw)
startbtn = frame.add_button("Start", start, 150)
stopbtn = frame.add_button("Stop", stop, 150)
resetbtn = frame.add_button("Reset", reset, 150)

# start frame
frame.start()

# Please remember to review the grading rubric
