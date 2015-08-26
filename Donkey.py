#! /usr/bin/env python
#######################################
#     Author : Dhruv Khattar         #
#####################################

import pygame
import Person

BLOCK = 30

class Donkey(Person.Person):
    """Donkey : Villain of the Game """
    def __init__(self):
        """ The Constructor Function"""
        """ Calling Parent's constructor"""
        Person.Person.__init__(self,"DK.png")

        """ Setting the Initial Cordinates of Donkey"""
        self.rect.x = BLOCK
        self.rect.y = BLOCK*4

        """ Speed vector of Donkey """
        self.change_x = 3

    def update(self,ctr):
        """ Updating Donkey's Location """
    
        self.rect.x += self.change_x

        """ Changing Donkey's direction if it reaches the end of the platform"""
        if self.rect.x >= 1050:
            self.goLeft()
            self.change_x += 3

        if self.rect.x <= BLOCK:
            self.goRight() 
            self.change_x -= 3
