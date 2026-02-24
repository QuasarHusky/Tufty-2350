import random

from pony import Pony

background_image = image.load("backgrounds/grass.png")

class World:
    
    def __init__(self):
        self.ponies = []

    def update(self):
        for pony in self.ponies:
            pony.update()

    def render(self):
        screen.blit(background_image, vec2(0, 0))

        ponies_render_order = sorted(self.ponies, key=lambda pony: pony.x + (pony.y * 100))

        for pony in ponies_render_order:
            pony.render_shadow()
        
        for pony in ponies_render_order:
            pony.render()

    def spawn_pony(self, pony_data):
        pony = Pony(pony_data, self)
        self.ponies.append(pony)
        return pony
    
    def find_ponies_by_type(self, type_id):
        found = []

        for pony in self.ponies:
            if pony.data.id == type_id:
                found.append(pony)
        
        return found
    
    def random_pony_of_type(self, type_id):
        ponies = self.find_ponies_by_type(type_id)

        if len(ponies) > 0:
            return random.choice(ponies)
        else:
            return None