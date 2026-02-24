from goal.goal import Goal

class AnimationLoopGoal(Goal):

    def __init__(self, pony, animation, duration):
        super().__init__(pony)

        self.animation = animation
        self.timer = duration

    def start(self):
        self.pony.animate_looping(self.animation)

    def update(self):
        self.timer -= io.ticks_delta
        return self.timer <= 0

    def finish(self, interrupt):
        self.pony.animate_looping("idle")

    def debug(self):
        return [
            "animation_loop",
            f"anim: {self.animation}",
            f"timer: {self.timer}"
        ]