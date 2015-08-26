#! /usr/bin/env python
#######################################
#     Author : Dhruv Khattar         #
#####################################

import pygame
import SpriteObject

class Coin(SpriteObject.SpriteObject):
    """ Coins : 5 points per coin"""
    """ Constructor Function """
    def __init__(self):
        """ Initializing Sprite """
        SpriteObject.SpriteObject.__init__(self,"Coin.png")

class Life(SpriteObject.SpriteObject):
    """ Extra Life """
    """ Constructor Function """
    def __init__(self):
        """ Initializing Sprite """
        SpriteObject.SpriteObject.__init__(self,"Heart.png")

class Wall(SpriteObject.SpriteObject):
    """ The brick platforms and walls """
    """ Constructor Function """
    def __init__(self):
        """ Initializing Sprite """
        SpriteObject.SpriteObject.__init__(self,"Brick.png")

class Queen(SpriteObject.SpriteObject):
    """ Queen : the one to be saved"""
    """ Constructor Function """
    def __init__(self):
        """ Initializing Sprite """
        SpriteObject.SpriteObject.__init__(self,"Queen.png")
