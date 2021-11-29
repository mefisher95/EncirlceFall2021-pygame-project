from AlienBaseObject import AlienBaseObject
from Surface import Surface
import pygame


class AquaAlien(AlienBaseObject):
    def __init__(self, surface: Surface, x: float, y: float) -> None:
        super().__init__(surface, x, y)

        self.image = pygame.image.load('./../images/GalaxianAquaAlien.gif')
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.w / 2
        self.rect.y = y
        self.x = self.rect.x

        self.speed = 2.14

    def draw(self):
        self.surface.surface().blit(self.image, self.rect)

    def attack(self): pass

    def move(self): pass
        