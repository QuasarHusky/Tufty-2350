from gui.item import Item

class Container(Item):
    
    def __init__(self):
        super().__init__()
        self.children = []

    def add(self, child):
        self.children.append(child)