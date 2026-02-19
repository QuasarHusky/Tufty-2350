class AppMenu:

    def __init__(self, label):
        self.menu = Menu(self, None, label)
        self.open_menu = None

    def close(self):
        self.open_menu = None

    def update(self):
        menu_open = self.open_menu != None

        if io.BUTTON_HOME in io.pressed:
            if menu_open:
                self.open_menu = None
            else:
                self.open_menu = self.menu

        if menu_open:
            self.open_menu.render()

        return menu_open

class Menu:

    def __init__(self, app_menu, parent, label):
        self.app_menu = app_menu
        self.parent = parent
        self.label = label
        self.items = []

    def render(self):
        screen.pen = color.rgb(0, 0, 0, 172)
        screen.rectangle(0, 0, screen.width, screen.height)

        screen.pen = color.rgb(255, 255, 255)
        screen.text(self.label, 10, 10)

        self.render_items()

    def render_items(self):
        y = 20

        for index, item in enumerate(self.items):
            item_height = item.get_height()
            item.render(4, y, screen.width - 8, item_height, index == 0)
            y += item_height + 2

    def add(self, item):
        self.items.append(item)
        return item

    def button(self, label, callback):
        return self.add(MenuButton(label, callback))

class MenuItem:

    def get_height(self):
        return 20
    
    def can_target(self):
        return False

    def update(self):
        pass

    def render(self, x, y, width, height, targeted):
        screen.pen = color.rgb(0, 0, 0)
        screen.rectangle(x, y, width, height)

class MenuButton:

    def __init__(self, label, callback):
        self.label = label
        self.callback = callback

    def get_height(self):
        text_w, text_h = screen.measure_text(self.label)
        return text_h + 4
    
    def update(self):
        if io.BUTTON_B in io.pressed:
            self.callback()

    def render(self, x, y, width, height, targeted):
        if targeted:
            screen.pen = color.rgb(10, 10, 10)
        else:
            screen.pen = color.rgb(30, 30, 30)

        screen.rectangle(x, y, width, height)

        screen.pen = color.rgb(255, 255, 255)
        screen.text(self.label, x + 4, y + 2)