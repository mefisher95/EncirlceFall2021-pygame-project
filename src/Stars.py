import pygame
from random import randint

from BaseObject import BaseObject
from Surface import Surface
from consants import *

class Star(BaseObject):
    def __init__(self, surface: Surface, x: float = 0, y: float = 0) -> None:
        super().__init__(surface, x, y)

        self.size = randint(1, 3)
        self.x = randint(0, width)
        self.y = randint(0, height)

        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

        if self.size == 1:
            self.color = (150, 150, 150)
            self.speed = 1

        if self.size == 2:
            self.color = (175, 175, 175)
            self.speed = 2

        if self.size == 3:
            self.color = (180, 180, 255)
            self.speed = 4

        return None

    def move(self):
        self.y += self.speed

        if self.y > height:
            self.size = randint(1, 3)

            self.y = 0
            self.x = randint(0, width)

            self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

            if self.size == 1:
                self.color = (150, 150, 150)
                self.speed = 1

            if self.size == 2:
                self.color = (175, 175, 175)
                self.speed = 2

            if self.size == 3:
                self.color = (180, 180, 255)
                self.speed = 4

        self.rect.y = self.y
        self.rect.x = self.x

    def draw(self):
        pygame.draw.rect(self.surface.surface(), self.color, self.rect)
        

class Stars:
    def __init__(self, surface) -> None:
        self.stars = [ Star(surface) for i in range(100) ]
        return None

    def move(self):
        for star in self.stars: star.move()

    def draw(self):
        for star in self.stars: star.draw()

    def __len__(self): return len(self.stars)