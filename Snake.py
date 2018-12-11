slug = [[2,4] + [3,4] + [4,4]]
Blue = (0, 0, 255)
def draw_slug():
    for segment in slug:
        sense.set_pixel(segment[0], segment[1], Blue)
sense.clear()
draw_slug()
