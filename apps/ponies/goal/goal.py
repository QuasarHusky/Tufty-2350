import random

class Goal:

    def __init__(self, pony):
        self.pony = pony

    def start(self):
        pass

    def update(self):
        return True

    def finish(self, interrupt):
        pass

    def debug(self):
        return ["no info"]