import gc

from world import World
from pony import Pony
import ponies.paperbark as paperbark
import ponies.vinyl_scratch as vinyl_scratch
import ponies.cocoa_butter as cocoa_butter

gc.threshold(-1)

debug = False

world = World()

def init():
    world.spawn_pony(paperbark)
    world.spawn_pony(vinyl_scratch)
    world.spawn_pony(cocoa_butter)

def update():
    global world, debug

    world.update()
    world.render()

    if debug:
        render_debug()

    if io.BUTTON_B in io.pressed:
        debug = not debug   

def render_debug():
    for pony in world.ponies:
        pony.render_debug()