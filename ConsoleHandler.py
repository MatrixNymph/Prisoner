#!/usr/bin/env python

import libtcodpy as libtcod

class ConsoleHandler:

    def __init__(self, width, height, fnt):
        self.SCREEN_WIDTH = width
        self.SCREEN_HEIGHT = height
        self.font = fnt

        libtcod.console_set_custom_font(self.font, libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
        libtcod.console_init_root(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, 'python/libtcod tutorial', False)
        self.con = libtcod.console_new(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        
    def draw(self, *args):
        if len(args) == 1:
            obj = args[0]
            libtcod.console_set_default_foreground(self.con, obj.color)
            libtcod.console_put_char(self.con, obj.x, obj.y, obj.char, libtcod.BKGND_NONE)
        elif len(args) == 3:
            color = args[0]
            x = args[1]
            y = args[2]

            libtcod.console_put_char_ex(self.con, x, y, 0, color, color)
  
    def blit(self):
        libtcod.console_blit(self.con, 0, 0, self.SCREEN_WIDTH, self.SCREEN_HEIGHT, 0, 0, 0)
        libtcod.console_flush()

    def clear(self, obj):
        libtcod.console_put_char(self.con, obj.x, obj.y, ' ', libtcod.BKGND_NONE)
