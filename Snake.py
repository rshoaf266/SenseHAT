from sense_hat import SenseHat
sense = SenseHat()
from time import *

slug = [[2,4],[3,4],[4,4]]
blue = (0, 0, 255)
blank = (0, 0, 0)
direction = "right"


def draw_slug():
    for segment in slug:
        sense.set_pixel(segment[0], segment[1], blue)
        


def move():
    last = slug[-1]
    first = slug[0]
    next = list(last)
    if direction == "right":
        next[0] = last[0] + 1
    slug.append(next)
    sense.set_pixel(next[0], next[1], blue)
    sense.set_pixel(first[0], first[1], blank)
    slug.remove(first)
    '''
    if direction ==  "right":
        if last[0] + 1 == 8:
            next[0] = 0
        else:
            next[0] = last[0] + 1
    elif direction == "left":
        if last[0] - 1 == -1:
            next[0] = 7
        else:
            next[0] = last[0] - 1 
    elif direction == "down":
        if last[1] + 1 == 8:
            next[1] = 0
        else:
            next[1] = last[1] + 1
    elif direction == "up":
        if last[1] - 1 == -1:
            next[1] = 7
        else:
            next[1] = last[1] - 1
    '''
    
def joystick_moved(event):
    global direction
    direction = event.direction
        
sense.stick.direction_any = joystick_moved

sense.clear()
draw_slug()

while True:
    "move"


    