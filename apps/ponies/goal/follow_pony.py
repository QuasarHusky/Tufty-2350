import random
from goal.goal import Goal
from utils import LEFT, RIGHT
import utils

class FollowPonyGoal(Goal):

    def __init__(self, pony, target_pony, duration=10000, speed=50):
        super().__init__(pony)

        self.target_pony = target_pony
        self.speed = speed
        self.timer = duration
        self.moving = False

        self.blink_timer = random.randint(0, 4000)
        self.blinking = False

        self.target_x = None
        self.target_y = None

    def start(self):
        pass

    def update(self):
        self.timer -= badge.ticks_delta

        if self.timer <= 0:
            return True

        delta = badge.ticks_delta / 1000

        offset_x = 0
        offset_y = 5

        if self.target_pony.facing == LEFT:
            offset_x += 20
        else:
            offset_x -= 20

        self.target_x = self.target_pony.x + offset_x
        self.target_y = self.target_pony.y + offset_y

        distance_to_target = utils.distance(self.pony.x, self.pony.y, self.target_x, self.target_y)

        if distance_to_target > 2:
            vx = ((self.target_x - self.pony.x) / distance_to_target) * self.speed * delta
            vy = ((self.target_y - self.pony.y) / distance_to_target) * self.speed * delta

            self.pony.x += vx
            self.pony.y += vy

            if vx > 0:
                self.pony.set_facing(RIGHT)
            else:
                self.pony.set_facing(LEFT)

            if not self.moving:
                self.moving = True
                self.pony.animate_looping("walk")
                self.blinking = False
        else:
            if self.moving:
                self.moving = False
                self.pony.animate_looping("idle")

            self.blink_timer -= badge.ticks_delta

            if self.blink_timer <= 0:
                if self.blinking == False:
                    self.blinking = True
                    self.pony.animate_oneshot("blink")
                
                if self.pony.is_animation_finished():
                    self.blinking = False
                    self.pony.animate_looping("idle")
                    self.blink_timer = random.randint(1500, 4000)

        return False

    def finish(self, interrupt):
        self.pony.animate_looping("idle")

    def debug(self):
        if self.target_x != None and self.target_y != None:
            screen.pen = color.rgb(255, 255, 0)
            screen.line(self.pony.x, self.pony.y, self.target_x, self.target_y)

            screen.pen = color.rgb(0, 255, 0)
            screen.circle(self.target_x, self.target_y, 5)

        if self.moving:
            screen.pen = color.rgb(255, 255, 255)
        else:
            screen.pen = color.rgb(128, 128, 128)
            
        screen.circle(self.pony.x, self.pony.y, 5)

        return [
            "follow_pony",
            f"{self.target_pony.data.id}",
        ]