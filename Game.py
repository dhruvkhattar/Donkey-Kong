#!/usr/bin/env python
#######################################
#     Author : Dhruv Khattar         #
#####################################

""" Importing libararies """
import pygame
import os
import sys
import time
import random

""" Importing Modules """
import Person
import Player
import Donkey
import Board
import Fireball

"""Declaring Screen Dimensions """
WIDTH = 1350
HEIGHT = 780
BLOCK = 30

class Game(object):
    """ This class represents an instance of the game. """
    """If we want to restart the game , then we just need to create a new instance of this class. """
    
    def __init__(self,score,lives,level):
        """ Constructor Function: called automatically when an instance of the class is created """
        
        """Creating Player """
        self.player = Player.Player()
    
        """ Creating a List for Donkey and Fireballs"""
        self.fireball_sprites = pygame.sprite.Group()

        """ Declaring Current Level """
        self.current_level = Board.Board(self.player)

        """ Creating various Sprite Groups """
        self.moving_sprites = pygame.sprite.Group()
        self.donkey_sprites = pygame.sprite.Group()
        self.player.level = self.current_level

        """ Player's initial Location """
        self.player.rect.x = 30
        self.player.rect.y = HEIGHT - self.player.rect.height-30
        
        """Adding Player in moving_sprites to make updates easy"""
        self.moving_sprites.add(self.player)

        """ List that contains random numbers for turning Donkey """
        self.donkeyturn = []

        """ Creating Donkey and adding it to lists """
        for i in range(0,level):
            donkey = Donkey.Donkey()
        
            """Donkey's initial Location"""
            donkey.rect.x = 30+30*i
            donkey.rect.y = 120
        
            """Adding Donkey in various lists"""
            self.donkey_sprites.add(donkey)
            self.donkeyturn.append(random.randint(100,200))
            self.moving_sprites.add(donkey)
    
        """ For restarting and respawing """
        self.game_over = False
        self.game_win = False

        """ Score Lives Level """
        self.level = level
        self.score = score
        self.lives = lives

        """ Flag to check when 'a' or 's' is pressed """
        self.flag = 0

        """ Counter to randomize things """
        self.counter = 0


    def checkCollision(self):
        """ Checks Collision netween Player and fireball_sprites """

        """ Checking if Fireball hits Player"""
        kill_hit = pygame.sprite.spritecollide(self.player,self.fireball_sprites,True)
        if len(kill_hit) > 0:
            """ Lost a Life """
            self.ouch_sound.play()
            self.game_over = True
        
        """ Checking if Donkey hits Player"""
        donkey_hit = pygame.sprite.spritecollide(self.player,self.donkey_sprites,True)
        if len(donkey_hit) > 0:
            """ Ending Game """
            self.gameover_sound.play()
            self.game_over = True
            self.lives = 1


    def collectCoin(self):
        """ Checks if Player collects a coin and increases the score by 5"""

        coins_hit = pygame.sprite.spritecollide(self.player,self.player.level.coins,True)
        if len(coins_hit) > 0:
            self.score += len(coins_hit)*5
            self.coin_sound.play()

    
    def collectLife(self):
        """ Checks if Player collects a heart and gains a life"""

        hearts_hit = pygame.sprite.spritecollide(self.player,self.player.level.life,True)
        if len(hearts_hit) > 0:
            self.lives += 1
            self.extralife_sound.play()

    
    def checkWin(self):
        """ Checks if the Player has saved the Queen """

        queen_hit = pygame.sprite.spritecollide(self.player,self.player.level.queen, True)

        if len(queen_hit) > 0:
            """Player wins the Game"""
            self.game_win = True
            self.win_sound.play()


    def editFireball(self):
        """ Creates and Destroys Fireballs"""
       
        """ Removing Fireballs when they reach the Player's spawn position """
        for fireball in self.fireball_sprites:
            if fireball.rect.y == HEIGHT - 60 and fireball.rect.x < 45:
                self.fireball_sprites.remove(fireball)
                self.moving_sprites.remove(fireball)
                
        """ Counter to randomize Fireballs produced by Donkey"""
        if self.counter%200 == 0:
            
            for donkey in self.donkey_sprites:
            
                """ Creating a new Fireball"""
                self.fireball = Fireball.Fireball()
            
                """ Setting the initial Fireball cordinates to Donkey's cordinates"""
                self.fireball.rect.x = donkey.rect.x
                self.fireball.rect.y = donkey.rect.y
                self.fireball.level = self.current_level
                
                """Setting Fireballs initial vector"""
                if donkey.change_x > 0:
                    self.fireball.change_x = 4
                else:
                    self.fireball.change_x = -4

                """ Adding Fireball to moving_sprites and fireball_sprites"""
                self.moving_sprites.add(self.fireball)
                self.fireball_sprites.add(self.fireball)


    def turnDonkey(self):
        """ Function that turns Donkey randomly """

        i = 0
        for donkey in self.donkey_sprites:
            if self.counter%self.donkeyturn[i] == 0:
                donkey.change_x *= -1
                self.donkeyturn[i] = random.randint(100,200)
                i += 1


    def process_Events(self):
        """ Processes all the events and returns True if we Game needs to be Quit """
        
        for event in pygame.event.get():
            """ If Window's closed"""
            if event.type == pygame.QUIT:
                return True
            
            """ If a key is pressed"""
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return True
                if event.key == pygame.K_a:
                    self.player.goLeft()
                if event.key == pygame.K_d:
                    self.player.goRight()
                if event.key == pygame.K_w:
                    self.flag = 1
                    self.player.goUp()
                if event.key == pygame.K_s:
                    self.flag = 1
                    self.player.goDown()
                if event.key == pygame.K_SPACE:
                    self.player.jump()
                if event.key == pygame.K_c:
                    if self.game_over and self.lives==1:
                        self.__init__(0,3,1)
                if event.key == pygame.K_RETURN:
                    if self.game_win:
                        self.__init__(self.score+50,self.lives,self.level+1)

            """ If a key pressed is left"""
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and self.player.change_x < 0:
                    self.player.stopX()
                if event.key == pygame.K_d and self.player.change_x > 0:
                    self.player.stopX()
                if event.key == pygame.K_w :
                    self.flag = 0
                    self.player.stopY()
                if event.key == pygame.K_s :
                    self.flag = 0
                    self.player.stopY()
        
        return False


    def respawn(self):
        """ Respawns Player in the bottom left corner """
        self.game_over = False
        self.score -= 25
        self.lives -= 1
        self.player.rect.x = BLOCK
        self.player.rect.y = HEIGHT - 2*BLOCK


    def updateSprites(self):
        """Updates various Sprites"""
        self.moving_sprites.update(self.flag)


    def drawFrame(self,screen):
        """Draws the Screen"""

        if self.game_win:
            font = pygame.font.Font(None,100)
            text1 = font.render("YOU WIN ", 1 , (0,0,0))
            text2 = font.render("Press ENTER to continue", 1 , (0,0,0))
            textpos1 = text1.get_rect(centerx=WIDTH/2,centery=HEIGHT/2-50)
            textpos2 = text2.get_rect(centerx=WIDTH/2,centery=HEIGHT/2+50)
            screen.blit(text1,textpos1)
            screen.blit(text2,textpos2)
        elif not self.game_over:
            self.current_level.draw(screen)
            self.moving_sprites.draw(screen)
            font = pygame.font.Font(None,36)
            text = font.render("SCORE: %s  LIVES: %s  LEVEL: %s" % (self.score ,self.lives,self.level), 1 , (0,0,0))
            screen.blit(text,[0,HEIGHT-30])
        else:
            font = pygame.font.Font(None,100)
            if self.lives > 1:
                text = font.render("LIVES LEFT: %s " % (self.lives - 1) , 1 , (0,0,0))
                self.respawn()
                textpos = text.get_rect(centerx=WIDTH/2,centery=HEIGHT/2)
                screen.blit(text,textpos)
                pygame.display.flip()
                time.sleep(0.5)
            else:
                back = pygame.image.load("images/DKback.jpg")
                screen.blit(back,(0,0))
                text1 = font.render("YOU LOSE " , 1 , (0,0,0))
                text2 = font.render("SCORE : %s" % self.score , 1 , (0,0,0))
                text3 = font.render("Press C to Restart" , 1 , (0,0,0))
                textpos1 = text1.get_rect(centerx=WIDTH/2,centery=HEIGHT/2-100)
                textpos2 = text2.get_rect(centerx=WIDTH/2,centery=HEIGHT/2)
                textpos3 = text3.get_rect(centerx=WIDTH/2,centery=HEIGHT/2+100)
                screen.blit(text1,textpos1)
                screen.blit(text2,textpos2)
                screen.blit(text3,textpos3)
        
        """ Updating the screen i.e. Showing the changes done in this iteration """
        pygame.display.flip()


