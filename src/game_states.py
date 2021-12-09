import pygame, sys

from AquaAlien import AquaFleet
from Laser import Lasers
import constants, colors
from Player import Player
from Text import Text

from general_functions import *


def play_state(surface, stars):
    player = Player(surface)
    lasers = Lasers()

    aquafleet = AquaFleet(surface, lasers)

    worldObj = [player, aquafleet, lasers, stars]

    while player.is_alive() and len(aquafleet) > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT: surface.set_size((500, 500))
                if event.key == pygame.K_RSHIFT: surface.set_size(constants.SIZE)
                if event.key == pygame.K_SPACE: 
                    lasers.add(player.shoot()) ### add lasers to container

        collide_player_lasers(aquafleet, lasers)
        collide_aliens_lasers(player, lasers)

        aquafleet.attack()


        for items in worldObj:
            items.move()

        surface.draw(worldObj) # handle batch drawing

    return 2


def main_menu(surface, stars) -> int:
    game_font = pygame.font.Font("./../fonts/space_age.ttf", 32)

    title_text = Text("Encircle Galaxish", colors.RED, game_font, surface, 0, constants.height / 2 - 200)
    Play_text = Text("Play", colors.RED, game_font, surface, 0, constants.height / 2 - 100)
    exit_text = Text("Exit", colors.RED, game_font, surface, 0, constants.height / 2)
    
    
    obj_center(title_text)
    obj_center(Play_text)
    obj_center(exit_text)

    text_list = [stars, title_text, Play_text, exit_text]

    pos = 0
    max_pos = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_s or event.key == pygame.K_DOWN)  and pos < max_pos: 
                    pos += 1
                if (event.key == pygame.K_w or event.key == pygame.K_UP) and pos > 0:
                    pos -= 1

                if (event.key == pygame.K_RETURN or event.key == pygame.K_SPACE): 
                    return pos

        if pos == 0:
            Play_text.recolor(colors.BLUE)
            exit_text.recolor(colors.RED)

        if pos == 1:
            Play_text.recolor(colors.RED)
            exit_text.recolor(colors.BLUE)

        stars.move()

        surface.draw(text_list)
