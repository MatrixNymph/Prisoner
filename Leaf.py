#!/usr/bin/env python

from random import randint

class Leaf:
    def __init__(self, _x, _y, width, height, min):
        self.x = _x
        self.y = _y
        self.size = [width, height]

        self.min_leaf_size = min

        self.leftChild = None
        self.rightChild = None
        
    def split(self):
        # Already split
        if (self.leftChild is not None or self.rightChild is not None):
            return False
        
        if (self.size[0] < self.min_leaf_size or self.size[1] < self.min_leaf_size):
            return False

        # If width > 25% larger than height, split vertically
        if self.size[0] > (1.25 * self.size[1]):
            dir = 1
        # If height > 25% larger than width, split horizontally
        elif self.size[1] > (1.25 * self.size[0]):
            dir = 0
        # Split randomly
        else:
            dir = randint(0, 1)

        if dir == 0:
            splitpt = randint(self.min_leaf_size, self.size[1])
        elif dir == 1:
            splitpt = randint(self.min_leaf_size, self.size[0])
        
        if dir == 0:
            self.leftChild = Leaf(self.x, self.y, self.size[0], splitpt, self.min_leaf_size)
            self.rightChild = Leaf(self.x, self.y + splitpt, self.size[0], self.size[1] - splitpt, self.min_leaf_size)
        else:
            self.leftChild = Leaf(self.x, self.y, splitpt, self.size[1], self.min_leaf_size)
            self.rightChild = Leaf(self.x + splitpt, self.y, self.size[0] - splitpt, self.size[1], self.min_leaf_size)
        return True
