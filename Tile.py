__author__ = 'Kot'
import libtcodpy as libtcod
from Utility import Colors

class Tile(object):
    def __init__(self, blocked, block_sight=None, color=None):
        self.blocked = blocked
        if block_sight is None:
            block_sight = blocked
        self.block_sight = block_sight
        if color is None:
            color = Colors['DIRT']
        self.color = color