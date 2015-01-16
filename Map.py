__author__ = 'Kot'
import libtcodpy as libtcod
from Tile import Tile
from Utility import Colors
from random import randint

class Map:
    def __init__(self, map_width, map_height):
        self.map = None
        self.map_width = map_width
        self.map_height = map_height

    def create_map(self):
        self.map = [[ Tile(False)
                    for y in range(self.map_height)]
                        for x in range(self.map_width+1)]
        return self.map

    def load_map(self, filename):
        self.create_map()
        lf = open(filename, 'r')
        x = 0
        y = 0
        for line in lf:
            x = 0
            for char in line:
                if char is '#':
                    print("(X:%d)-(Y:%d)") % (x, y)
                    self.map[x][y] = Tile(True)
                else:
                    type = randint(0, 15)
                    if type >= 0 and type <= 1:
                        self.map[x][y] = Tile(False, color=Colors['DIRT'])
                    else:
                        self.map[x][y] = Tile(False, color=Colors['GRASS'])
                x += 1
            y += 1

        return self.map

    def render(self, con):
        for y in range(self.map_height):
            for x in range(self.map_width):
                wall = self.map[x][y].block_sight
                if wall:
                    libtcod.console_set_char_background(con, x, y, Colors['WALL_DARK'], libtcod.BKGND_SET)
                else:
                    libtcod.console_set_char_background(con, x, y, self.map[x][y].color, libtcod.BKGND_SET)