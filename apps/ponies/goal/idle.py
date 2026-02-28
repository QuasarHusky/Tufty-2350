import random
from goal.goal import Goal

class IdleGoal(Goal):

    def __init__(self, pony, duration=None):
        super().__init__(pony)

        if duration == None:
            self.timer = random.randint(3000, 8000)
        else:
            self.timer = duration

        self.blink_timer = random.randint(0, 4000)
        self.blinking = False

    def start(self):
        self.pony.animate_looping("idle")

    def update(self):
        self.timer -= badge.ticks_delta
        
        if self.timer <= 0:
            return True
        
        self.blink_timer -= badge.ticks_delta

        if self.blink_timer <= 0:
            if self.blinking == False:
                self.blinking = True
                self.pony.animate_oneshot("blink")
            
            if self.pony.is_animation_finished():
                self.blinking = False
                self.pony.animate_looping("idle")
                self.blink_timer = random.randint(1500, 4000)

    def finish(self, interrupt):
        self.pony.animate_looping("idle")

    def debug(self):
        return [
            "idle",
            f"timer: {self.timer}",
            f"blink: {self.blinking} / {self.blink_timer}",
        ]