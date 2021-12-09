import pygame
from BaseObject import BaseObject
from Surface import Surface

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


