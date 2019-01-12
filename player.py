
import pygame, sys, random, resources, window, sprite
from pygame.locals import *


##Player Class:
    ##Arguments: Self, Position, Width, Height, Velocity, Booleans, Jump Vars


class player(object):

   
    def __init__(self, x, y, width, height):

        ##(X,Y) Variables
        self.x = x
        self.y = y

        self.originalX = x
        self.originalY = y

        
        self.width = width
        self.height = height
        

        self.centerX = x + (self.width/2)
        self.centerY = y + (self.height/2)

        
        ##(X, Y) Corner Boundaries for Playable Actor Space 
        ##[top left x, top left y, bottom right x, bottom right y]
        self.boundaries = [80, 200, 520, 720]
        self.spawn = [80, 320]

        
        ##Movement and Jump Vars
        self.velocity = 10
        self.facing = True

        
        self.negative = 1

        
        self.jump = False
        self.jumpCounter = 10
        self.jumpHeight = 0
        self.maxJumpHeight = 40

        self.punch = False
        self.kick = False


        ##Sprite Variables

        self.walkCount = 0
        


        
        

## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ##

##    Set and Get Functions

## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ##



    ##Coordinates Get/Set

    def setX(self, xVal):
        self.x = xVal

    def setY(self, yVal):
        self.y = yVal

    def setOriginalX(self, oxVal):
        self.originalX = oxVal

    def setOriginalY(self, oyVal):
        self.originalY = oyVal
        
    def setCenterX(self, center):
        self.centerX = center
        
    def setCenterY(self, center):
        self.centerY = center

    def setBoundaries(self, corner1, corner2, corner3, corner4):
        self.boundaries[0] = corner1
        self.boundaries[1] = corner2
        self.boundaries[2] = corner3
        self.boundaries[3] = corner4
        
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getOriginalX(self):
        return self.originalX

    def getOriginalY(self):
        return self.originalY
    
    def getCenterX(self):
        return self.centerX
    
    def getCenterY(self):
        return self.centerY

    def getBoundaries(self, corner):
        return self.boundaries[corner]

    



    ##Hitbox Get/Set

    def setWidth(self, newWidth):
        self.width = newWidth
        
    def setHeight(self, newHeight):
        self.height = newHeight

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height




    ##Jump Variable Set/Gets

    def getJump(self):
        return self.jump

    def setJump(self, jumpTrue):
        self.jump = jumpTrue
        
    def getJumpHeight(self):
        return (self.getOriginalY() - self.getY())
    
    def setJumpHeight(self, new):
        self.jumpHeight = new
        
    def getNegative(self):
        return self.negative

    def setNegative(self, negativeBool):
        if not(negativeBool):
            self.negative = 1
        else:
            self.negative = -1

    def getJumpCounter(self):
        return self.jumpCounter

    def setJumpCounter(self, counterVar):
        self.jumpCounter = counterVar

    
    
    
    ##Sprite Variables
    
    def getFacing(self):
        return self.facing

    def setFacing(self, facingBool):
        self.facing = facingBool




    ##Action Sets/Gets

    def getPunch(self):
        return self.punch

    def setPunch(self, punched):
        self.punch = punched

    def getKick(self):
        return self.kick

    def setKick(self, kicked):
        self.kick = kicked




## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ##


