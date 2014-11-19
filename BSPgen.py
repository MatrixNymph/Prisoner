#!/usr/bin/env python

from Leaf import Leaf

from random import getrandbits, randint
import libtcodpy as libtcod
import os.path

class BSPgen:
    def __init__(self, x, y, min, max):
        self.x = x
        self.y = y
        self.min_leaf_size = min
        self.max_leaf_size = max

        self.root = Leaf(0, 0, self.x, self.y, self.min_leaf_size)
        self.leaves = [self.root]

    def iterate(self, _i):
        newLeaves = []
	for i in range(_i):
            for leaf in self.leaves:
                if (leaf.leftChild == None and leaf.rightChild == None):
                    if (leaf.size[0] > self.max_leaf_size or leaf.size[1] > self.max_leaf_size or randint(1, 100) > 25):
                        if leaf.split():
                            newLeaves.append(leaf.leftChild)
                            newLeaves.append(leaf.rightChild)
        
        for leaf in newLeaves:
            self.leaves.append(leaf)
        
    def reset(self):
        self.root = Leaf(0, 0, self.x, self.y, self.min_leaf_size)
        self.leaves = []
        self.leaves.append(self.root)

    def render(self):
        libtcod.console_set_default_foreground(0, libtcod.white)
        libtcod.console_set_custom_font(os.path.join('resources', 'fonts' , 'arial12x12.png'), libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
        libtcod.console_init_root(self.x, self.y, 'BSPgen', False)

        while not libtcod.console_is_window_closed():
            for x in range(0, self.x):
                    for y in range(0, self.y):
                        libtcod.console_put_char(0, x, y, ' ', libtcod.BKGND_NONE)

            for leaf in self.leaves:
                for x in range(leaf.x, leaf.x + leaf.size[0]):
                    libtcod.console_put_char(0, x, leaf.y, '1', libtcod.BKGND_NONE)
                    libtcod.console_put_char(0, x, leaf.y + leaf.size[1], '1', libtcod.BKGND_NONE)
                for y in range(leaf.y, leaf.y + leaf.size[1]):
                    libtcod.console_put_char(0, leaf.x, y, '1', libtcod.BKGND_NONE)
                    libtcod.console_put_char(0, leaf.x + leaf.size[0], y, '1', libtcod.BKGND_NONE)

            libtcod.console_flush()
            key = libtcod.console_wait_for_keypress(True)
            if key.vk == libtcod.KEY_ESCAPE:
                break
            if key.vk == libtcod.KEY_UP:
                self.iterate(1)


    def save(self, fileLoc):
        return 0
