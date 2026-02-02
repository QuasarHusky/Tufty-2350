from badgeware import get_battery_level, is_charging
import math


def update():
    battery_level = get_battery_level()
    charging = is_charging()

    if not charging and battery_level <= 5: 
        render_battery_low()

def render_battery_low():
    if math.floor(io.ticks / 500) % 2 == 0:
        return

    phosphor = color.rgb(255, 50, 50)
    background = color.rgb(0, 0, 0)

    pos = (2, 2)
    size = (16, 8)

    screen.pen = background
    screen.shape(shape.rectangle(pos[0] - 2, pos[1] - 2, size[0] + 5, size[1] + 4))
    
    screen.pen = phosphor
    screen.shape(shape.rectangle(*pos, *size))
    screen.shape(shape.rectangle(pos[0] + size[0], pos[1] + 2, 1, 4))
    screen.pen = background
    screen.shape(shape.rectangle(pos[0] + 1, pos[1] + 1, size[0] - 2, size[1] - 2))

    screen.pen = phosphor
    screen.shape(shape.rectangle(pos[0] + 2, pos[1] + 2, 1, size[1] - 4))