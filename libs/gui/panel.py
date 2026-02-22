from gui.units import Bounds

class Panel:

    def __init__(self, root=None):
        self.root = root
    
    def render(self):
        if self.root != None:
            size = self.root.size()
            self.root.render(size.as_bounds(0, 0))

    def update(self):
        if self.root != None:
            self.root.update()

