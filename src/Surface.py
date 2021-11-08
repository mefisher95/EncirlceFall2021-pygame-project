import pygame
import colors

class Surface:
    def __init__(self, size: tuple, caption: str, fps: int) -> None:
        self.__size = size
        self.__caption = caption
        self.__fill_color = colors.WHITE
        self.__fps = fps

        self.__surface = pygame.display.set_mode(self.__size)

        pygame.display.set_caption(self.__caption)
        self.__clock = pygame.time.Clock()
        

        return None
    
    def surface(self) -> pygame.Surface: return self.__surface

    def clear(self) -> None: self.surface().fill(self.__fill_color)

    def set_caption(self, str: str) -> None: pygame.display.set_caption(str)

    def set_size(self, size: tuple) -> None : self.__surface = pygame.display.set_mode(size)

    def set_color(self, color : tuple) -> None:
        self.__fill_color = color
        return None

    def draw(self, iterable : list) -> None: 
        self.surface().lock()
        self.clear()

        for obj in iterable:
            obj.draw()

        pygame.display.flip()
        self.surface().unlock()

        self.__clock.tick(self.__fps)

        return None