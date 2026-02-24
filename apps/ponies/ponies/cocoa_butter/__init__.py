from badgeware import SpriteSheet
import random
import goal
from utils import LEFT, RIGHT

id = "cocoa_butter"
name = "Cocoa Butter"

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
            LEFT: SpriteSheet("ponies/cocoa_butter/idle_left.png", 1, 1).animation(),
            RIGHT: SpriteSheet("ponies/cocoa_butter/idle_right.png", 1, 1).animation(),
        },
        "blink": None,
        "walk": {
            "framerate": 24,
            LEFT: SpriteSheet("ponies/cocoa_butter/walk_left.png", 16, 1).animation(),
            RIGHT: SpriteSheet("ponies/cocoa_butter/walk_right.png", 16, 1).animation(),
        },
    }

def available_goals(pony):
    goals = {
        "idle": {
            "weight": 50,
            "build": lambda pony: [goal.IdleGoal(pony)],
        },
        "wander": {
            "weight": 10,
            "build": lambda pony: [goal.WanderGoal(pony)],
        },
        "portal": {
            "weight": 1,
            "build": build_portal_goal,
        }
    }

    return goals

def build_portal_goal(pony):
    if random.random() > 0.5:
        # Right portal
        return [
            goal.WalkToPointGoal(pony, screen.width + 20, pony.y),
            goal.TeleportGoal(pony, -20 - pony.width, pony.y),
            goal.WalkToPointGoal(pony, 10, pony.y),
        ]
    else:
        # Left portal
        return [
            goal.WalkToPointGoal(pony, -20 - pony.width, pony.y),
            goal.TeleportGoal(pony, screen.width + 20, pony.y),
            goal.WalkToPointGoal(pony, screen.width - pony.width - 10, pony.y),
        ]
