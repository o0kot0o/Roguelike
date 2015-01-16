__author__ = 'Kot'
import libtcodpy as libtcod
from Entity import Entity


class Player(Entity):
    def __init__(self, name, x, y, char, mapdata, keylist):
        Entity.__init__(self, name, x, y, char, libtcod.white, mapdata, keylist)
        self.color = libtcod.white

    def update(self):
        dx = 0
        dy = 0
        if self.keylist[ord('w')] == True:
            dy = -1
        elif self.keylist[ord('s')] == True:
            dy = 1
        elif self.keylist[ord('d')] == True:
            dx = 1
        elif self.keylist[ord('a')] == True:
            dx = -1

        print(dy)
        self.move(dx, dy);

    def move(self, dx, dy):
        if not self.mapdata[self.x + dx][self.y + dy].blocked:
            print(self.x + dx)
            self.x += dx
            self.y += dy



