__author__ = 'Kot'
import libtcodpy as libtcod
from Entity import Entity


class Player(Entity):
    def __init__(self, name, x, y, char, keylist):
        Entity.__init__(self, name, x, y, char, libtcod.white, keylist)
        self.color = libtcod.white

    def update(self):
        if self.keylist[ord('w')] == True:
            self.y -= 1
        elif self.keylist[ord('s')] == True:
            self.y += 1
        elif self.keylist[ord('d')] == True:
            self.x += 1
        elif self.keylist[ord('a')] == True:
            self.x -= 1



