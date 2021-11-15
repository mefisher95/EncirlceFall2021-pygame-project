from pygame import constants
import Surface, pygame
from pygame import Rect
from Laser import Laser
from BaseObject import BaseObject
from consants import width, height

class Player(BaseObject):
    def __init__(self, surface: Surface, x: float = (width / 2), y: float = height - 100) -> None:
        super().__init__(surface, x, y)

        self.image = pygame.image.load('./../images/GalaxianGalaxip.gif')
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.w / 2
        self.rect.y = y
        self.x = self.rect.x

        # self.color = list(color)
        self.speed = 3.14

    def draw(self):
        # pygame.draw.rect(self.surface.surface(), self.color, self.rect)
        self.surface.surface().blit(self.image, self.rect)
    def shoot(self):
        laser_x = self.x + self.rect.w / 2
        laser_y = self.y - 5
        return Laser(self.surface, laser_x, laser_y)


    def move(self): 
        keys = pygame.key.get_pressed()

        dictionary = { 'a' : True, 'b' : False }
        dictionary['a']
        # print(keys)

        if keys[pygame.K_w] and keys[pygame.K_a]: x, y = -1, -1
        elif keys[pygame.K_w] and keys[pygame.K_d]: x, y =  1, -1
        elif keys[pygame.K_s] and keys[pygame.K_a]: x, y = -1, 1
        elif keys[pygame.K_s] and keys[pygame.K_d]: x, y = 1, 1
        elif keys[pygame.K_w]: x, y = 0, -1
        elif keys[pygame.K_a]: x, y = -1, 0
        elif keys[pygame.K_s]: x, y = 0, 1
        elif keys[pygame.K_d]: x, y = 1, 0
        else: return 

        self.x += x * self.speed; self.y += y * self.speed
        self.rect.x, self.rect.y = self.x, self.y
