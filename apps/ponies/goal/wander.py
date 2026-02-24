import random
import math
from goal.goal import Goal
from utils import LEFT, RIGHT

class WanderGoal(Goal):

    def __init__(self, pony, duration=None, speed=50):
        super().__init__(pony)

        if duration == None:
            self.timer = random.randint(5000, 8000)
        else:
            self.timer = duration

        self.speed = speed

        direction = random.random() * math.pi * 2
        self.vx = math.cos(direction) * speed
        self.vy = math.sin(direction) * speed

    def start(self):
        if self.vx > 0:
            self.pony.set_facing(RIGHT)
        else:
            self.pony.set_facing(LEFT)
        
        self.pony.animate_looping("walk")

    def update(self):
        self.timer -= io.ticks_delta
        
        if self.timer <= 0:
            return True
        
        delta = io.ticks_delta / 1000
        self.pony.x += self.vx * delta
        self.pony.y += self.vy * delta

        if self.pony.x < 0:
            self.pony.x = 0
            self.vx *= -1
            self.pony.set_facing(RIGHT)
        
        if self.pony.x > screen.width - self.pony.width:
            self.pony.x = screen.width - self.pony.width
            self.vx *= -1
            self.pony.set_facing(LEFT)
        
        if self.pony.y < 0:
            self.pony.y = 0
            self.vy *= -1
        
        if self.pony.y > screen.height - self.pony.height:
            self.pony.y = screen.height - self.pony.height
            self.vy *= -1

        return False

    def finish(self, interrupt):
        self.pony.animate_looping("idle")

    def debug(self):
        return [
            "wander",
            f"timer: {self.timer}"
        ]