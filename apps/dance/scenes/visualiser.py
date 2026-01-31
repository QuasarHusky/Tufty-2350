import math
import random

name = "Visualiser"
auto_cycle = True

bar_count = 16
bar_width = math.ceil(screen.width / bar_count)
bar_targets = []
bar_values = []

for i in range(bar_count):
    bar_values.append(0)
    bar_targets.append(0)

def render_background():
    global bar_values

    screen.pen = color.rgb(100, 30, 110)
    screen.clear()

    decay_speed = io.ticks_delta / 1000 * 3

    for i in range(bar_count - 1):
        bar_values[i] -= (bar_values[i] - bar_values[i + 1]) * 0.3

    for i in range(1, bar_count):
        bar_values[i] -= (bar_values[i] - bar_values[i - 1]) * 0.3

    for i in range(bar_count):
        bar_values[i] = max(0, bar_values[i] - decay_speed)
        bar_values[i] = max(bar_values[i], random.random() * random.random())
        bar_targets[i] -= (bar_targets[i] - bar_values[i]) * 0.3

        render_bar(i)

def render_overlay():
    pass

def render_bar(i):
    height = max(2, math.floor(bar_targets[i] * bar_targets[i] * screen.height * 1.75))
    x = i * bar_width
    y = (screen.height - height) / 2

    screen.pen = color.rgb(183, 67, 232)
    screen.rectangle(x + 1, y, bar_width - 2, height)
