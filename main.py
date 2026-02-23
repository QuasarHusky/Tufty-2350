import sys
import os
from badgeware import fatal_error, display, DEFAULT_FONT, State, file_exists
import machine
import gc

system_state = {
    "backlight": 0.5,
    "launch_app": None,
}
State.load("quasar.system", system_state)

display.backlight(system_state["backlight"])

screen.pen = color.rgb(0, 0, 0)
screen.clear()
display.update(screen.width == 320)

running_app = None

standard_modules = list(sys.modules.keys())

sys.path.append("/system/libs")

def run(app):
    try:
        screen.font = DEFAULT_FONT
        screen.pen = color.rgb(0, 0, 0)
        screen.clear()
        screen.pen = color.rgb(255, 255, 255)

        init = getattr(app, "init", None)
        update = getattr(app, "update")
        on_exit = getattr(app, "on_exit", None)

        if init:
            init()
            gc.collect()
        
        result = None

        while result == None:
            io.poll()
            result = update()

            # screen.pen = color.rgb(0, 0, 0)
            # screen.rectangle(0, 0, 40, 15)
            # screen.font = DEFAULT_FONT
            # screen.pen = color.rgb(255, 255, 255)
            # screen.text(f"{1000 / io.ticks_delta:.1f}", 2, 0)

            display.update(screen.width == 320)
        
        gc.collect()

        if on_exit:
            on_exit()
            gc.collect()

        return result

    except Exception as e:
        fatal_error("App Error", e)

def quit_to_launcher(pin):
    system_state["launch_app"] = None
    State.save("quasar.system", system_state)
    
    while not pin.value():
        pass
    
    machine.reset()



app = system_state["launch_app"]

if app == None:
    try:
        sys.path.insert(0, "/system/launcher")
        launcher = __import__("/system/launcher")
    except Exception as e:  # noqa: BLE001
        fatal_error("System Error", e)
    
    app = run(launcher)

    if sys.path[0].startswith("/system/launcher"):
        sys.path.pop(0)
    
    del launcher


for key, _module in sys.modules.items():
    if key not in standard_modules:
        del sys.modules[key]

gc.collect()

if app is None:
    fatal_error("System Error", "Launcher did not provide an app to run")

system_state["launch_app"] = app
State.save("quasar.system", system_state)

io.poll()
io.poll()
while io.held:
    io.poll()

machine.Pin.board.BUTTON_HOME.irq(
    trigger=machine.Pin.IRQ_FALLING, handler=quit_to_launcher
)

sys.path.insert(0, app)

try:
    os.chdir(app)
    running_app = __import__(app)
except Exception as e:
    system_state["launch_app"] = None
    State.save("quasar.system", system_state)
    fatal_error("System Error", e)

run(running_app)

machine.reset()
