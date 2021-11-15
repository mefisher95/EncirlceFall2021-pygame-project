from Surface import Surface

class BaseObject:
    def __init__(self, surface: Surface, x: float, y: float) -> None:
        self.surface = surface
        self.x = x
        self.y = y
        
        return

    def draw(self): pass
    def move(self): pass
    def pos(self): return (self.x, self.y)
    def __str__(self) -> str: pass
    def __repr__(self) -> str: pass
    def addr(self) -> str: return hex(id(self))

def addr(obj) -> str: return obj.addr()