""" Main Program """
def main():
    """ Initializing PyGame """
    pygame.init()

    """ Initializing Screen """
    screen = pygame.display.set_mode((WIDTH,HEIGHT))

    """ Setting Title of the Game"""
    pygame.display.set_caption("Donkey Kong")
   
    """ FPS """
    clock = pygame.time.Clock()
   
    """ Counter to check if Game is closed"""
    done = False

    """ Adding intro sound """
    intro = pygame.mixer.Sound("sounds/intro.wav")
    intro.play()

    """ Printing Rules of the Game """
    font = pygame.font.Font(None,70)
    font.set_bold(True)

    title = pygame.font.Font(None,100).render(" DONKEY KONG ", 1, (0,255,0))
    name = pygame.font.Font(None , 40).render("created by : Dhruv Khattar", 1, (0,255,0))
    rule = font.render(" Rules ", 1 , (0,0,0))
    rule1 = font.render(" - To win the Game , you just have to save the Queen.", 1 , (0,0,0))
    rule2 = font.render(" - Player can not climb up a broken Ladder.", 1 , (0,0,0))
    rule3 = font.render(" - Coins give you 5 points each." , 1, (0,0,0))
    rule4 = font.render(" - Heart gives you an extra life. " , 1 , (0,0,0))
    rule5 = font.render(" - Winning a game gives you 50 points. " , 1 , (0,0,0))
    rule6 = font.render(" - If you get hit by a Fireball, you'll respawn , " , 1 , (0,0,0))
    rule7 = font.render("    loose a life and get penalized with 25 points. " , 1 , (0,0,0))
    rule8 = font.render(" - If you get hit by a Donkey , then you lose the game. " , 1 , (0,0,0))
    rule9 = font.render(" - Press any key to play. " , 1 , (0,0,0))
    
    titlepos = title.get_rect(centerx=WIDTH/2,centery=HEIGHT/2-300)
    namepos = name.get_rect(centerx=WIDTH/2,centery=HEIGHT/2-220)
    rulepos = rule.get_rect(centerx=WIDTH/2,centery=HEIGHT/2-180)
    textpos1 = rule1.get_rect(centery=HEIGHT/2-120)
    textpos2 = rule2.get_rect(centery=HEIGHT/2-60)
    textpos3 = rule3.get_rect(centery=HEIGHT/2)
    textpos4 = rule4.get_rect(centery=HEIGHT/2+60)
    textpos5 = rule5.get_rect(centery=HEIGHT/2+120)
    textpos6 = rule6.get_rect(centery=HEIGHT/2+180)
    textpos7 = rule7.get_rect(centery=HEIGHT/2+240)
    textpos8 = rule8.get_rect(centery=HEIGHT/2+300)
    textpos9 = rule9.get_rect(centery=HEIGHT/2+360)
    
    back = pygame.image.load("images/DKback.jpg")
    screen.blit(back,(0,0))
    screen.blit(name,namepos)
    screen.blit(title,titlepos)
    screen.blit(rule1,textpos1)
    screen.blit(rule2,textpos2)
    screen.blit(rule3,textpos3)
    screen.blit(rule4,textpos4)
    screen.blit(rule5,textpos5)
    screen.blit(rule6,textpos6)
    screen.blit(rule7,textpos7)
    screen.blit(rule8,textpos8)
    screen.blit(rule9,textpos9)

    pygame.display.flip()

    flag = 0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                flag = 1
        if flag:
            break

    """ Initializing Game """
    game = Game(0,3,1)
    
    """ Adding Sounds """
    game.ouch_sound = pygame.mixer.Sound("sounds/ouch.ogg")
    game.coin_sound = pygame.mixer.Sound("sounds/coin.ogg")
    game.win_sound = pygame.mixer.Sound("sounds/win.ogg")
    game.gameover_sound = pygame.mixer.Sound("sounds/gameover.ogg")
    game.extralife_sound = pygame.mixer.Sound("sounds/extralife.ogg")
    pygame.mixer.music.load("sounds/bacmusic.wav")

    pygame.mixer.music.play(-1)
    
    """ Main Program Loop """
    while not done:
        
        """ Process Key Strokes """
        done = game.process_Events()
        
        """Adding Fireballs"""
        game.editFireball()
        
        """ Randomizing turning of Donkey """
        game.turnDonkey()
        
        """ Update Sprites """
        game.updateSprites()
        
        """ Checking if Player collects a Coin """
        game.collectCoin()
        
        """ Checking if Player gains a life """
        game.collectLife()

        """ Checking if Player dies """
        game.checkCollision()
        
        """ Checking if Player Wins the Game """
        game.checkWin()
        
        """ Drawing the Screen """
        game.drawFrame(screen)
        
        """ FPS Pause for the next Frame"""
        clock.tick(60)

        """ Incrementing counter """
        game.counter += 1

""" Close Screen and exit """
pygame.quit()


if __name__ == "__main__":
    main()
