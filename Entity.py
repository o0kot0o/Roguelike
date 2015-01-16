__author__ = 'Kot'
import libtcodpy as libtcod

class Entity(object):
    def __init__(self, name, x, y, char, color, keylist=None):
        self.name = name
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.keylist = keylist

    def update(self):
        return

    def render(self, con):
        libtcod.console_set_default_foreground(con, self.color)
        libtcod.console_put_char(con, self.x, self.y, '@', libtcod.BKGND_NONE)