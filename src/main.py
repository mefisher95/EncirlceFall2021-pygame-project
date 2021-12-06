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


class Text(BaseObject):
    def __init__(self, string: str, color: tuple, font: pygame.font.Font, surface: Surface, x: float, y: float) -> None:
        super().__init__(surface, x, y)

        self.font = font
        self.string = string
        self.text_str = font.render(self.string, False, color)
        
        self.rect = self.text_str.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        self.surface.surface().blit(self.text_str, self.rect)

    def recolor(self, color):
        self.text_str = self.font.render(self.string, False, color)



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

def obj_center(obj: BaseObject):
    obj_width = obj.rect.w
    obj.rect.x = constants.width / 2 - obj_width / 2

def play_state(surface, stars):


    player = Player(surface)
    lasers = Lasers()

    aquafleet = AquaFleet(surface, lasers)

    worldObj = [player, aquafleet, lasers, stars]

    while player.is_alive() and len(aquafleet) > 0:
        ### Event Handling ###
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

        ### surface handling
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
        # surface.surface().blit(text, text_rect)
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

        

    # play_state(surface)
    print(main_menu(surface))

if __name__ == "__main__": main()
