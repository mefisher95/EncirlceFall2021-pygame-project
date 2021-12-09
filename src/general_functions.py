from BaseObject import BaseObject
import constants


def collide(obj0, obj1) -> bool:
    return obj0.rect.colliderect(obj1.rect)


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