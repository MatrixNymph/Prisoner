#!/usr/bin/env python

from random import getrandbits
import libtcodpy as libtcod
import os.path

class CAgen:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.cellGrid = [[ getrandbits(1)
            for _y in range(y) ]
                for _x in range(x) ]

    def randomize(self):
        for y in range(self.y):
            for x in range(self.x):
                self.cellGrid[x][y] = getrandbits(1)

    def setrules(self, under, over, repro):
        self.under = under
        self.over = over
        self.repro = repro

    def iterate(self, i):
        tempgrid = self.cellGrid
        for y in range(self.y - 1):
            for x in range(self.x - 1):
                tempgrid[x][y] = self.check([x, y])
        self.cellGrid = tempgrid
        if i > 1:
            self.iterate(i - 1)

    def check(self, cell): #cell should be (x, y) ordered pair
        alive = []
        for y in range(cell[1] - 1, cell[1] + 2):
            if y < 0 or y > len(self.cellGrid[0]):
                continue
            for x in range(cell[0] - 1, cell[0] + 2):
                if x < 0 or x > len(self.cellGrid):
                    continue
                elif [x, y] == cell:
                    continue
                else:
                    if self.cellGrid[x][y] == 1 or self.cellGrid[x][y] == 1L:
                        alive.append([x, y])

        if self.cellGrid[cell[0]][cell[1]] == 1L:
            if len(alive) <= self.under or len(alive) >= self.over:
                return 0L
            else:
                return 1L
        elif self.cellGrid[cell[0]][cell[1]] == 0L:
            if len(alive) == self.repro:
                return 1L
            else:
                return 0L
        
    def render(self):
        libtcod.console_set_default_foreground(0, libtcod.white)
        libtcod.console_set_custom_font(os.path.join('resources', 'fonts', 'arial12x12.png'), libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
        libtcod.console_init_root(self.x, self.y, 'CAgen', False)

        while not libtcod.console_is_window_closed():
            for y in range(self.y - 1):
                for x in range(self.x - 1):
                    if self.cellGrid[x][y] == 1L:
                        libtcod.console_put_char(0, x, y, '1', libtcod.BKGND_NONE)
                    else:
                        libtcod.console_put_char(0, x, y, ' ', libtcod.BKGND_NONE)
                        
            libtcod.console_flush()
            key = libtcod.console_wait_for_keypress(True)
            if key.vk == libtcod.KEY_ESCAPE:
                break
            if key.vk == libtcod.KEY_UP:
                self.iterate(1)

    def save(self, fileloc):
        outFile = open(fileloc, 'w')
        for y in range(len(self.cellGrid[0])):
            for x in range(len(self.cellGrid)):
                outFile.write(str(self.cellGrid[x][y]))
            outFile.write('\n')
        outFile.close()
