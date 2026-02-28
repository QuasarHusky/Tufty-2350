import wifi_patched as wifi
import requests
import os

def init():
    global download

    show_message("Starting...")
    wifi.connect()

    status, message = None, ""

    while status != 3:
        badge.poll()
        wifi.tick()
        status, message = wifi.status()
        show_message(f"[{status}] {message}")
    
    show_message("Downloading image...")
    res = requests.get("https://quasar.dog/absolute-fluttershy.png", stream=True)
    
    show_message("Saving image...")
    with open("/state/download.png", "wb") as file:
        file.write(res.content)

    download = image.load("/state/download.png")
    os.remove("/state/download.png")

    screen.clear()
    screen.blit(download, vec2(0, 0))

    badge.update()

def update():
    pass

def show_message(text):
    screen.pen = color.rgb(0, 0, 0)
    screen.clear()

    text_w, text_h = screen.measure_text(text)

    screen.pen = color.rgb(255, 255, 255)
    screen.text(text, (screen.width - text_w) / 2, (screen.height - text_h) / 2)

    badge.update()