import os
import sys

sys.path.insert(0, "/system/apps/gallery")
os.chdir("/system/apps/gallery")

mode(HIRES)

image_paths = []

current_index = 0
current_image = None

message_timer = 0
message_text = ""

def init():
    global image_paths

    image_paths = list(filter(lambda path: path.lower().endswith(".png"), os.listdir("images")))
    image_paths.sort()

    if len(image_paths) > 0:
        change_image(image_paths[0])

def update():
    global image_paths, current_image

    screen.pen = color.rgb(0, 0, 0)
    screen.clear()

    if current_image == None:
        screen.pen = color.rgb(0, 0, 0)
        screen.clear()

        screen.pen = color.rgb(255, 255, 255)
        screen.text("No images available", 10, 10)

        return
    
    screen.blit(current_image, vec2(0, 0))

    render_message()

    if io.BUTTON_A in io.pressed or io.BUTTON_UP in io.pressed:
        prev_image()

    if io.BUTTON_C in io.pressed or io.BUTTON_DOWN in io.pressed:
        next_image()

def on_exit():
    pass

def change_image(image_path):
    global current_image
    current_image = image.load(f"images/{image_path}")

def next_image():
    global current_index, image_paths

    if len(image_paths) == 0:
        return

    current_index += 1

    if current_index >= len(image_paths):
        current_index = 0

    change_image(image_paths[current_index])
    
    show_message(f"({current_index + 1}/{len(image_paths)}) {image_paths[current_index][:-4]}")

def prev_image():
    global current_index, image_paths

    if len(image_paths) == 0:
        return

    current_index -= 1

    if current_index < 0:
        current_index = len(image_paths) - 1

    change_image(image_paths[current_index])

    show_message(f"({current_index + 1}/{len(image_paths)}) {image_paths[current_index][:-4]}")

def show_message(text):
    global message_timer, message_text

    message_timer = 1500
    message_text = text 

def render_message():
    global message_timer

    if message_timer <= 0:
        return
    
    message_timer -= io.ticks_delta
    
    width, height = screen.measure_text(message_text)
    x = (screen.width - width) / 2
    y = screen.height - height - 5

    screen.pen = color.rgb(0, 0, 0)
    screen.rectangle(x - 2, y - 2, width + 4, height + 4)

    screen.pen = color.rgb(255, 255, 255)
    screen.text(message_text, x, y)