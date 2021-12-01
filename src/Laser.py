from pygame import constants
import Surface, pygame, colors
from pygame import Rect
from BaseObject import BaseObject
from ObjectContainer import ObjectContainer

import constants

class Laser(BaseObject):
    def __init__(self, surface: Surface, x: float, y: float, is_player: bool) -> None:
        super().__init__(surface, x, y)

        self.player = is_player

        if self.player:
            self.rect = Rect(x, y, 2, 5)
            self.color = list(colors.RED)
            self.speed = 6.28

        else:
            self.rect = Rect(x, y - 5, 2, 5)
            self.color = list(colors.GREEN)
            self.speed = -6.28

        self.alive = True
        return None

    def is_player(self): return self.player
    def is_alive(self) -> bool: return self.alive
    def kill(self) -> None: self.alive = False

    def draw(self) -> None:
        pygame.draw.rect(self.surface.surface(), self.color, self.rect)
        return None

    def move(self) -> None:
        self.y -= self.speed
        self.rect.y = self.y

        if self.y < 0 or self.y > constants.height: self.kill()
        return None

class Lasers(ObjectContainer):
    def __init__(self) -> None:
        super().__init__()

    