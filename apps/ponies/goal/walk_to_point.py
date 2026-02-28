import random
import math
from goal.goal import Goal
from utils import LEFT, RIGHT
import utils

class WalkToPointGoal(Goal):

    def __init__(self, pony, target_x, target_y, speed=50):
        super().__init__(pony)

        self.initial_x = None
        self.initial_y = None
        self.target_x = target_x
        self.target_y = target_y
        self.speed = speed

        self.start_time = None
        self.end_time = None

    def start(self):
        self.initial_x = self.pony.x
        self.initial_y = self.pony.y

        self.start_time = badge.ticks

        distance = utils.distance(self.initial_x, self.initial_y, self.target_x, self.target_y)
        self.duration = math.ceil((distance / self.speed) * 1000)

        if self.target_x > self.initial_x:
            self.pony.set_facing(RIGHT)
        else:
            self.pony.set_facing(LEFT)

        self.pony.animate_looping("walk")

    def update(self):
        if self.duration == 0:
            return True
        
        t = (badge.ticks - self.start_time) / self.duration

        if t >= 1:
            return True
        
        self.pony.x = utils.lerp(self.initial_x, self.target_x, t)
        self.pony.y = utils.lerp(self.initial_y, self.target_y, t)

        return False

    def finish(self, interrupt):
        if not interrupt:
            self.pony.x = self.target_x
            self.pony.y = self.target_y
        
        self.pony.animate_looping("idle")

    def debug(self):
        t = (badge.ticks - self.start_time) / self.duration

        screen.pen = color.rgb(255, 255, 0)
        screen.line(self.initial_x, self.initial_y, self.target_x, self.target_y)

        screen.pen = color.rgb(255, 0, 0)
        screen.circle(self.initial_x, self.initial_y, 5)

        screen.pen = color.rgb(0, 255, 0)
        screen.circle(self.target_x, self.target_y, 5)

        screen.pen = color.rgb(255, 255, 255)
        screen.circle(self.pony.x, self.pony.y, 5)

        return [
            "walk_to_point",
            f"dur: {self.duration}",
            f"t: {t:.2f}",
        ]