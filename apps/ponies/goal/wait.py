from goal.goal import Goal

class WaitGoal(Goal):

    def __init__(self, pony, duration=None):
        super().__init__(pony)

        self.timer = duration

    def start(self):
        pass

    def update(self):
        self.timer -= badge.ticks_delta
        return self.timer <= 0

    def finish(self, interrupt):
        pass

    def debug(self):
        return [
            "wait",
            f"timer: {self.timer}",
        ]