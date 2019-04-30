##Ty Dawson - Python Project 2018-2019
##
##Enemy.py - Enemy attributes and actions


##Imports

import pygame, random

##Enemy Class:
    ##Arguments: Self, Position, Width, Height, Style, HealthPoints


class enemy(pygame.rect.Rect):
    
    def __init__(self):
        
        self.x = 800 + random.randint(0, 800)
        self.y = random.randint(160, 400)
        
        self.originalX = 800
        
        
        self.width = 40
        self.height = 40
        
        self.x2 = self.x + self.width
        self.y2 = self.y + self.height
        
        self.style = 0
        self.styleNo = [0, ##Default, spawns from right, moves straight
                        1, ##Spawns from left, moves straight
                        2, ##Boss spawn from the right
                        3] ##Boss spawn from the left
                        
        
        self.bounce = 1
        
        self.hp = 50
        self.death = False
        
        
        self.boundaries = [80, 160,  ##Top left XY
                           500, 720] ##bottom right YX
        
        self.enemySpawn = [800 + random.randint(40, 200), random.randint(160, 320)]

        self.enemySizes = [40, 80]
        
        
        self.hitbox = (self.x, self.y, 
                       self.width, self.height)
        
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.bigHitbox = pygame.Rect(self.x, self.y, self.width * 2, self.height * 2)
                                  
        self.spriteList = [pygame.image.load('sprites/snake1.png'),
                           pygame.image.load('sprites/snake2.png'),
                           pygame.image.load('sprites/snake1_reverse.png'),
                           pygame.image.load('sprites/snake2_reverse.png'),
                           pygame.image.load('sprites/big_snake1.png'),
                           pygame.image.load('sprites/big_snake2.png'),
                           pygame.image.load('sprites/big_snake1_reverse.png'),
                           pygame.image.load('sprites/big_snake2_reverse.png')]
        
        
    
    def setX(self, x):
        self.x = x 
        
    def getX(self):
        return self.x 
    
    def setY(self, y):
        self.y = y
        
    def getY(self):   
        return self.y

    def getX2(self):
        return self.x2
    
    def getY2(self):
        return self.y2
    
    def getXY(self):
        return (self.getX(), self.getY())
    
    def getRect(self):
        return self.getXY() + (self.getWidth(), self.getHeight())
    
    def getCoordinates(self):
        return self.getXY() + (self.getX2(), self.getY2())

    def setWidth(self, w):
        self.width = w

    def getWidth(self):
        return self.width
    
    def setHeight(self, h):
        self.height = h
    
    def getHeight(self):
        return self.height
    
    def setStyle(self, s):
        self.style = self.styleNo[s]
        
    def getStyle(self):
        return self.style
    
    def setBounce(self):
        self.bounce = self.bounce * -1
    
    def getHitbox(self):
        return self.hitbox
    
    def getEnemyCount(self):
        return self.enemyCount
    
    def setEnemyCount(self, n):
        self.enemyCount = n
    
    def getHP(self):
        return self.hp
    
    def setHP(self, h):
        self.hp = h
    
    def getDeath(self):
        return self.death
    
    def setDeath(self, d):
        self.death = d
    
    
    ## -- -- -- -- ##
    ## Draw enemy onto plane and move
    
    def drawEnemy(self, window):
        
        
        ##Check Sprite path style
    
        ##From the right (default)
        if(self.getStyle() == 0):
            if(self.getX() % 100 <= 50):
                window.frame.blit(self.spriteList[1], 
                                 (self.getX(), self.getY()))        
            
            elif(self.getX() % 100 > 50): 
                window.frame.blit(self.spriteList[0], 
                                 (self.getX(), self.getY()))
            
            self.enemyTrail()


        ##From the left
        if(self.getStyle() == 1):
            if(self.getX() % 100 <= 50):
                window.frame.blit(self.spriteList[3], 
                                 (self.getX(), self.getY()))        
           
            elif(self.getX() % 100 > 50): 
                window.frame.blit(self.spriteList[2], 
                                 (self.getX(), self.getY()))
            
            self.enemyTrail()
    
    
        ##Boss from the right
        if(self.getStyle() == 2):
            if(self.getX() % 100 == 0):
                window.frame.blit(self.spriteList[5], 
                                 (self.getX(), self.getY()))        
            
            else: window.frame.blit(self.spriteList[4], 
                                   (self.getX(), self.getY()))
            
            self.enemyTrail()
    
        ##Boss from the left
        if(self.getStyle() == 3):
            if(self.getX() % 100 == 0):
                window.frame.blit(self.spriteList[7], 
                                 (self.getX(), self.getY()))        
            
            else: window.frame.blit(self.spriteList[6], 
                                   (self.getX(), self.getY()))
            
            self.enemyTrail()
        


    def enemyTrail(self):
        
        
        if(self.getDeath() == False):
            
            if(self.getStyle() == 0):
                self.setX(self.getX() - 4)
                            
                
            if(self.getStyle() == 1):
                self.setX(self.getX() + 4)
                            
        
            if(self.getStyle() == 2):
                self.setX(self.getX() - 2)
        
                
            if(self.getStyle() == 3):
                self.setX(self.getX() + 2)
                            
                   
        else: 
            self.setX(800)
            self.setY(600)
        
            
            
            
                
                