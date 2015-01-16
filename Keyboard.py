__author__ = 'Kot'

import libtcodpy as libtcod

class Keyboard:
    def __init__(self, keylist):
        self.keylist = keylist

    def update(self):
        key = libtcod.console_check_for_keypress(libtcod.KEY_PRESSED | libtcod.KEY_RELEASED)
        if key.vk != libtcod.KEY_NONE:
            if key.pressed == True:
                print(key.c)
                self.keylist[key.c] = True
            elif key.pressed == False:
                self.keylist[key.c] = False

        return self.keylist