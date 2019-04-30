
import pygame

##Player Class:
    ##Arguments: Self, Position, Width, Height, Velocity, Booleans, Jump Vars


class player(pygame.rect.Rect):

   
    def __init__(self, x, y, width, height):

        ##(X,Y) Variables
        self.x = x
        self.y = y
        self.x2 = self.x + self.width
        self.y2 = self.y + self.height

        self.originalX = x
        self.originalY = y

        
        self.width = width
        self.height = height
        
        
        self.spawnPoint = [80, 320]
        
        self.centerX = x + (self.width/2)
        self.centerY = y + (self.height/2)

        self.boundaries = [80, 160,  ##Top left XY
                           480, 720] ##bottom right YX
        
        ##Movement and Jump Variables
        self.velocity = 10
        self.negative = 1
        
        self.facing = True
        self.run = False 
    
        self.jump = False
        self.jumpCounter = 10
        self.jumpHeight = 0
        self.maxJumpHeight = 40

        self.punch = False
        self.kick = False
        
        
        ##Hit boxes
        
        self.attackHitboxR = pygame.rect.Rect((self.x + self.width), (self.y + self.height / 4),
                                              (self.width / 2), (self.height / 2))
        
        self.attackHitboxL = pygame.rect.Rect((self.x - self.width / 2),(self.y2 / 4),
                                              (self.width / 2),(self.height /2))
        
        ##Attribute Variables
        self.HP = 100
        self.ATK = 20
        
        self.death = False
        
        self.score = 0
        

        ##Sprite Variables
        self.scrollCount = 0
        
    
        ##Sprite List
        self.spriteList = [pygame.image.load('sprites/ninja_stand.png'),
                           pygame.image.load('sprites/ninja_stand_reverse.png'),
                           
                           pygame.image.load('sprites/ninja_stand_punch.png'),
                           pygame.image.load('sprites/ninja_stand_punch_reverse.png'),
                           
                           pygame.image.load('sprites/punch_right.png'),
                           pygame.image.load('sprites/punch_left.png'),
                           
                           pygame.image.load('sprites/ninja_run_right.png'),
                           pygame.image.load('sprites/ninja_run_right_2.png'),
                           
                           pygame.image.load('sprites/ninja_run_left.png'),
                           pygame.image.load('sprites/ninja_run_left_2.png'),
                           
                           pygame.image.load('sprites/ninja_run_punch.png'),
                           pygame.image.load('sprites/ninja_run_punch_reverse.png')]
    

        
        

## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ##

##    Set and Get Functions

## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ##

    ##Coordinates Get/Set

    def setX(self, xVal):
        self.x = xVal
        self.setX2(xVal + self.getWidth())
        self.setCenterX(xVal + (self.getWidth() / 2))
        self.setXY()
        
    def setY(self, yVal):
        self.y = yVal
        self.setY2(yVal + self.getHeight())
        self.setCenterY(yVal + (self.getHeight() / 2))
        self.setXY()
        
    def setX2(self, xVal):
        self.x2 = xVal
        
    def setY2(self, yVal):
        self.y2 = yVal
        
    def setXY(self):
        self.x = self.getX()
        self.y = self.getY()

    def setOriginalX(self, oxVal):
        self.originalX = oxVal

    def setOriginalY(self, oyVal):
        self.originalY = oyVal
        
    def setCenterX(self, center):
        self.centerX = center
        
    def setCenterY(self, center):
        self.centerY = center
        
    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def getX2(self):
        return self.x2
    
    def getY2(self):
        return self.y2
    
    def getXY(self):
        return (self.getX(), self.getY())
    
    def getRect(self):
        return pygame.rect.Rect(self.getXY() + (self.getWidth(), self.getHeight()))
    
    def getOriginalX(self):
        return self.originalX

    def getOriginalY(self):
        return self.originalY
    
    def getCenterX(self):
        return self.centerX
    
    def getCenterY(self):
        return self.centerY

    def getBoundaries(self, cornerNo):
        return self.boundaries[cornerNo]
    
    
    
    ##Hit box Get/Set

    def setWidth(self, newWidth):
        self.width = newWidth
        
    def setHeight(self, newHeight):
        self.height = newHeight

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height
    
    def getAttackHitboxR(self):
        return pygame.rect.Rect(self.attackHitboxR)
    
    def getAttackHitboxL(self):
        return pygame.rect.Rect(self.attackHitboxL)

    def setAttackHitboxR(self):
        self.attackHitboxR = pygame.rect.Rect((self.x + self.width),(self.y + self.height / 4),
                                              (self.width / 2), (self.height / 2))
            
    def setAttackHitboxL(self):
        self.attackHitboxL = pygame.rect.Rect((self.x - self.width / 2),(self.y + self.height / 4),
                                              (self.width / 2), (self.height / 2))
    
    def resetAttackHitboxes(self):
        self.attackHitboxR = pygame.rect.Rect(0,0,0,0)
        
        self.attackHitboxL = pygame.rect.Rect(0,0,0,0)
    
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
    
    def getRun(self):
        return self.run

    def setRun(self, r):
        self.run = r
            
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
    
    
    ##HUD
    
    def getHP(self):
        return self.HP
    
    def setHP(self, hp):
        self.HP = hp
        
    def getScore(self):
        return self.score
    
    def setScore(self, s):
        self.score = s
        
    def getDeath(self):
        return self.death
    
    def setDeath(self, d):
        self.death = d
    
    
    ##Scrolls
    
    def getScrollCount(self):
        return self.scrollCount
    
    def setScrollCount(self):
        self.scrollCount = self.scrollCount + 1
    
    def resetScrollCount(self):
        self.scrollCount = 0


## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ##
##
## KEY PRESS FUNCTIONS
##
## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ##
##
## - - playerMotion
##
## - - playerAction
##
## - - player


    def playerMotion(self):

        
        ##KeyPress Variable
        eventKey = pygame.key.get_pressed()
        
        
        ##Movement (WASD/Arrow) Keys In Action

        if ((eventKey[pygame.K_LEFT] or eventKey[pygame.K_a]) and 
            (self.getX() > self.getBoundaries(0))):
        
            self.setRun(True)
            self.setX(self.getX() - self.velocity)
            self.setOriginalX(self.getX())
            self.setFacing(False)
            
            
      
            
            
        if ((eventKey[pygame.K_RIGHT] or eventKey[pygame.K_d])):
            
            self.setRun(True)
             
            if(self.getX() < self.getBoundaries(3) - self.getWidth()):
        
                self.setX(self.getX() + self.velocity)
                self.setOriginalX(self.getX())
                self.setFacing(True)
                
        
        

        if not(self.getJump()):
            

            if ((eventKey[pygame.K_UP] or eventKey[pygame.K_w]) and 
                self.getOriginalY() > self.getBoundaries(1) - (self.getHeight() / 2)):
            
                self.setY(self.getY() - (self.velocity / 2))
                self.setOriginalY(self.getY())
                self.setRun(True)
            

            if ((eventKey[pygame.K_DOWN] or eventKey[pygame.K_s]) and 
                self.getOriginalY() < self.getBoundaries(2) - self.getHeight()):
            
                self.setY(self.getY() + (self.velocity / 2))
                self.setOriginalY(self.getY())
                self.setRun(True)
            
            self.setJumpHeight(0)
            

        else: ##Moving up and down WHILE jumping
            
            
            ##IF UP or W is pressed AND origin Y is greater than top boundary AND less than bottom boundary
            if ((eventKey[pygame.K_UP] or eventKey[pygame.K_w]) and 
                self.getOriginalY() > self.getBoundaries(1) - (self.getHeight() / 2)):
                
                self.setY(self.getY() - (self.velocity / 2))
                self.setOriginalY(self.getOriginalY() - (self.velocity / 2))
                self.setJumpHeight(self.getY() - self.getOriginalY())
                self.setRun(True)
            
            
            ##IF DOWN or S is pressed AND origin Y is less than bottom boundary  
            if (eventKey[pygame.K_DOWN] or eventKey[pygame.K_s] and 
                self.getOriginalY() < self.getBoundaries(2) - self.getHeight()):
                
                self.setY(self.getY() + (self.velocity / 2))
                self.setOriginalY(self.getOriginalY() + (self.velocity / 2))
                self.setJumpHeight(self.getY() - self.getOriginalY())
                self.setRun(True)
                           
            
            
            ## ## ## ## ## ## 
            ## Jump equation 
            ## ## ## ## ## ##
            
            
            if self.getJumpCounter() >= -10:
               
                self.setNegative(False)
                
                if self.getJumpCounter() <= 0:
                    self.setNegative(True)
                
                self.setY(self.getY() - 0.1 * (self.getJumpCounter() ** 2) * self.getNegative())
                
                self.setJumpCounter(self.getJumpCounter() - 1)

            else:
               
                self.setJump(False)
                self.setJumpCounter(10)

        

    def playerAction(self):

        ##KeyPress Variables
        eventKey = pygame.key.get_pressed()

        ##Kick

        #if ((eventKey[pygame.K_z]) or (eventKey[pygame.K_y])):
        #   self.setKick(True)
        #  self.setPunch(False)
            
        
        ##Punch
        
        if ((eventKey[pygame.K_LSHIFT]) or (eventKey[pygame.K_t])):
            self.setKick(False)
            self.setPunch(True)
            
        
        ##If SPACE is pressed
        if eventKey[pygame.K_SPACE]:
            self.setJump(True)
            
        
        
## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ##
##
## Draw Functions (Sprite & Hit boxes)
##
## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ## -- ##
##       
## - - drawPlayer
##
## - - drawShadow
##
## - - drawAction


    def drawPlayer(self, windowFrame):

        
        ##Draw Direction of Player
    
        if(self.facing):
        
            ##Facing Right (True) (Default)
            
            ##Hit box
            ##pygame.draw.rect(windowFrame, (0,255,255), (self.getXY(), self.getWidth(), self.getHeight()))
            ##pygame.draw.rect(windowFrame,(0,0,255), (self.getX() + (self.getWidth() / 2), self.getY(), self.getWidth() / 2, self.getHeight()))
            
            
            ##SPRITE BLITS 0 Stand right, 2 Attack right, 6/7 Run right
            
            if(self.getPunch()):
                windowFrame.blit(self.spriteList[2], (self.getXY()))
                
            else: windowFrame.blit(self.spriteList[0], (self.getXY()))
            
            if(self.getRun()):
                if(self.getPunch()):
                        windowFrame.blit(self.spriteList[10], (self.getXY()))
                elif(pygame.time.get_ticks() % 10 == 0):
                    
                    windowFrame.blit(self.spriteList[6], (self.getXY()))
                
                else: windowFrame.blit(self.spriteList[7], (self.getXY()))
                 
                 
        else:

            ##Facing Left (False)
            
            ##Hit box
            #pygame.draw.rect(windowFrame, (0,0,255), (self.getXY(), self.getWidth(), self.getHeight()))
            #pygame.draw.rect(windowFrame, (0,255,255), (self.getX() + (self.getWidth() / 2), self.getY(), self.getWidth() / 2, self.getHeight()))
            
            
            ##SPRITE BLITS 1 Stand left, 3 Attack left, 8/9 Run left
            
            if(self.getPunch()):
                windowFrame.blit(self.spriteList[3], (self.getXY()))
            
            else: windowFrame.blit(self.spriteList[1], (self.getXY()))
            
            if(self.getRun()):
                if(self.getPunch()):
                        windowFrame.blit(self.spriteList[11], (self.getXY()))
                elif(pygame.time.get_ticks() % 10 == 0):
                    
                    windowFrame.blit(self.spriteList[8], (self.getXY()))
                
                else: windowFrame.blit(self.spriteList[9], (self.getXY()))
                 
            
            
        self.drawShadow(windowFrame)
        self.drawAction(windowFrame)
        self.playerMotion()



    def drawShadow(self, windowFrame):


        ##Draw Shadow of Player
        if(self.getJump()):
            
          
            ##Shadow Circle w/in ellipse, must follow Player and shrink/grow as Player JUMPS
            shadowX = self.getCenterX() - (self.getJumpHeight() / 2)
            shadowY = (self.getOriginalY() + (self.getHeight()))
            shadowWidth = self.getJumpHeight()
            shadowHeight = self.getJumpHeight() / 2
            

            pygame.draw.ellipse(windowFrame, (0,0,0),(shadowX, shadowY, shadowWidth, shadowHeight))



    def drawAction(self, windowFrame):

        ##Draw Punch/Kick Hit boxes

        if(self.getPunch()): ##If Punch button pressed
            
            if(self.facing): ##Facing Right by default
                
                windowFrame.blit(self.spriteList[4], 
                                 (self.getX() + self.getWidth(),
                                  self.getY() + self.getHeight() / 4))
                
                self.setAttackHitboxR()
                
                ##Hit box
                #pygame.draw.rect(windowFrame,(255,0,0),
                #       ((self.getX2()),(self.getY2() / 4),
                #              (self.getWidth() / 2),(self.getHeight() /2)))
            
            else: ##Faces left
                
                windowFrame.blit(self.spriteList[5], 
                                 (self.getX() - self.getWidth() / 2,
                                  self.getY() + self.getHeight() / 4))
                
                self.setAttackHitboxL()
                
                ##Hit box
                #pygame.draw.rect(windowFrame,
                #       (255,0,0),((self.getX() - self.getWidth() / 2),(self.getY2() / 4),
                #       (self.getWidth() / 2),(self.getHeight() /2)))
        
        
        self.setPunch(False)


        ##Kick Action  **********(unused)
        ##if(self.kick):
        
        ##Hit box    
        #if(self.facing): ##Facing Right by default
        #   pygame.draw.rect(windowFrame, (255,0,0), ((self.getX() + (self.getWidth() * 0.75)), (self.getY2() / 2),
        #                     (self.getWidth() / 2), (self.getHeight() /2)))
        #else: ##Faces left
        #   pygame.draw.rect(windowFrame,(255,0,0), ((self.getX() - (self.getWidth() * 0.25)), (self.getY2() / 2),
        #                    (self.getWidth() / 2),(self.getHeight() /2)))
        #self.setKick(False)
        
        
            
        
        
        
    
            


