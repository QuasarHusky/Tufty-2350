import math

import system_ui

quasar_text = image.load("images/quasar-text.png")
beachball = image.load("images/beachball.png")
quasar_happy = image.load("images/quasar-happy.png")

def init():
    pass

def update():
    screen.pen = color.rgb(19, 47, 122)
    screen.clear()
    
    screen.pen = color.rgb(24, 60, 141)
    wave_precession = io.ticks / 1500
    for x in range(0, screen.width, 3):
        screen.rectangle(x, math.floor(math.sin(wave_precession + (x / 25)) * 5) + 15, 3, screen.height - 30)

    screen.blit(quasar_text, vec2(math.floor((screen.width - quasar_text.width) / 2), math.floor((screen.height / 3) - (quasar_text.height / 2))))

    # text = "He / Him"
    # screen.pen = color.rgb(255, 255, 255)
    # screen.font = rom_font.ignore

    # text_w, text_h = screen.measure_text(text)
    # screen.text(text, math.floor((screen.width - text_w) / 2), math.floor((screen.height / 3 * 2) - (text_h / 2)))

    screen.blit(quasar_happy, vec2(math.floor((screen.width - quasar_happy.width) / 2), math.floor(screen.height - 75 - math.sin(io.ticks / 1000) * 10)))
    screen.blit(beachball, vec2(math.floor((screen.width - beachball.width) / 2), 20))

    system_ui.update()

def on_exit():
    pass