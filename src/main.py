import pygame, sys
from random import randint

from pygame.rect import Rect
from pygame.sprite import collide_rect

import consants, colors
from Surface import Surface



class BasicRect:
    def __init__(self, surface, x: float, y:float, w:float, h:float, color : tuple) -> None:
        self.rect = Rect(x, y, w, h)
        self.surface = surface
        self.color = list(color)


    def draw(self):
        pygame.draw.rect(self.surface.surface(), self.color, self.rect)

def main():
    # surface = pygame.display.set_mode(consants.SIZE)
    # pygame.display.set_caption("Test Project")

    surface = Surface(consants.SIZE, "My new Title", 60)
    test_obj = BasicRect(surface, 100, 100, 50, 50, colors.BLUE)

    surface.set_color(colors.GREEN)

    surface.set_caption("I changed the caption")

    while True:
        ### Event Handling ###
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                print("quit code: ", pygame.QUIT)
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT: surface.set_size((500, 500))
                if event.key == pygame.K_RSHIFT: surface.set_size(consants.SIZE)
                if event.key == pygame.K_LALT: surface.set_color(colors.RED)
                if event.key == pygame.K_LCTRL: surface.set_color(colors.GREEN)


        ### object handling

        ### surface handling
        # surface.surface.fill(colors.RED) # represent a color (0 - 255, 0 - 255, 0 - 255) -> r g b
        # test_obj.draw()
        # pygame.display.flip()

        surface.draw([test_obj])


if __name__ == "__main__": main()
