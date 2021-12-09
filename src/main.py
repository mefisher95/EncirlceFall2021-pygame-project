import pygame

import constants, colors

from Surface import Surface
from Stars import Stars

from game_states import main_menu, play_state

def main():
    pygame.init()

    surface = Surface(constants.SIZE, "My new Title", 60)
    surface.set_color(colors.BLACK)
    
    stars = Stars(surface)

    state = 2

    while True:
        if state == 0: state = play_state(surface, stars)
        if state == 1: return
        if state == 2: state = main_menu(surface, stars)


if __name__ == "__main__": main()
