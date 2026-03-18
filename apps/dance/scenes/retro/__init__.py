import math

from visualiser import FakeVisualiser

name = "Retro"
auto_cycle = True

visualiser = FakeVisualiser(12)
bar_width = math.ceil(screen.width / visualiser.bar_count)

def render_background():
    screen.pen = color.rgb(0, 0, 0)
    screen.clear()

    visualiser.update()

    for i in range(visualiser.bar_count):
        render_bar(i, visualiser.get_bar(i))

def render_overlay():
    pass

def render_bar(i, value):
    height = math.floor(value * screen.height * 2.5) + 10
    x = i * bar_width - 4

    for j in range(0, screen.height, 10):
        t = j / screen.height
        active = j <= height

        if t < 0.4:
            if active:
                screen.pen = color.rgb(40, 200, 40)
            else:
                screen.pen = color.rgb(10, 50, 10)
        elif t < 0.75:
            if active:
                screen.pen = color.rgb(200, 200, 40)
            else:
                screen.pen = color.rgb(50, 50, 10)
        else:
            if active:
                screen.pen = color.rgb(200, 40, 40)
            else:
                screen.pen = color.rgb(50, 10, 10)

        y = screen.height - j - 9

        screen.rectangle(x + 1, y, bar_width - 2, 8)
        
