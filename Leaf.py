#!/usr/bin/env python

from random import getrandbits

class Leaf:
    def __init__(self, _x, _y, width, height):
        self.x = _x
        self.y = _y
        self.size = [width, height]

        self.leftChild = None
        self.rightChild = None
        
    def split(self):
        # Already split
        if (self.leftChild is not None or self.rightChild is not None):
            return false
        
        # If width > 25% larger than height, split vertically
        if self.width > (1.25 * height):
            split = 1
        # If height > 25% larger than width, split horizontally
        elif self.height > (1.25 * width):
            split = 0
        # Split randomly
        else:
            split = getrandbits(1)

        if split == 0:
            self.leftChild = Leaf(self.x, self.y, self.width, split)
            self.rightChild = Leaf(self.x, self.y + split, self.width, self.height - split)
        else:
            self.leftChild = Leaf(self.x, self.y, self.split, self.height)
            self.rightChild = Leaf(self.x + split, self.y, self.width - split, self.height)
        return True
