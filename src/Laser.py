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
        return None

    def is_alive(self) -> bool: return self.alive
    def kill(self) -> None: self.alive = False

    def draw(self) -> None:
        pygame.draw.rect(self.surface.surface(), self.color, self.rect)
        return None

    def move(self) -> None:
        self.y -= self.speed
        self.rect.y = self.y

        if self.y < 0: self.kill()
        return None

class Lasers:
    def __init__(self) -> None:
        self.lasers = []
        return None

    def draw(self) -> None:
        for laser in self.lasers: laser.draw()
        return None

    def move(self) -> None:
        for laser in self.lasers: laser.move()
        self.lasers = [ laser for laser in self.lasers if laser.is_alive() ]
        return None

    def add(self, laser: Laser) -> None:
        self.lasers.append(laser)
        return None

    def __len__(self) -> int: return len(self.lasers)

    