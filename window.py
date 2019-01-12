##Ty Dawson - Untitled Python Project 2018-2019
##
##Window.py - Object containing all game graphics


##Imports

import pygame, sys, random, player
from pygame.locals import *


##Window Class
    ##Arguments: Width, Height, Title, Menu, Scene


class window(object):

    
    
    def __init__(self, windowWidth, windowHeight):
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight


        ##Title of Window
        self.title = "Ty's Pygame Prototype"
        pygame.display.set_caption(self.title)


        ##Actual Window Frame **Refresh "frame"
        self.frame = pygame.display.set_mode((windowWidth, windowHeight))


    ##GET/SET Functions for Vars

    def getWidth(self):
        return self.windowWidth

    def setWidth(self, newWidth):
        self.windowWidth = newWidth

    def getHeight(self):
        return self.windowHeight

    def setHeight(self, newHeight):
        self.windowHeight = newHeight

    


    def getBoundaries(self, n):
        return self.boundaries[n]

    def setBoundaries(self, newBoundaries):
        self.boundaries = newBoundaries




    ## -- -- -- -- -- ##
    ##Position Monitor## (X, Y) Coordinates, Direction, Jump Height
    ## -- -- -- -- -- ##


    def positionMonitor(self, player):


        ##Character Hitbox Coordinates
        font = pygame.font.SysFont("Arial, Times New Roman", 20)

        
        topLXY = font.render("TopL X: " + str(player.getX()) + ##Top left corner of Player hitbox
                             "/TopL Y: " + str(player.getY()),
                             True, (0,0,0))

        topRXY = font.render("TopR X: " + str(player.getX() + player.getWidth()) + ##Top right
                             "/TopR Y: " + str(player.getY()),
                             True, (0,0,0))

        btmLXY = font.render("BtmL X: " + str(player.getX()) + ##Bottom left
                             "/BtmL Y: " + str(player.getY() + player.getHeight()),
                             True, (0,0,0))

        btmRXY = font.render("BtmR X: " + str(player.getX() + player.getWidth()) + ##Bottom right
                             "/BtmR Y: " + str(player.getY() + player.getHeight()),
                             True, (0,0,0))

        origin = font.render("Origin X/Y: " + str(player.getOriginalX()) + ", " + ##Original coordinates prior to jump
                             str(player.getOriginalY()),
                             True, (0,0,0))

        jumpHeight = font.render("Jump Height: " + str(player.getJumpHeight()), ##Distance from originalY
                                 True, (0,0,0))
        

        

    
        ##Booleans
        direction = font.render("Facing right: " + str(player.getFacing()), True, (0, 255, 0))

        jumpCheck = font.render("Jump: " + str(player.getJump()), True, (255,0,0))


        ##Boundary test functions
        boundaryText = font.render("BOUNDARY SPACE", True, (0,0,0))



        ##Boundary Background Shapes

        pygame.draw.rect(self.frame, (200,0,200),
                         (player.getBoundaries(0), player.getBoundaries(1),
                          (player.getBoundaries(3) - player.getBoundaries(0) ),
                          (player.getBoundaries(2) - player.getBoundaries(1) ) ) )
     

        ##Text Blits -- SHOWS WHAT IS ONSCREEN
    
        self.frame.blit(direction, (0, 540))
        self.frame.blit(jumpCheck, (0, 560))
        self.frame.blit(boundaryText, (self.getHeight() / 2,self.getWidth() / 2))
    
        #self.frame.blit(origin, (500, 0))
        #self.frame.blit(jumpHeight, (500, 20))
        self.frame.blit(topLXY, (0,0))
        self.frame.blit(topRXY, (0,20))
        self.frame.blit(btmLXY, (0,40))
        self.frame.blit(btmRXY, (0,60))

    


    ##!!##!!##!!##!!##!!##!!##!!##!!##
    ##Refresh Game Window Graphics!!##       Refreshs game window with objects
    ##!!##!!##!!##!!##!!##!!##!!##!!##


    def refreshWindow(self, player):



        ##CURRENT BACKGROUND
        self.frame.fill((255,255,255))
        
        
        ##DEBUG MENU
        self.positionMonitor(player)

        
        
        
        ##Key press & Draw Player functions
        player.playerMotion()
        player.playerAction()
        
        player.drawSelf(self.frame)
        player.drawShadow(self.frame)
        player.drawAction(self.frame)

        
    

    
        pygame.display.update()

    
