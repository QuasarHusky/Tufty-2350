import random

class FakeVisualiser():

    def __init__(self, bar_count):
        self.bar_count = 16
        self.bar_targets = []
        self.bar_values = []

        for i in range(bar_count):
            self.bar_values.append(0)
            self.bar_targets.append(0)

    def update(self):
        decay_speed = badge.ticks_delta / 1000 * 3

        for i in range(self.bar_count - 1):
            self.bar_values[i] -= (self.bar_values[i] - self.bar_values[i + 1]) * 0.3

        for i in range(1, self.bar_count):
            self.bar_values[i] -= (self.bar_values[i] - self.bar_values[i - 1]) * 0.3

        for i in range(self.bar_count):
            self.bar_values[i] = max(0, self.bar_values[i] - decay_speed)
            self.bar_values[i] = max(self.bar_values[i], random.random() * random.random())
            self.bar_targets[i] -= (self.bar_targets[i] - self.bar_values[i]) * 0.3

    def get_bar(self, index):
        return self.bar_targets[index] * self.bar_targets[index]