#!/usr/bin/env python

from Object import Object
from Map import Map
from ConsoleHandler import ConsoleHandler

from os.path import join
import libtcodpy as libtcod

con = ConsoleHandler(133, 66, join('resources', 'fonts', 'arial12x12.png'))

def handle_keys():

    key = libtcod.console_wait_for_keypress(True)
    #movement keys
    if libtcod.console_is_key_pressed(libtcod.KEY_UP) or libtcod.console_is_key_pressed(libtcod.KEY_KP8):
        player.move(0, -1)
 
    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN) or libtcod.console_is_key_pressed(libtcod.KEY_KP2):
        player.move(0, 1)
 
    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT) or libtcod.console_is_key_pressed(libtcod.KEY_KP4):
        player.move(-1, 0)
 
    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT) or libtcod.console_is_key_pressed(libtcod.KEY_KP6):
        player.move(1, 0)

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        # Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

    elif key.vk == libtcod.KEY_ESCAPE:
        return True

player = Object(con.SCREEN_WIDTH/2, con.SCREEN_HEIGHT/2, '@', libtcod.white)
npc = Object(con.SCREEN_WIDTH/2 - 5, con.SCREEN_HEIGHT/2, '@', libtcod.yellow)
Objects = [npc, player]
Mapdata = Map(133, 66)
Mapdata.load('test.txt')

while not libtcod.console_is_window_closed():

    Mapdata.render(con)    
    con.blit()
    for obj in Objects:
        con.draw(obj)
    con.blit()

    for obj in Objects:
        con.clear(obj)

    libtcod.console_flush()
    exit = handle_keys()
    if exit:
        break


