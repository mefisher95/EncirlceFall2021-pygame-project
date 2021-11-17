import pygame, sys
from random import randint
from pygame import constants

from BaseObject import BaseObject
from Laser import Laser, Lasers
import consants, colors
from Surface import Surface
from Player import Player


def main():
    surface = Surface(consants.SIZE, "My new Title", 60)
    surface.set_color(colors.BLACK)

    player = Player(surface)
    lasers = Lasers()

    while True:
        ### Event Handling ###
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT: surface.set_size((500, 500))
                if event.key == pygame.K_RSHIFT: surface.set_size(consants.SIZE)
                if event.key == pygame.K_SPACE: 
                    lasers.add(player.shoot()) ### add lasers to container
                    print(len(lasers)) #### add in len method


        
        player.move()
        lasers.move()
        # for laser in lasers: #### handle group movement
        #     laser.move()
        ### object handling

        ### surface handling
        surface.draw([player] + [lasers]) # handle batch drawing


if __name__ == "__main__": main()
