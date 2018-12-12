from sense_hat import SenseHat
sense = SenseHat()

slug = [[2,4],[3,4],[4,4]]
Blue = (0, 0, 255)

def draw_slug():
    for segment in slug:
        sense.set_pixel(segment[0], segment[1], Blue)
sense.clear()
draw_slug()

def move():
    last = slug[-1]
    first = slug[0]
    next = list (last)
    if direction ==  "right":
        if last[0] + 1 == 8:
            next[0] = 0
        else:
            next[0] = last[0] + 1
   
    elif direction == "left":
slug.append(next)

sense.set_pixel(next[0], next[1], Blue)

sense.set_pixel(first[0], first[1], blank)

slug.remove(first)

def joystick_moved(event):
    global direction
    direction = event.direction