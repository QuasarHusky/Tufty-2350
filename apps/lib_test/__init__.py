from app_menu import AppMenu
import toast
import system_ui
import machine

app_menu = AppMenu("Lib Test")
app_menu.menu.button("Return", app_menu.close)
app_menu.menu.button("Exit", machine.reset)
app_menu.menu.button("Button 1", lambda: toast.show("Pressed 1"))
app_menu.menu.button("Button 2", lambda: toast.show("Pressed 2"))
app_menu.menu.button("Button 3", lambda: toast.show("Pressed 3"))

count = 0

def init():
    pass

def update():
    global count

    screen.pen = color.rgb(0, 50, 100)
    screen.clear()
    
    toast.update()
    system_ui.update()

    if app_menu.update():
        return

    if io.BUTTON_UP in io.pressed:
        count += 1
        toast.show(f"Count: {count}", duration=toast.SHORT, position=toast.TOP)
    
    if io.BUTTON_DOWN in io.pressed:
        count -= 1
        toast.show(f"Count: {count}", duration=toast.SHORT, position=toast.BOTTOM)

def on_exit():
    pass