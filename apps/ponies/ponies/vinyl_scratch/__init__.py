from badgeware import SpriteSheet
import goal
from utils import LEFT, RIGHT

id = "vinyl_scratch"
name = "Vinyl Scratch"

sprite_bounds = {
    "x": 18,
    "y": 41,
    "width": 44,
    "height": 50,
}

def animations():
    return {
        "idle": {
            "framerate": 24,
            LEFT: SpriteSheet("ponies/vinyl_scratch/idle_left.png", 1, 1).animation(),
            RIGHT: SpriteSheet("ponies/vinyl_scratch/idle_right.png", 1, 1).animation(),
        },
        "blink": None,
        "walk": {
            "framerate": 24,
            LEFT: SpriteSheet("ponies/vinyl_scratch/walk_left.png", 16, 1).animation(),
            RIGHT: SpriteSheet("ponies/vinyl_scratch/walk_right.png", 16, 1).animation(),
        },
    }

def available_goals(pony):
    goals = {
        "idle": {
            "weight": 10,
            "build": lambda pony: [goal.IdleGoal(pony)],
        },
        "wander": {
            "weight": 10,
            "build": lambda pony: [goal.WanderGoal(pony)],
        }
    }

    return goals