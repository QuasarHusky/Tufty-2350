from badgeware import fatal_error

try:
    import sys
    import os
    from badgeware import display, DEFAULT_FONT, State
    import machine
    import gc

    system_state = {
        "backlight": 0.5,
        "launch_app": None,
    }
    State.load("quasar.system", system_state)

    display.backlight(system_state["backlight"])

    badge.default_clear = None
    badge.mode(LORES)

    screen.pen = color.rgb(0, 0, 0)
    screen.clear()
    display.update()

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
            
            result = None

            while result == None:
                badge.poll()
                result = update()

                # screen.pen = color.rgb(0, 0, 0)
                # screen.rectangle(0, 0, 40, 15)
                # screen.font = DEFAULT_FONT
                # screen.pen = color.rgb(255, 255, 255)
                # screen.text(f"{1000 / badge.ticks_delta:.1f}", 2, 0)

                display.update()

            if on_exit:
                on_exit()

            return result

        except Exception as e:
            if not badge.usb_connected():
                State.load("quasar.system", system_state)
                system_state["launch_app"] = None
                State.save("quasar.system", system_state)

            fatal_error("App Error", e)

    def quit_to_launcher(pin):
        State.load("quasar.system", system_state)
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
            fatal_error("Launcher Error", e)
        
        app = run(launcher)

        if sys.path[0].startswith("/system/launcher"):
            sys.path.pop(0)
        
        del launcher


    for key, _module in sys.modules.items():
        if key not in standard_modules:
            del sys.modules[key]

    gc.collect()

    if app is None:
        fatal_error("App Launching Error", "Launcher did not provide an app to run")

    State.load("quasar.system", system_state)
    system_state["launch_app"] = app
    State.save("quasar.system", system_state)

    badge.poll()
    badge.poll()
    while badge.held():
        badge.poll()

    machine.Pin.board.BUTTON_HOME.irq(
        trigger=machine.Pin.IRQ_FALLING, handler=quit_to_launcher
    )

    sys.path.insert(0, app)

    try:
        os.chdir(app)
        running_app = __import__(app)
    except Exception as e:
        State.load("quasar.system", system_state)
        system_state["launch_app"] = None
        State.save("quasar.system", system_state)
        
        fatal_error("App Launching Error", e)

    run(running_app)

    machine.reset()

except Exception as e:
    screen.pen = color.rgb(0, 0, 0)
    screen.clear()
    fatal_error("System Error", e)