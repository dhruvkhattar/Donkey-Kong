#! /usr/bin/env python
#######################################
#     Author : Dhruv Khattar         #
#####################################

import pygame
import os

class SpriteObject(pygame.sprite.Sprite):
    """ The Basic Sprite Object Class """
    """ Constructor Function """
    def __init__(self,image_location):
        """ Initializing Sprite Class """
        pygame.sprite.Sprite.__init__(self)

        """Loading Sprite's Image"""
        full_location = os.path.join("images",image_location)
        self.image = pygame.image.load(full_location).convert()
                         
        """ Removing Black Background of image """
        self.image.set_colorkey((0,0,0))

        """ Changing size of image """
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()
                                                                         
