import pygame

from constants import width, height

import Surface
from Laser import Laser
from BaseObject import BaseObject

class Player(BaseObject):
    def __init__(self, surface: Surface, x: float = (width / 2), y: float = height - 100) -> None:
        super().__init__(surface, x, y)

        self.image = pygame.image.load('./../images/GalaxianGalaxip.gif')
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.w / 2
        self.rect.y = y
        self.x = self.rect.x

        self.speed = 3.14

    def draw(self):
        if self.is_alive():
            self.surface.surface().blit(self.image, self.rect)

    def shoot(self):
        laser_x = self.x + self.rect.w / 2
        laser_y = self.y - 5
        return Laser(self.surface, laser_x, laser_y, True)


    def down_y(self):
        if self.rect.y + self.rect.h >= height - 50:
            self.y = height - self.rect.h - 50
        else:
            self.y += self.speed

    def up_y(self):
        if self.rect.y <= height / 2:
            self.y = height / 2
        else:
            self.y -= self.speed

    def left_x(self):
        if self.x <= 10: 
            self.x = 10
        else:
            self.x -= self.speed

    def right_x(self):
        if self.rect.x + self.rect.w >= width - 10:
            self.x = width - self.rect.w - 10
        else:
            self.x += self.speed


    def move(self): 
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and keys[pygame.K_a]:
            self.up_y()
            self.left_x()
        elif keys[pygame.K_w] and keys[pygame.K_d]: 
            self.up_y()
            self.right_x()
        elif keys[pygame.K_s] and keys[pygame.K_a]: 
            self.left_x()
            self.down_y()
        elif keys[pygame.K_s] and keys[pygame.K_d]: 
            self.down_y()
            self.right_x()
        elif keys[pygame.K_w]: 
            self.up_y()
        elif keys[pygame.K_a]: 
            self.left_x()
        elif keys[pygame.K_s]: 
            self.down_y()
        elif keys[pygame.K_d]: 
            self.right_x()
        else: return 

        self.rect.x = self.x
        self.rect.y = self.y
