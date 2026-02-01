import math

TOP = 1
BOTTOM = 2

SHORT = 1000
LONG = 4000

toast_text = ""
toast_lifetime = 0
toast_position = TOP

def show(text, duration=SHORT, position=TOP):
    global toast_text, toast_lifetime, toast_position
    toast_text = text
    toast_lifetime = duration
    toast_position = position

def clear():
    global toast_lifetime
    toast_lifetime = 0

def update():
    global toast_lifetime

    if toast_lifetime > 0:
        toast_lifetime -= io.ticks_delta
        render()

def render():
    width, height = screen.measure_text(toast_text)
    x = math.floor((screen.width - width) / 2)

    if toast_position == TOP:
        y = 5
    elif toast_position == BOTTOM:
        y = screen.height - height - 5

    screen.pen = color.rgb(0, 0, 0, 192)
    screen.rectangle(x - 4, y - 2, width + 8, height + 4)

    screen.pen = color.rgb(255, 255, 255)
    screen.text(toast_text, x, y)