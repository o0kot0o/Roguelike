__author__ = 'Kot'
import libtcodpy as libtcod
from Tile import Tile

color_dark_wall   = libtcod.Color(  0,   0, 100)
color_dark_ground = libtcod.Color( 50,  50, 150)

class Map:
    def __init__(self, map_width, map_height):
        self.map = None
        self.map_width = map_width
        self.map_height = map_height

    def create_map(self):
        self.map = [[ Tile(False)
                    for y in range(self.map_height)]
                        for x in range(self.map_width)]
        return self.map

    def render(self, con):
        for y in range(self.map_height):
            for x in range(self.map_width):
                wall = self.map[x][y].block_sight
                if wall:
                    libtcod.console_set_char_background(con, x, y, color_dark_wall, libtcod.BKGND_SET)
                else:
                    libtcod.console_set_char_background(con, x, y, color_dark_ground, libtcod.BKGND_SET)