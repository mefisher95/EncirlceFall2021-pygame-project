from AlienBaseObject import AlienBaseObject
from ObjectContainer import ObjectContainer
from Surface import Surface
from Laser import Laser, Lasers
import pygame

import random


class AquaAlien(AlienBaseObject):
    def __init__(self, surface: Surface, x: float, y: float) -> None:
        super().__init__(surface, x, y)

        self.image = pygame.image.load('./../images/GalaxianAquaAlien.gif')
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.w / 2
        self.rect.y = y
        self.x = self.rect.x

        self.speed = 2.14
        
        ##### states #####
        # state 0 = flying in formation
        # state 1 = firing laser
        # state 2 = diving down
        # state 3 = returning to formation
        self.state = 0


    def shoot(self):
        laser_x = self.x + self.rect.w / 2
        laser_y = self.y + self.rect.height
        return Laser(self.surface, laser_x, laser_y, False)


    def attack(self): 
        self.state = random.randint(0, 1)
        

    def move(self): pass


class AquaFleet(ObjectContainer):
    def __init__(self, surface, lasers: Lasers) -> None:
        super().__init__()

        self.lasers = lasers
        self.delay = 30

        # self.objects = [ AquaAlien(surface, 100 + x * 32, 50) for x in range(10)]
        
        for i in range(15):
            self.objects.append(AquaAlien(surface, 100 + i * 32, 50))

        for i in range(15):
            self.objects.append(AquaAlien(surface, 100 + i * 32, 100))


    def attack(self):
        if len(self.objects) > 0: random_ships = random.sample(self.objects, 1)
        else: return

        if self.delay >= 0:
            self.delay -= 1
            return
        else:
            self.delay = len(self.objects)

        for ship in random_ships:
            ship.attack()
            if ship.state == 1: self.lasers.add(ship.shoot())