##KEY PRESS FUNCTIONS
#
# 1 - playerMotion
#
# 2 - playerAction


    def playerMotion(self):


        keys = pygame.key.get_pressed()
        

        ##Movement (WASD/Arrow) Keys In Action
    
        if ((keys[pygame.K_LEFT] or keys[pygame.K_a])
            and (self.getX() > self.boundaries[0])):
        
            self.setX(self.getX() - self.velocity)

            self.setOriginalX(self.getX())

            self.setFacing(False)
    
        if ((keys[pygame.K_RIGHT] or keys[pygame.K_d])
            and (self.getX() < self.boundaries[3] - self.getWidth())):
        
            self.setX(self.getX() + self.velocity)

            self.setOriginalX(self.getX())

            self.setFacing(True)  

        ##Can only JUMP moving HORIZONTALLY
        if not(self.getJump()):
            

            if ((keys[pygame.K_UP] or keys[pygame.K_w])
                and self.getOriginalY() > self.boundaries[1] - (self.getHeight() / 2)):
            
                self.setY(self.getY() - (self.velocity / 2))

                self.setOriginalY(self.getY())

            if ((keys[pygame.K_DOWN] or keys[pygame.K_s])
                and self.getOriginalY() < self.boundaries[2] - (self.getHeight() * 1.5)):
            
                self.setY(self.getY() + (self.velocity / 2))

                self.setOriginalY(self.getY())

            
            self.setJumpHeight(0)
            ##If SPACE is pressed
            if keys[pygame.K_SPACE]:
                self.setJump(True)

        else: ##Moving up and down WHILE jumping
            
            
            ##IF UP or W is pressed AND origin Y is greater than top boundary AND less than bottom boundary
            if ((keys[pygame.K_UP] or keys[pygame.K_w])
                and self.getOriginalY() > self.boundaries[1] - (self.getHeight() / 2)):
                
                self.setY(self.getY() - (self.velocity / 2))
                self.setOriginalY(self.getOriginalY() - (self.velocity / 2))
                self.setJumpHeight(self.getY() - self.getOriginalY())
                
            
            ##IF DOWN or S is pressed AND origin Y is less than bottom boundary and 
            if (keys[pygame.K_DOWN] or keys[pygame.K_s]
                and self.getOriginalY() < self.boundaries[2] - (self.getHeight() * 1.5)):
                
                self.setY(self.getY() + (self.velocity / 2))
                self.setOriginalY(self.getOriginalY() + (self.velocity / 2))
                self.setJumpHeight(self.getY() - self.getOriginalY())
                
                           
            
            
            ## ## ## ## ## ## 
            ## Jump equation 
            ## ## ## ## ## ##
            
            
            if self.getJumpCounter() >= -10:
                self.setNegative(False)
                if self.getJumpCounter() < 0:
                    self.setNegative(True)

                
                self.setY(self.getY() - 0.1 * (self.getJumpCounter() ** 2)* self.getNegative())
                self.setJumpCounter(self.getJumpCounter() - 1)

            else:
                self.setJump(False)
                self.setJumpCounter(10)




    ##playerAction Function

    def playerAction(self):


        keys = pygame.key.get_pressed()


        ##Fist of Fury / Foot of Mild Discontent - Retrieve Key Action


        if ((keys[pygame.K_0]) or (keys[pygame.K_q])):
            self.setKick(True)
            self.setPunch(False)
            
            
        if ((keys[pygame.K_LSHIFT]) or (keys[pygame.K_e])):
            self.setKick(False)
            self.setPunch(True)





    
    
## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ##
##
##  Draw Functions (Hitboxes)
##
## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ##
##       
## - - drawSelf
##
## - - drawShadow
##
## - - drawAction
##
##


    def drawSelf(self, windowFrame):


        
        ##Draw Direction of Player
    
        if(self.facing):
        
            ##Facing Right (True) (Default)
            pygame.draw.rect(windowFrame,
                             (0,255,255),
                             (self.getX(), self.getY(),
                              self.getWidth(), self.getHeight()))
            
            pygame.draw.rect(windowFrame,
                             (0,0,255), 
                             (self.getX() + (self.getWidth() / 2), self.getY(),
                              self.getWidth() / 2, self.getHeight()))
        else:

            ##Facing Left (False)
            
            pygame.draw.rect(windowFrame,
                             (0,0,255),
                             (self.getX(), self.getY(), self.getWidth(), self.getHeight()))
            pygame.draw.rect(windowFrame,
                             (0,255,255),
                             (self.getX() + (self.getWidth() / 2), self.getY(),
                              self.getWidth() / 2, self.getHeight()))





    def drawShadow(self, windowFrame):


        ##Draw Shadow of Player

        if(self.jump):
            
          
            ##Shadow Rect, must follow Player and shrink/grow as Player JUMPS
            shadowX = self.getX() + (self.getWidth() / 2) - (self.getJumpHeight() / 2)
            shadowY = (self.getOriginalY() + (self.getHeight()))
            shadowWidth = self.getJumpHeight()
            shadowHeight = self.getJumpHeight() / 2
            

            pygame.draw.ellipse(windowFrame,
                                (0,0,0),
                                [shadowX, shadowY, shadowWidth, shadowHeight])





    def drawAction(self, windowFrame):

        ##Draw Punch/Kick Hitboxes

        if(self.punch): ##If Punch button pressed
            
            if(self.facing): ##Facing Right by default
                pygame.draw.rect(windowFrame,
                                 (255,0,0),
                                 ((self.getX() + (self.getWidth() * 0.75)),
                                  (self.getY() + self.getHeight() / 4),
                                  (self.getWidth() / 2),
                                  (self.getHeight() /2)))
            else:
                pygame.draw.rect(windowFrame,
                                 (255,0,0),
                                 ((self.getX() - (self.getWidth() * 0.25)),
                                  (self.getY() + self.getHeight() / 4),
                                  (self.getWidth() / 2),
                                  (self.getHeight() /2)))
        self.setPunch(False)

        if(self.kick):
            
            if(self.facing): ##Facing Right by default
                pygame.draw.rect(windowFrame,
                                 (255,0,0),
                                 ((self.getX() + (self.getWidth() * 0.75)),
                                  (self.getY() + self.getHeight() / 2),
                                  (self.getWidth() / 2),
                                  (self.getHeight() /2)))
            else:
                pygame.draw.rect(windowFrame,
                                 (255,0,0),
                                 ((self.getX() - (self.getWidth() * 0.25)),
                                  (self.getY() + self.getHeight() / 2),
                                  (self.getWidth() / 2),
                                  (self.getHeight() /2)))
        self.setKick(False)
        
            


