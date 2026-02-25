import math

from visualiser import FakeVisualiser

name = "Visualiser"
auto_cycle = True

visualiser = FakeVisualiser(16)
bar_width = math.ceil(screen.width / visualiser.bar_count)

def render_background():
    global bar_values

    screen.pen = color.rgb(100, 30, 110)
    screen.clear()

    visualiser.update()

    for i in range(visualiser.bar_count):
        render_bar(i, visualiser.get_bar(i))

def render_overlay():
    pass

def render_bar(i, value):
    height = max(2, math.floor(value * screen.height * 1.75))
    x = i * bar_width
    y = (screen.height - height) / 2

    screen.pen = color.rgb(183, 67, 232)
    screen.rectangle(x + 1, y, bar_width - 2, height)
