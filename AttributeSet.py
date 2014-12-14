#!/usr/bin/env python

from random import randint

class AttributeSet:
    def __init__(self, *args):
        # Technical data
        self.fileLoc = " "

        # AttributeSet(fileLoc, [sides, num_dice, drop_mode, reroll_list])
        if len(args) == 1:
            self.fileLoc = args[0]
            self.load(args[0]) #fileLoc
        elif len(args) == 2:
            self.fileLoc = args[0]
            self.roll(args[1]) #rollRules
            
        # Attributes
        self.Strength = 
        self.Dexterity = 
        self.Intelligence = 
        self.Wisdom = 
        self.Perception = 
        self.Constitution =
        self.Affinity = 
        self.Willpower = 

        self.AttrSet = [
                        getAttr('strength'), getAttr('dexterity'), getAttr('intelligence'), getAttr('wisdom'),   
                        getAttr('perception'), getAttr('constitution'), getAttr('affinity'), getAttr('willpower')   
                       ]

    def roll([sides, num_dice, drop_mode, reroll_list]):
        ''' sides - number of sides on the dice to roll
            num_dice - number of dice to roll
            drop_mode - 1: drop lowest
                        2: drop highest
            reroll_list - list of numbers to reroll
                        eg [1, 2, 6]'''
        for attr in self.AttrSet:
                    
    def getAttr(self, attr):
        if (attr.lower() == 'strength'):
            return self.Strength
        elif (attr.lower() == 'dexterity'):
            return self.Dexterity
        elif (attr.lower() == 'intelligence'):
            return self.Intelligence
        elif (attr.lower() == 'wisdom'):
            return self.Wisdom
        elif (attr.lower() == 'perception'):
            return self.Perception
        elif (attr.lower() == 'constitution'):
            return self.Constitution
        elif (attr.lower() == 'affinity'):
            return self.Affinity
        elif (attr.lower() == 'willpower'):
            return self.Willpower

    def setAttr(self, attr, value):
        if (attr.lower() == 'strength'):
            self.Strength = value
        elif (attr.lower() == 'dexterity'):
            self.Dexterity = value
        elif (attr.lower() == 'intelligence'):
            self.Intelligence = value
        elif (attr.lower() == 'wisdom'):
            self.Wisdom = value
        elif (attr.lower() == 'perception'):
            self.Perception = value
        elif (attr.lower() == 'constitution'):
            self.Constitution = value
        elif (attr.lower() == 'affinity'):
            self.Affinity = value
        elif (attr.lower() == 'willpower'):
            self.Willpower = value

    
