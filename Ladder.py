#! /usr/bin/env python
#######################################
#     Author : Dhruv Khattar         #
#####################################

import pygame

class Ladder(pygame.sprite.Sprite):
    """ Ladders : Player can climb up these """
    def __init__(self,flag):
        """ Constructor Function """
        """ Initializing Sprites """
        pygame.sprite.Sprite.__init__(self)

        """ Loading Ladder's Image """
        """ checking Flag for image size"""
        if flag == 1:
            self.image = pygame.image.load("images/Ladder.png").convert()
            self.image.set_colorkey((0,0,0))
        else:
            self.image = pygame.image.load("images/Broken3.png").convert()
            self.image.set_colorkey((0,0,0))

        self.rect = self.image.get_rect()

class BrokenLadder1(pygame.sprite.Sprite):
    """ Broken Ladders Part 1"""
    def __init__(self):
        """ Constructor Function """
        """ Initializing Sprites """
        pygame.sprite.Sprite.__init__(self)

        """ Loading Broken Ladder Image """
        self.image = pygame.image.load("images/Broken21.png").convert()
        self.image.set_colorkey((0,0,0))

        self.rect = self.image.get_rect()

class BrokenLadder2(pygame.sprite.Sprite):
    """ Broken Ladders Part 2"""
    def __init__(self):
        """ Constructor Function """
        """ Initializing Sprites """
        pygame.sprite.Sprite.__init__(self)

        """ Loading Broken Ladder Image """
        self.image = pygame.image.load("images/Broken22.png").convert()
        self.image.set_colorkey((0,0,0))

        self.rect = self.image.get_rect()
