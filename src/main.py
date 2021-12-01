import pygame, sys
from random import randint
from pygame import constants
from AquaAlien import AquaAlien, AquaFleet

from BaseObject import BaseObject
from Laser import Laser, Lasers
import constants, colors
from Surface import Surface
from Player import Player
from Stars import Star, Stars
from AlienBaseObject import AlienBaseObject

from general_functions import collide

def collide_player_lasers(aliens, lasers):
    for laser in lasers.objects:
        if laser.is_player():
            for ship in aliens.objects:
                if collide(ship, laser):
                    ship.kill()
                    laser.kill()


def collide_aliens_lasers(player, lasers):
    for laser in lasers.objects:
        if not laser.is_player():
            if collide(player, laser):
                player.kill()
                laser.kill()


def main():
    surface = Surface(constants.SIZE, "My new Title", 60)
    surface.set_color(colors.BLACK)

    player = Player(surface)
    lasers = Lasers()

    aquafleet = AquaFleet(surface, lasers)
    stars = Stars(surface)

    worldObj = [player, aquafleet, lasers, stars]

    while True:
        ### Event Handling ###
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT: surface.set_size((500, 500))
                if event.key == pygame.K_RSHIFT: surface.set_size(constants.SIZE)
                if event.key == pygame.K_SPACE: 
                    lasers.add(player.shoot()) ### add lasers to container
                    print(len(lasers)) #### add in len method


        
        # player.move()
        # alien.move()
        # lasers.move()
        # stars.move()

        # collide_container(lasers, aquafleet)
        collide_player_lasers(aquafleet, lasers)
        collide_aliens_lasers(player, lasers)

        aquafleet.attack()


        for items in worldObj:
            items.move()
        # for laser in lasers: #### handle group movement
        #     laser.move()
        ### object handling

        ### surface handling
        surface.draw(worldObj) # handle batch drawing


if __name__ == "__main__": main()
