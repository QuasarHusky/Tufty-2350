import toast
import system_ui

count = 0

def init():
    pass

def update():
    global count

    screen.pen = color.rgb(0, 50, 100)
    screen.clear()
    
    if io.BUTTON_UP in io.pressed:
        count += 1
        toast.show(f"Count: {count}", duration=toast.SHORT, position=toast.TOP)
    
    if io.BUTTON_DOWN in io.pressed:
        count -= 1
        toast.show(f"Count: {count}", duration=toast.SHORT, position=toast.BOTTOM)

    toast.update()
    system_ui.update()

def on_exit():
    pass