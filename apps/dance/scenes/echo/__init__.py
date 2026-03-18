name = "Echo"
auto_cycle = False

def render_background():
    screen.pen = color.rgb(0, 0, 0, 10)
    screen.rectangle(0, 0, screen.width, screen.height)
    screen.blur(5)

def render_overlay():
    pass