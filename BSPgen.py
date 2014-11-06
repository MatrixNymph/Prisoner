#!/usr/bin/env python

from random import getrandbits, randint
import libtcodpy as libtcod

class BSPgen:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.cellGrid = [[ getrandbits(1)
            for _y in range(y) ]
                for _x in range(x) ]

    def iterate(self, i):
        direction = getrandbits(1)
        if direction == 0: #Horizontal
            start = randint(len(self.cellGrid))
            for each in range(len(self.cellGrid[0])):
                
        if direction == 1: #Vertical
            start = randint(len(self.cellGrid[0]))

    def randomize(self):

    def render(self):

    def save(self, fileLoc):
