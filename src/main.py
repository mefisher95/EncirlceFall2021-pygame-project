import sys, pygame, consants
from pygame import color
from pygame.mixer import pause
from pygame import Rect, event
from random import randint

class play_object:
    def __init__(self, surface, x, y, width, height, color = consants.BLUE) -> None:
        self.surface = surface
        self.rect = Rect(x, y, width, height)
        self.color = list(color)
        self.speed = 3.14
        self.timer = 0
        self.dir = 0

        self.__color_fade_choice = randint(0, 2)
        self.__color_fade_value = 1

    def move(self) -> None:

        if self.timer >= 20:
            self.timer = 0

            self.dir = randint(0, 3)
        else: self.timer += 1
        print(self.timer)

        if self.dir == 0 and self.rect.left >= 0: 
            self.rect.x -= self.speed
        if self.dir == 1 and self.rect.right <= consants.SIZE[0]: 
            self.rect.x += self.speed
        if self.dir == 2 and self.rect.top >= 0: 
            self.rect.y -= self.speed
        if self.dir == 3 and self.rect.bottom <= consants.SIZE[1]: 
            self.rect.y += self.speed

        return None
    def draw(self):
        self.__color_fade()
        print(self.color)
        pygame.draw.rect(self.surface, self.color, test_obj)

    def __color_fade(self):
        print(self.__color_fade_choice, self.color)
        if self.color[self.__color_fade_choice] >= 250:
            self.__color_fade_value = -1
        if self.color[self.__color_fade_choice] <= 10:
            self.__color_fade_value = 1
        self.color[self.__color_fade_choice] += self.__color_fade_value
            


screen = pygame.display.set_mode(consants.SIZE)
pygame.display.set_caption('Encirle Python')
test_obj = play_object(screen, 100, 100, 50, 50)
clock = pygame.time.Clock()

while 1:
    for events in event.get():
        if events.type == pygame.QUIT:
            print(pygame.QUIT)
            sys.exit()

    test_obj.move()
    
    screen.fill(consants.RED)
    # pygame.draw.rect(screen, consants.BLUE, test_obj)
    test_obj.draw()
    pygame.display.flip()

    clock.tick(60)
