class Edges:

    def __init__(self, top, right, bottom, left):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left

    def all(value):
        return Edges(value, value, value, value)
    
    def xy(x, y):
        return Edges(y, x, y, x)
    
    def total_width(self):
        return self.left + self.right
    
    def total_height(self):
        return self.top + self.bottom


class Size:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def as_bounds(self, x, y):
        return Bounds(x, y, self.width, self.height)


class Bounds:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def as_size(self):
        return Size(self.width, self.height)
    
    def x2(self):
        return self.x + self.width
    
    def y2(self):
        return self.y + self.height