import pygame, sys
from random import randint
from pygame import constants

from pygame.rect import Rect
from pygame.sprite import collide_rect
from BasicObject import BaseObject

import consants, colors
from Surface import Surface



# class BasicRect: # -> has-a relationship
#     def __init__(self, surface, x: float, y:float, w:float, h:float, color : tuple) -> None:
#         self.rect = Rect(x, y, w, h)
#         self.surface = surface
#         self.color = list(color)


#     def draw(self):
#         pygame.draw.rect(self.surface.surface(), self.color, self.rect)

class BasicRect(BaseObject): # -> is-a relationship
    def __init__(self, surface: Surface, x: float, y: float, w : float, h : float, color : tuple) -> None:
        super().__init__(surface, x, y)
        self.rect = Rect(x, y, w, h)
        self.color = list(color)


    def draw(self):
        pygame.draw.rect(self.surface.surface(), self.color, self.rect)

class Laser(BaseObject):
    def __init__(self, surface: Surface, x: float, y: float) -> None:
        super().__init__(surface, x, y)

        self.rect = Rect(x, y, 2, 5)
        self.color = list(colors.RED)
        self.speed = 6.28


    def draw(self):
        pygame.draw.rect(self.surface.surface(), self.color, self.rect)

    def move(self):
        self.y -= self.speed
        self.rect.y = self.y




class Player(BaseObject):
    def __init__(self, surface: Surface, x: float, y: float, w : float, h : float, color : tuple) -> None:
        super().__init__(surface, x, y)
        self.rect = Rect(x, y, w, h)
        self.color = list(color)
        self.speed = 3.14

    def draw(self):
        pygame.draw.rect(self.surface.surface(), self.color, self.rect)

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


def main():
    # surface = pygame.display.set_mode(consants.SIZE)
    # pygame.display.set_caption("Test Project")

    surface = Surface(consants.SIZE, "My new Title", 60)
    test_obj = BasicRect(surface, 100, 100, 50, 50, colors.BLUE)

    surface.set_color(colors.BLACK)

    # surface.set_caption("I changed the caption")

    player = Player(surface, 150, 150, 50, 50, colors.ORANGE)
    lasers = []

    while True:
        ### Event Handling ###
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                print("quit code: ", pygame.QUIT)
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT: surface.set_size((500, 500))
                if event.key == pygame.K_RSHIFT: surface.set_size(consants.SIZE)
                # if event.key == pygame.K_LALT: surface.set_color(colors.RED)
                # if event.key == pygame.K_LCTRL: surface.set_color(colors.GREEN)
                if event.key == pygame.K_SPACE: 
                    # player_pos = player.shoot()
                    lasers.append(player.shoot())
                    print(len(lasers))


        
        player.move()
        for i in lasers: i.move()

        ### object handling

        ### surface handling
        # surface.surface.fill(colors.RED) # represent a color (0 - 255, 0 - 255, 0 - 255) -> r g b
        # test_obj.draw()
        # pygame.display.flip()

        surface.draw([player] + lasers)


if __name__ == "__main__": main()
