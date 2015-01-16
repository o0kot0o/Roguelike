__author__ = 'Kot'
__name__ = 'Roguelike'

import libtcodpy as libtcod
from Keyboard import Keyboard
from Player import Player
from Entity import Entity
from Map import Map

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 15

MAP_WIDTH = 80
MAP_HEIGHT = 45

# KEYS
KEYLIST = [[False] for i in range(255)]

libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Roguelike', False)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

libtcod.sys_set_fps(LIMIT_FPS)

kb = Keyboard(KEYLIST)

mapO = Map(MAP_WIDTH, MAP_HEIGHT)

map = mapO.load_map('level1.lvl')

'''map = mapO.create_map()
map[30][22].blocked = True
map[30][22].block_sight = True
map[50][22].blocked = True
map[50][22].block_sight = True'''

player = Player('player', SCREEN_WIDTH/2, SCREEN_HEIGHT/2, '@', map, KEYLIST)
npc = Entity('npc', 10, 10, '@', libtcod.yellow, map)

entities = [npc, player]



while not libtcod.console_is_window_closed():
    libtcod.console_clear(con)

    KEYLIST = kb.update()

    mapO.render(con)

    for entity in entities:
        entity.update()

    for entity in entities:
        entity.render(con)

    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
    libtcod.console_flush()

