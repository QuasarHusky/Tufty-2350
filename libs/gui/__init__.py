from gui.units import Edges, Size, Bounds
from gui.panel import Panel
from gui.item import Item
from gui.container import Container
from gui.label import Label
from gui.vbox import VBox

active_panels = []

def update():
    if len(active_panels) == 0:
        return
    
    panel = active_panels[len(active_panels) - 1]

    panel.update()
    panel.render()

def open(panel):
    active_panels.append(panel)

def close():
    active_panels.pop()

def close_all():
    active_panels.clear()

def replace(panel):
    close_all()
    open(panel)

def is_active():
    return len(active_panels) > 0