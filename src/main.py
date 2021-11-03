import pygame, sys
from random import randint

from pygame.rect import Rect

import consants, colors


# consants.SIZE = (1000, 1000)


# x, y, width, height
# test_obj = Rect(100, 100, 50, 50)

class BasicRect:
    def __init__(self, surface, x: float, y:float, w:float, h:float, color : tuple) -> None:
        self.rect = Rect(x, y, w, h)
        self.surface = surface
        self.color = list(color)


    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)

def main():
    surface = pygame.display.set_mode(consants.SIZE)
    pygame.display.set_caption("Test Project")

    test_obj = BasicRect(surface, 100, 100, 50, 50, colors.BLUE)

    while True:
        ### Event Handling ###
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                print("quit code: ", pygame.QUIT)
                sys.exit()

        ### object handling

        ### surface handling
        surface.fill(colors.RED) # represent a color (0 - 255, 0 - 255, 0 - 255) -> r g b
        test_obj.draw()
        pygame.display.flip()


if __name__ == "__main__": main()
