__author__ = 'Kot'
__name__ = 'Roguelike'

import libtcodpy as libtcod

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

# KEYS
KEYLIST = [[False] for i in range(255)]

playerx = SCREEN_WIDTH  / 2
playery = SCREEN_HEIGHT / 2

libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Roguelike', False)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

libtcod.sys_set_fps(LIMIT_FPS)

class Keyboard:
    global KEYLIST

    def update(self):
        key = libtcod.console_check_for_keypress(libtcod.KEY_PRESSED | libtcod.KEY_RELEASED)
        if key.vk != libtcod.KEY_NONE:
            if key.pressed == True:
                print(key.c)
                KEYLIST[key.c] = True
            elif key.pressed == False:
                KEYLIST[key.c] = False


def handle_keys():
    global playerx, playery

kb = Keyboard()

while not libtcod.console_is_window_closed():
    libtcod.console_set_default_foreground(con, libtcod.white)
    libtcod.console_put_char(con, playerx, playery, '@', libtcod.BKGND_NONE)


    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
    libtcod.console_flush()

    kb.update()

    libtcod.console_put_char(con, playerx, playery, ' ', libtcod.BKGND_NONE)

    if KEYLIST[ord('w')] == True:
        playery -= 1
    elif KEYLIST[ord('s')] == True:
        playery += 1
    elif KEYLIST[ord('d')] == True:
        playerx += 1
    elif KEYLIST[ord('a')] == True:
        playerx -= 1

    libtcod.sys_set_fps(LIMIT_FPS)

