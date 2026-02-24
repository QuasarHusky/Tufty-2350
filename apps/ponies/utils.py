import math
import random

LEFT = 0
RIGHT = 1

def lerp(start, end, t):
    return start * (1 - t) + end * t

def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

def weighted_random(choices, weights):
    total_weight = sum(weights)
    r = random.uniform(0, total_weight)

    for i, weight in enumerate(weights):
        r -= weight
        if r <= 0:
            return choices[i]

    raise RuntimeError("Weighted random failed to pick")