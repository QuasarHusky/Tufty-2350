from badgeware import State, display

system_state = {
    "backlight": 0.5,
}
State.load("quasar.system", system_state)

background_image = image.load("/system/assets/images/background.png")

def init():
    pass

def update():
    global count

    screen.blit(background_image, vec2(0, 0))

    screen.pen = color.rgb(0, 0, 0)
    screen.rectangle(0, 0, screen.width, 15)

    screen.pen = color.rgb(255, 255, 255)
    screen.text(f"Backlight: {backlight_to_percent(system_state["backlight"]) * 100:.0f}%", 4, 2)

    if badge.pressed(BUTTON_UP):
        system_state["backlight"] = percent_to_backlight(min(1, backlight_to_percent(system_state["backlight"]) + 0.1))
        display.backlight(system_state["backlight"])
        State.save("quasar.system", system_state)

    if badge.pressed(BUTTON_DOWN):
        system_state["backlight"] = percent_to_backlight(max(0, backlight_to_percent(system_state["backlight"]) - 0.1))
        display.backlight(system_state["backlight"])
        State.save("quasar.system", system_state)

def percent_to_backlight(percent):
    return (percent * (1 - 0.45)) + 0.45

def backlight_to_percent(backlight):
    return (backlight - 0.45) / (1 - 0.45)