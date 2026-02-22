from gui.container import Container
from gui.units import Edges, Size, Bounds

class VBox(Container):

    def __init__(self):
        super().__init__()
        self.gap = 0
        self.padding = Edges.all(0)
        self.background = None

    def size(self):
        width = 0
        height = 0

        for child in self.children:
            size = child.size()

            width = max(width, size.width)
            height += size.height

        width += self.padding.total_width()
        height += self.padding.total_height()

        height += min(0, self.gap * (len(self.children) - 1))

        return Size(width, height)

    def render(self, bounds):
        if self.background != None:
            screen.pen = self.background
            screen.rectangle(bounds.x, bounds.y, bounds.width, bounds.height)

        x = bounds.x + self.padding.left
        y = bounds.y + self.padding.top

        for child in self.children:
            child_size = child.size()
            child_bounds = child_size.as_bounds(x, y)
            child.render(child_bounds)
            y += child_size.height + self.gap

    def update(self):
        pass