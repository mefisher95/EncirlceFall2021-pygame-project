import Surface, pygame, colors
from pygame import Rect
from BaseObject import BaseObject

class Laser(BaseObject):
    def __init__(self, surface: Surface, x: float, y: float) -> None:
        super().__init__(surface, x, y)

        self.rect = Rect(x, y, 2, 5)
        self.color = list(colors.RED)
        self.speed = 6.28

        self.alive = True

    def is_alive(self): return self.alive
    def kill(self): self.alive = False

    def draw(self):
        pygame.draw.rect(self.surface.surface(), self.color, self.rect)

    def move(self):
        self.y -= self.speed
        self.rect.y = self.y

        if self.y < 0: self.kill()

class Lasers:
    def __init__(self) -> None:
        self.lasers = []
        return None

    def draw(self):
        for laser in self.lasers: laser.draw()

    def move(self):
        for laser in self.lasers: laser.move()
        self.lasers = [ laser for laser in self.lasers if laser.is_alive() ]

    def add(self, laser: Laser) -> None:
        self.lasers.append(laser)

    def __len__(self): return len(self.lasers)

    