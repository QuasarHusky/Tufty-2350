import os
import sys

import toast

sys.path.insert(0, "/system/apps/gallery")
os.chdir("/system/apps/gallery")

mode(HIRES)

image_paths = []

current_index = 0
current_image = None

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

    if io.BUTTON_A in io.pressed or io.BUTTON_UP in io.pressed:
        prev_image()

    if io.BUTTON_C in io.pressed or io.BUTTON_DOWN in io.pressed:
        next_image()

    toast.update()

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
    toast_current_image()

def prev_image():
    global current_index, image_paths

    if len(image_paths) == 0:
        return

    current_index -= 1

    if current_index < 0:
        current_index = len(image_paths) - 1

    change_image(image_paths[current_index])
    toast_current_image()


def toast_current_image():
    toast.show(
        f"({current_index + 1}/{len(image_paths)}) {image_paths[current_index][:-4]}",
        duration=toast.SHORT,
        position=toast.BOTTOM
    )
