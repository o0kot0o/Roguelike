__author__ = 'Kot'
import libtcodpy as libtcod
from Entity import Entity


class Player(Entity):
    def __init__(self, name, x, y, keylist):
        Entity.__init__(self, name, x, y, keylist)

    def update(self):
        if self.keylist[ord('w')] == True:
            self.y -= 1
        if self.keylist[ord('s')] == True:
            self.y += 1
        if self.keylist[ord('d')] == True:
            self.x += 1
        if self.keylist[ord('a')] == True:
            self.x -= 1

    def render(self, con):
        #TODO: DO THIS :)
        libtcod.console_set_default_foreground(con, libtcod.white)
        libtcod.console_put_char(con, self.x, self.y, '@', libtcod.BKGND_NONE)

