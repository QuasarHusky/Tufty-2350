import math
import random

name = "Space"
auto_cycle = True

particle_count = 40

particles = []
delta = 0

for i in range(particle_count):
    particles.append({
        "x": random.random() * screen.width * 1.2,
        "y": random.random() * screen.height,
        "variation": math.pow(i / particle_count, 2),
    })

def render_background():
    global particles, delta

    delta = io.ticks_delta / 1000

    screen.pen = color.rgb(10, 0, 30)
    screen.clear()

    for particle in particles:
        render_particle(particle)

def render_overlay():
    pass

def render_particle(particle):
    particle["x"] -= (particle["variation"] * 0.97 + 0.03) * 225 * delta

    if particle["x"] < -20:
        particle["x"] += screen.width + 40
        particle["y"] = random.random() * screen.height

    screen.pen = color.rgb(255, 255, 255, 10)
    screen.circle(particle["x"] + particle["variation"] * 20, particle["y"], particle["variation"] * 4 + 2)

    screen.pen = color.rgb(255, 255, 255, 20)
    screen.circle(particle["x"] + particle["variation"] * 10, particle["y"], particle["variation"] * 2 + 1)

    screen.pen = color.rgb(255, 255, 255, math.floor(particle["variation"] * 100 + 80))

    if particle["variation"] > 0.33:
        screen.circle(particle["x"], particle["y"], particle["variation"] * 3)
    else:
        if particle["x"] > 0 and particle["x"] < screen.width:
            screen.put(math.floor(particle["x"]), math.floor(particle["y"]))