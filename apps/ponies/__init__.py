import gc

from world import World
from pony import Pony
import ponies.paperbark as paperbark
import ponies.vinyl_scratch as vinyl_scratch
import ponies.cocoa_butter as cocoa_butter

gc.threshold(-1)

debug = False
debug_target_pony = 0

world = World()

def init():
    world.spawn_pony(paperbark)
    world.spawn_pony(vinyl_scratch)
    world.spawn_pony(cocoa_butter)

def update():
    global world, debug, debug_target_pony

    # BUG: Prevent updating when having a lag spike - likely caused by GC?
    if io.ticks_delta > 500:
        return
    
    world.update()
    world.render()

    if debug:
        render_debug()

    if io.BUTTON_B in io.pressed:
        debug = not debug   

    if io.BUTTON_A in io.pressed and debug:
        debug_target_pony -= 1
        if debug_target_pony < 0:
            debug_target_pony = len(world.ponies) - 1   
    
    if io.BUTTON_C in io.pressed and debug:
        debug_target_pony += 1
        if debug_target_pony >= len(world.ponies):
            debug_target_pony = 0

def render_debug():
    global debug_target_pony
    world.ponies[debug_target_pony].render_debug()