__author__ = 'Kot'
import libtcodpy as libtcod
from Entity import Entity
from Utility import Colors


class Player(Entity):
    def __init__(self, name, x, y, char, mapdata, keylist):
        Entity.__init__(self, name, x, y, char, libtcod.white, mapdata, keylist)
        self.color = libtcod.white

    def update(self):
        dx = 0
        dy = 0
        if self.keylist[ord('w')] == True:
            dy = -1
            self.lookAt = 2
        elif self.keylist[ord('s')] == True:
            dy = 1
            self.lookAt = 1
        elif self.keylist[ord('d')] == True:
            dx = 1
            self.lookAt = 4
        elif self.keylist[ord('a')] == True:
            dx = -1
            self.lookAt = 3

        print(dy)
        self.move(dx, dy);

    def move(self, dx, dy):
        if not self.mapdata[self.x + dx][self.y + dy].blocked:
            print(self.x + dx)
            self.x += dx
            self.y += dy

    def render(self, con):
        self.drawVisionLine(con)
        super(Player, self).render(con)

    def drawVisionLine(self, con):
        curx = self.x
        cury = self.y
        if self.lookAt == 2:
            while not self.mapdata[curx][cury].blocked:
                libtcod.console_put_char(con, curx, cury, Colors['LINE'], libtcod.BKGND_SET)
                cury -= 1
        elif self.lookAt == 1:
            while not self.mapdata[curx][cury].blocked:
                libtcod.console_put_char(con, curx, cury, Colors['LINE'], libtcod.BKGND_SET)
                cury += 1
        elif self.lookAt == 3:
            while not self.mapdata[curx][cury].blocked:
                libtcod.console_put_char(con, curx, cury, Colors['LINE'], libtcod.BKGND_SET)
                curx -= 1
        elif self.lookAt == 4:
            while not self.mapdata[curx][cury].blocked:
                libtcod.console_put_char(con, curx, cury, Colors['LINE'], libtcod.BKGND_SET)
                curx += 1