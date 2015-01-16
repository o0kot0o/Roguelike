__author__ = 'Kot'
__name__ = 'Roguelike'

import libtcodpy as libtcod
from Keyboard import Keyboard
from Player import Player

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

# KEYS
KEYLIST = [[False] for i in range(255)]

libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Roguelike', False)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

libtcod.sys_set_fps(LIMIT_FPS)

kb = Keyboard(KEYLIST)
player = Player('player', SCREEN_WIDTH/2, SCREEN_HEIGHT/2, KEYLIST)

while not libtcod.console_is_window_closed():
    libtcod.console_set_default_foreground(con, libtcod.white)
    libtcod.console_put_char(con, player.x, player.y, '@', libtcod.BKGND_NONE)


    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
    libtcod.console_flush()

    KEYLIST = kb.update()

    libtcod.console_put_char(con, player.x, player.y, ' ', libtcod.BKGND_NONE)

    player.update()

    libtcod.sys_set_fps(LIMIT_FPS)

