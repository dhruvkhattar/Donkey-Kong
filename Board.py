#! /usr/bin/env python
#######################################
#     Author : Dhruv Khattar         #
#####################################

import pygame
import random

import NonMovingObjects
import Donkey
import Ladder

""" Declaring Screen Constants """
WIDTH = 1350
HEIGHT = 780
BLOCK = 30

class Board(object):
    """ Decides how the Level and the Board will look like """
    def __init__(self,player):
        """ Constructor Function """
    
        """ Creating Sprite Groups """
        self.walls = pygame.sprite.Group()
        self.ladders = pygame.sprite.Group()
        self.fullladders = pygame.sprite.Group()
        self.brokenladders1 = pygame.sprite.Group()
        self.brokenladders2 = pygame.sprite.Group()
        self.brokenladders3 = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.queen = pygame.sprite.Group()
        self.life = pygame.sprite.Group()

        self.background = None

        """Generating Random Numbers for Random Walls"""
        r1 = random.randint(150/BLOCK,(WIDTH/2)/BLOCK)*BLOCK
        r2 = random.randint(150/BLOCK,(WIDTH/2)/BLOCK)*BLOCK
        r3 = random.randint(150/BLOCK,(WIDTH/2)/BLOCK)*BLOCK
        r4 = random.randint(150/BLOCK,(WIDTH/2)/BLOCK)*BLOCK
        r5 = random.randint(150/BLOCK,(WIDTH/2)/BLOCK)*BLOCK
        self.queenplatform = random.randint(150/BLOCK,(WIDTH/2)/BLOCK)*BLOCK
      
        """ Generating Random Ladders """
        l1 = (random.randint(1,(1050-r2)/BLOCK))*BLOCK
        l2 = (random.randint(1,(WIDTH-r3-r2)/BLOCK))*BLOCK
        l3 = (random.randint(1,(WIDTH-r3-r4)/BLOCK))*BLOCK
        l4 = (random.randint(1,(WIDTH-r5-r4)/BLOCK))*BLOCK
        l5 = (random.randint(1,(r5-BLOCK)/BLOCK))*BLOCK
        l6 = (random.randint(1,240/BLOCK))*BLOCK

        """ Generating Random Ladders """
        b1 = (random.randint(1,(1050-r2)/BLOCK))*BLOCK
        b2 = (random.randint(1,(WIDTH-r3-r2)/BLOCK))*BLOCK
        b3 = (random.randint(1,(WIDTH-r3-r4)/BLOCK))*BLOCK
        b4 = (random.randint(1,(WIDTH-r5-r4)/BLOCK))*BLOCK
        b5 = (random.randint(1,(r5-BLOCK)/BLOCK))*BLOCK
        b6 = (random.randint(1,240/BLOCK))*BLOCK
       
        """ List for Walls dimensions and cordinates"""
        self.level_walls = [[WIDTH,BLOCK,0,HEIGHT-BLOCK],
                [WIDTH,BLOCK,BLOCK,0],
                [BLOCK,HEIGHT,0,0],
                [BLOCK,HEIGHT,WIDTH-BLOCK,0],
                [1050,BLOCK,BLOCK,150],
                [WIDTH-r2,BLOCK,r2,270],
                [WIDTH-r3,BLOCK,BLOCK,390],
                [WIDTH-r4,BLOCK,r4,510],
                [WIDTH-r5,BLOCK,BLOCK,630],
                [300,BLOCK,self.queenplatform,60],
                [BLOCK,BLOCK,self.queenplatform,BLOCK],
                [BLOCK,BLOCK,self.queenplatform+300,BLOCK],
                ]

        """ List for Ladders cordinates"""
        self.level_ladders = [[BLOCK+r2+l1,150-2],
                [r2+l2,270-2],
                [r4+l3,390-2],
                [r4+l4,510-2],
                [BLOCK+l5,630-2],
                [self.queenplatform+l6,60-2]
                ]
        
        """ List for Broken Ladders cordinates"""
        self.level_broken_ladders = [[BLOCK+r2+b1,150],
                [r2+b2,270],
                [r4+b3,390],
                [r4+b4,510],
                [BLOCK+b5,630]
                ]

        """ List for Walls Y-cordinate """
        self.ground = [630,510,390,270,150]

        """ Creating Ladders and Walls """
        self.createObjects()
        
        """ Removing Walls and Ladders """
        self.removeObjects()
        
    def createObjects(self):
        """ Creates Walls and Ladders"""
        
        """ Creating Walls """ 
        for cordinate in self.level_walls:
            if cordinate[0] == BLOCK:
                y = cordinate[3]
                while y <= cordinate[1] + cordinate[3]:
                    wall = NonMovingObjects.Wall()
                    wall.rect.x = cordinate[2]
                    wall.rect.y = y
                    self.walls.add(wall)
                    y += BLOCK
               
            elif cordinate[1] == BLOCK:
                x = cordinate[2]
                while x <= cordinate[2] + cordinate[0]:
                    wall = NonMovingObjects.Wall()
                    wall.rect.x = x
                    wall.rect.y = cordinate[3]
                    self.walls.add(wall)
                    x += BLOCK

        """ Creating Ladders"""
        for cordinate in self.level_ladders:
            ladder = Ladder.Ladder(1)
            ladder.rect.x = cordinate[0]
            ladder.rect.y = cordinate[1]
            self.ladders.add(ladder)
            self.fullladders.add(ladder)
        
        """ Creating Broken Ladders"""
        for cordinate in self.level_broken_ladders:
            broken_ladder = Ladder.BrokenLadder1()
            broken_ladder.rect.x = cordinate[0]
            broken_ladder.rect.y = cordinate[1]
            self.brokenladders1.add(broken_ladder)

            broken_ladder = Ladder.BrokenLadder2()
            broken_ladder.rect.x = cordinate[0]
            broken_ladder.rect.y = cordinate[1]+BLOCK-1
            self.brokenladders2.add(broken_ladder)

            broken_ladder = Ladder.Ladder(0)
            broken_ladder.rect.x = cordinate[0]
            broken_ladder.rect.y = cordinate[1]+BLOCK*3
            self.ladders.add(broken_ladder)
            self.brokenladders3.add(broken_ladder)
        
        """ Adding Coins"""
        for i in range(40):
            x = random.randint(BLOCK,WIDTH-60)
            
            coin = NonMovingObjects.Coin()
            coin.rect.x = x
            coin.rect.y = self.ground[i%5]-BLOCK
            self.coins.add(coin)

        """ Making Queen"""
        queen = NonMovingObjects.Queen()
        queen.rect.x = random.randint(self.queenplatform+BLOCK,self.queenplatform+270)
        queen.rect.y = BLOCK
        self.queen.add(queen)

        """ Adding Extra Life """

        life = NonMovingObjects.Life()
        life.rect.x = random.randint(1,WIDTH)
        life.rect.y = BLOCK
        self.life.add(life)

    def removeObjects(self):
        """ Removes unwanted Objects """

        """ Removing some of the Broken Ladders to make the Board look good """
        for ladder in self.ladders:
            ladder.rect.x += 1
            brokenladders1_removed = pygame.sprite.spritecollide(ladder,self.brokenladders1,True)
            brokenladders2_removed = pygame.sprite.spritecollide(ladder,self.brokenladders2,True)
            ladder.rect.x -= 1
            
            ladder.rect.x -= 1
            brokenladders1_removed = pygame.sprite.spritecollide(ladder,self.brokenladders1,True)
            brokenladders2_removed = pygame.sprite.spritecollide(ladder,self.brokenladders2,True)
            ladder.rect.x += 1
            
        for ladder in self.fullladders:
            ladder.rect.x += 1
            brokenladders3_removed = pygame.sprite.spritecollide(ladder,self.brokenladders3,True)
            ladder.rect.x -= 1
            
            ladder.rect.x -= 1
            brokenladders3_removed = pygame.sprite.spritecollide(ladder,self.brokenladders3,True)
            ladder.rect.x += 1

            self.ladders.remove(brokenladders3_removed)
        
        """ Removing Walls behind Ladders"""
        for ladder in self.ladders:
            walls_removed = pygame.sprite.spritecollide(ladder,self.walls,True)
         
        for ladder in self.brokenladders1:
            walls_removed = pygame.sprite.spritecollide(ladder,self.walls,True)

        for wall in self.walls:
            life_removed = pygame.sprite.spritecollide(wall,self.life,True)

    def draw(self,screen):
        """ The main drawing function """

        """ Draw the background """
        screen.fill((135,206,235))

        """ Draw all the sprites that we have """
        self.walls.draw(screen)
        self.ladders.draw(screen)
        self.brokenladders1.draw(screen)
        self.brokenladders2.draw(screen)
        self.coins.draw(screen)
        self.queen.draw(screen)
        self.life.draw(screen)
