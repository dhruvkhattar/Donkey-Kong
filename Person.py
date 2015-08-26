#! /usr/bin/env python
#######################################
#     Author : Dhruv Khattar         #
#####################################

import pygame
import SpriteObject

class Person(SpriteObject.SpriteObject):
    """ The Main Human Class"""
    def __init__(self,image_location):
        """ Constructor Function"""
        SpriteObject.SpriteObject.__init__(self,image_location)
    
    """ Function to change speed of Donkey and Player """
    def goRight(self):
        """ Change speed to right direction """
        self.change_x = 6 
    
    def goLeft(self):
        """ Change speed to left direction """
        self.change_x = -6
