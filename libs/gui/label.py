from gui.item import Item
from gui.units import Edges, Size, Bounds

class Label(Item):

    def __init__(self, text=""):
        super().__init__()
        self.text = text
        self.padding = Edges.all(0)
        self.color = color.rgb(255, 255, 255, 255)
        self.background = None

    def size(self):
        width, height = screen.measure_text(self.text)

        width += self.padding.total_width()
        height += self.padding.total_height()

        return Size(width, height)

    def render(self, bounds):
        if self.background != None:
            screen.pen = self.background
            screen.rectangle(bounds.x, bounds.y, bounds.width, bounds.height)
        
        screen.pen = self.color
        screen.text(self.text, bounds.x + self.padding.left, bounds.y + self.padding.top)

    def update(self):
        pass