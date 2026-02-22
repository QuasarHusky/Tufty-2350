import gui
import toast
import system_ui
import machine

app_menu = gui.Panel()
app_menu.root = gui.VBox()
app_menu.root.padding = gui.Edges.all(2)
app_menu.root.gap = 2
app_menu.root.background = color.rgb(0, 0, 0)
app_menu.root.add(gui.Label("Library Test"))

count_label = gui.Label()
app_menu.root.add(count_label)

app_menu.root.add(gui.Label("Another line"))

count = 0

def init():
    pass

def update():
    global count

    screen.pen = color.rgb(0, 50, 100)
    screen.clear()

    count_label.text = f"Count: {count}"
    
    gui.update()
    toast.update()
    system_ui.update()

    if io.BUTTON_HOME in io.pressed:
        if gui.is_active():
            gui.close_all()
        else:
            gui.replace(app_menu)

    if not gui.is_active():
        if io.BUTTON_UP in io.pressed:
            count += 1
            toast.show(f"Count: {count}", duration=toast.SHORT, position=toast.TOP)
        
        if io.BUTTON_DOWN in io.pressed:
            count -= 1
            toast.show(f"Count: {count}", duration=toast.SHORT, position=toast.BOTTOM)

def on_exit():
    pass