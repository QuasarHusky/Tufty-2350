from goal.goal import Goal
from utils import LEFT, RIGHT
import utils

class TeleportGoal(Goal):

    def __init__(self, pony, target_x, target_y):
        super().__init__(pony)

        self.target_x = target_x
        self.target_y = target_y

    def start(self):
        self.pony.x = self.target_x
        self.pony.y = self.target_y

    def update(self):
        return True

    def finish(self, interrupt):
        pass

    def debug(self):
        return [
            "teleport",
        ]