from BaseObject import BaseObject
from Surface import Surface

class AlienBaseObject(BaseObject):
    def __init__(self, surface: Surface, x: float, y: float) -> None:
        super().__init__(surface, x, y)

        self.image = None
        self.rect = None
        self.speed = 0
        self.alive = True

    def move(self): pass
    def attack(self): pass

    def draw(self): 
        if self.is_alive():
            self.surface.surface().blit(self.image, self.rect)