from general_functions import collide


class ObjectContainer:
    def __init__(self) -> None:
        self.objects = []

    def draw(self) -> None:
        for obj in self.objects: obj.draw()
        return None

    def move(self) -> None:
        for obj in self.objects: obj.move()    
        self.objects = [ obj for obj in self.objects if obj.is_alive() ]

        return None

    def add(self, obj) -> None:
        self.objects.append(obj)
        return None

    def __len__(self) -> int: return len(self.objects)


def collide_container(container0, container1):
    for obj0 in container0.objects:
        for obj1 in container1.objects:
            if collide(obj0, obj1):
                obj0.kill()
                obj1.kill()