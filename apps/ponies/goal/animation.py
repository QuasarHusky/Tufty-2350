import random
from goal.goal import Goal

class AnimationGoal(Goal):

    def __init__(self, pony, animation):
        super().__init__(pony)

        self.animation = animation

    def start(self):
        self.pony.animate_oneshot(self.animation)

    def update(self):
        return self.pony.is_animation_finished()

    def finish(self, interrupt):
        self.pony.animate_looping("idle")

    def debug(self):
        return [
            "animation",
            f"{self.animation}",
        ]