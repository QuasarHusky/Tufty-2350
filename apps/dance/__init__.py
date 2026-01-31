import os
import sys
import math
from badgeware import SpriteSheet

import scenes.void as scene_void
import scenes.visualiser as scene_visualiser

sys.path.insert(0, "/system/apps/dance")
os.chdir("/system/apps/dance")

scenes = [
    scene_void,
    scene_visualiser,
]

animations = [
    {
        "path": "assets/paperbark/dance_5.png",
        "frames": 28,
    },
    {
        "path": "assets/paperbark/dance_8.png",
        "frames": 31,
    },
    {
        "path": "assets/paperbark/dance_7.png",
        "frames": 28,
    },
    {
        "path": "assets/paperbark/dance_2.png",
        "frames": 28,
    },
    {
        "path": "assets/paperbark/jump.png",
        "frames": 28,
    },
    {
        "path": "assets/paperbark/applaud.png",
        "frames": 17,
    },
]

message_timer = 0
message_text = ""

current_scene_index = 0
current_scene = None

current_animation_index = 0
current_animation_sprites = None
animation_start_time = io.ticks

ms_per_frame = 1000 / 30

screen.antialias = image.X2

def init():
    load_scene(scenes[current_scene_index])
    load_animation(animations[current_animation_index])

def update():
    global current_animation_index, current_animation_sprites, animation_start_time

    render()

    if io.BUTTON_B in io.pressed:
        cycle_animation()

    if io.BUTTON_C in io.pressed:
        cycle_scene()

def render():
    global message_timer
    
    current_scene.render_background()

    frame = math.floor((io.ticks - animation_start_time) / ms_per_frame)

    image = current_animation_sprites.frame(frame)
    screen.blit(image, rect((screen.width - (image.width * 2)) / 2 - 8, screen.height - (image.height * 2) + 4, image.width * 2, image.height * 2))
    
    current_scene.render_overlay()

    if message_timer > 0:
        message_timer -= io.ticks_delta
        render_message()


def on_exit():
    pass

def cycle_scene():
    global current_scene_index

    current_scene_index += 1

    if current_scene_index >= len(scenes):
        current_scene_index = 0

    load_scene(scenes[current_scene_index])

    show_message(current_scene.name)

def cycle_animation():
    global current_animation_index, animation_start_time
    
    current_animation_index += 1
    animation_start_time = io.ticks

    if current_animation_index >= len(animations):
        current_animation_index = 0

    load_animation(animations[current_animation_index])

def load_scene(scene):
    global current_scene
    current_scene = scene

def load_animation(animation):
    global current_animation_sprites
    current_animation_sprites = SpriteSheet(animation["path"], animation["frames"], 1).animation()

def show_message(text):
    global message_timer, message_text

    message_timer = 1000
    message_text = text 

def render_message():
    width, height = screen.measure_text(message_text)
    x = (screen.width - width) / 2
    y = 5

    screen.pen = color.rgb(0, 0, 0)
    screen.rectangle(x - 2, y - 2, width + 4, height + 4)

    screen.pen = color.rgb(255, 255, 255)
    screen.text(message_text, x, y)