#! /usr/bin/env python
#######################################
#     Author : Dhruv Khattar         #
#####################################

import pygame
import SpriteObject

""" Width and Block size of the Screen"""
WIDTH = 1350
BLOCK = 30

class Fireball(SpriteObject.SpriteObject):
    """Fireballs : Weapon of Donkey"""
    def __init__(self):
        """ Constructor Function """
        """ Calling Parent's constructor """
        SpriteObject.SpriteObject.__init__(self,"Fireball.png")

        """ Fireball's initial Velocity"""
        self.change_x = 0
        self.change_y = 10

        """Adding Sounds"""
        fireball_sound = pygame.mixer.Sound("sounds/fireball.ogg")
        fireball_sound.play()

        self.level = None

    def update(self,ctr):
        """ Function to update location """

        """ Editing Fireball's location """
        self.rect.y += self.change_y
        self.rect.x += self.change_x

        """ Reversing direction of Fireball """
        if self.rect.x >= WIDTH - 2*BLOCK:
            self.change_x = -4                
        if self.rect.x <= BLOCK:
            self.change_x = 4
        
    
        """Checking if Fireball is on a Wall """
        walls_hit = pygame.sprite.spritecollide(self,self.level.walls,False)
        for wall in walls_hit:
            if self.change_y > 0:
                self.rect.bottom = wall.rect.top
            elif self.change_y < 0:
                self.rect.top = wall.rect.bottom
