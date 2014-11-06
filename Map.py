#!/usr/bin/env python

import libtcodpy as libtcod
import Color
from ConsoleHandler import ConsoleHandler

from Tile import Tile

class Map:

    def __init__(self , width, height):
        self.size = [width, height]

        self.data = [[ Tile(False)
            for y in range(height) ]
                for x in range(width) ]

    def render(self, console):
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                wall = self.data[x][y].block_sight

                if wall:
                    console.draw(Color.dark_wall, x, y)
                else:
                    console.draw(Color.dark_ground, x, y)

    def load(self, fileloc):
        inFile = open(fileloc, 'r')
        inData = inFile.readlines()
        formattedData = [list() for _ in range(len(inData[0]) - 1)]

        for y in range(len(inData)):
            for x in range(len([char for char in inData[y]]) - 1): # -1 avoids taking in newline characters
                formattedData[x].append([char for char in inData[y]][x])

        for x in range(len(formattedData)):
            for y in range(len(formattedData[0])):
                if int(formattedData[x][y]) == 1:
                    self.data[x][y].blocked = True
                    self.data[x][y].block_sight = True
                elif int(formattedData[x][y]) == 0:
                    self.data[x][y].blocked = False
                    self.data[x][y].block_sight = False
                












