from AlienBaseObject import AlienBaseObject
from ObjectContainer import ObjectContainer
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


    def attack(self): pass

    def move(self): pass


class AquaFleet(ObjectContainer):
    def __init__(self, surface) -> None:
        super().__init__()

        # self.objects = [ AquaAlien(surface, 100 + x * 32, 50) for x in range(10)]
        
        for i in range(15):
            self.objects.append(AquaAlien(surface, 100 + i * 32, 50))

        for i in range(15):
            self.objects.append(AquaAlien(surface, 100 + i * 32, 100))
