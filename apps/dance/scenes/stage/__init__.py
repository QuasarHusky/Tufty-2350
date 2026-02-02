import math

name = "Stage"
auto_cycle = True

light_colors = [
    color.rgb(255, 128, 128, 70),
    color.rgb(255, 255, 128, 70),
    color.rgb(128, 255, 128, 70),
    color.rgb(128, 255, 255, 70),
    color.rgb(128, 128, 255, 70),
    color.rgb(255, 128, 255, 70),
]

def render_background():
    screen.pen = color.rgb(100, 30, 110)
    screen.clear()

    screen.pen = color.rgb(80, 20, 90)
    screen.rectangle(0, math.floor(screen.height / 4 * 3), screen.width, math.ceil(screen.height / 4))

def render_overlay():
    light_cone = shape.pie(0, 0, screen.height * 2, 170, 190)

    transform = mat3().translate(20, -50).rotate(math.sin(io.ticks / 700) * 30 - 25)
    light_cone.transform = transform
    screen.pen = light_colors[math.floor(io.ticks / 1000) % len(light_colors)]
    screen.shape(light_cone)

    transform = mat3().translate(screen.width - 20, -50).rotate(math.cos(io.ticks / 700) * 30 + 25)
    light_cone.transform = transform
    screen.pen = light_colors[math.floor(io.ticks / 1000 + 3.5) % len(light_colors)]
    screen.shape(light_cone)

