#! /usr/bin/env python
#######################################
#     Author : Dhruv Khattar         #
#####################################

import pygame
import Person

""" Screen constants """
HEIGHT = 780
WIDTH = 1500

class Player(Person.Person):
    """ The Person that the user controls """
    def __init__(self):
        """ Constructor Function """
        """ Calling Parent constructor """
        Person.Person.__init__(self,"Player.png")
       
        """ Initial Speed of player """
        self.change_x = 0
        self.change_y = 0

        """ Adding Sounds """
        self.jump_sound = pygame.mixer.Sound("sounds/jump.ogg")

        self.level = None

    def update(self,ctr):
        """ Function to update Location of Player """
        
        """ Checking if Player is on a Ladder """
        flag = self.checkLadder()

        """Enabling and Disabling Gravity """
        if not flag :
            self.checkGravity()
        else:
            """ Checking for going down the Ladder """
            if self.change_y >= 0 and ctr==0:
                self.rect.y += 1
                ladders_hit = pygame.sprite.spritecollide(self,self.level.ladders,False)
                self.rect.y -= 1
                if len(ladders_hit) > 0:
                    self.rect.bottom == ladders_hit[0].rect.top
                    self.change_y = 0

        """ Checking collisions between Walls and Player """
        self.checkWall()

   
    def getPosition(self):
        return (self.rect.x,self.rect.y)

    def checkGravity(self):
        """ Gravity Function """
        if self.change_y == 0:
            self.change_y=1
        else:
            self.change_y += 0.3

        """ Checking if Player has reached Ground """
        if self.rect.y >= HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = HEIGHT - self.rect.height
    
    def checkWall(self):
        """ Collision checker """

        """ Movement in X Direction"""
        self.rect.x += self.change_x
        
        """ Checking Collisions """
        blocks_hit = pygame.sprite.spritecollide(self,self.level.walls,False)
        brokenladders_hit = pygame.sprite.spritecollide(self,self.level.brokenladders1,False)
        
        for block in blocks_hit:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right

        for block in brokenladders_hit:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right
        
        """ Movement in Y Direction """
        self.rect.y += self.change_y
        
        """Checking Collisions """
        blocks_hit = pygame.sprite.spritecollide(self,self.level.walls,False)
        brokenladders_hit = pygame.sprite.spritecollide(self,self.level.brokenladders1,False)
        
        for block in blocks_hit:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
            
            """Stop the vertical movement"""
            self.change_y = 0
        
        for block in brokenladders_hit:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            """Stop the vertical movement"""
            self.change_y = 0

    
    def checkLadder(self):
        """ Checks if the Player is on the Ladder """
        self.rect.y += 1
        ladders_hit = pygame.sprite.spritecollide(self,self.level.ladders,False)
        self.rect.y -= 1

        if len(ladders_hit) > 0:
            return 1

    """ Player controlled movements """

    def jump(self):
        """ Called when SPACE is pressed . Implements Jump """

        """ Checking if Player is standing on a Platform """
        self.rect.y += 1
        walls_hit = pygame.sprite.spritecollide(self,self.level.walls,False)
        ladders_hit = pygame.sprite.spritecollide(self,self.level.ladders,False)
        brokenladders_hit = pygame.sprite.spritecollide(self,self.level.brokenladders1,False)
        self.rect.y -= 1

        if len(walls_hit) > 0 or len(ladders_hit) > 0 or len(brokenladders_hit) > 0 :
            self.change_y = -9.5
            self.jump_sound.play()

    def goUp(self):
        """ Called when 'a' is pressed. Player goes up if he is on a Ladder """
        
        """ Checking if Player is on a Ladder """
        self.rect.y -= 1 
        ladders_hit = pygame.sprite.spritecollide(self,self.level.ladders,False)
        self.rect.y += 1

        if len(ladders_hit) > 0 :
            self.change_y = -3

    def goDown(self):
        """ Called when 's' is pressed. Player goes down if he is on a Ladder """
        
        """ Checking if Player is on a Ladder """
        self.rect.y += 1
        ladders_hit = pygame.sprite.spritecollide(self,self.level.ladders,False)
        self.rect.y -= 1

        if len(ladders_hit) > 0 :
            self.change_y = 3
            self.rect.y += self.change_y

    """ Called when user lets off the key """
    def stopX(self):
        """ Changes the horizontal speed to 0"""
        self.change_x = 0
    
    def stopY(self):
        """ Changes the vertical speed to 0"""
        self.change_y = 0
