##Ty Dawson - Python Project 2018-2019
##
##Window.py - Object containing all game graphics


##Imports

import pygame, sys

##Window Class
    ##Arguments: Width, Height, Title, Menu, Scene


class window(object):

    
    
    def __init__(self, windowWidth, windowHeight):
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        
        self.boundaries = [80, 160,  ##Top left XY
                           480, 720] ##bottom right YX

        self.frameCount = pygame.time.get_ticks()
        

        ##Actual Window Frame **Refresh "frame"
        self.frame = pygame.display.set_mode((windowWidth, windowHeight))
        
        
    def getEvent(self):
        return pygame.event.get()

    ##GET/SET Functions for Vars

    def getWidth(self):
        return self.windowWidth

    def setWidth(self, newWidth):
        self.windowWidth = newWidth

    def getHeight(self):
        return self.windowHeight

    def setHeight(self, newHeight):
        self.windowHeight = newHeight

    
    ##Return Boundaries
    ##0 - TopX, 1 - TopY, 2 - BottomX, 3 - BottomY
    def getBoundaries(self, n):
        return self.boundaries[n]






    def scrollBackground(self, player):
        
        
        window8th = self.getWidth() / 8
        trianglePos = [self.getWidth(),
                       self.getWidth() - window8th,
                       self.getWidth() - window8th * 2,
                       self.getWidth() - window8th * 3,
                       self.getWidth() - window8th * 4,
                       self.getWidth() - window8th * 5,
                       self.getWidth() - window8th * 6,
                       self.getWidth() - window8th * 7]
        
        
        for i in trianglePos:
            
            ##Triangle polygons; simulate scrolling
            ##Resets at ScrollCount == 200 (4 * width of Window)
        
            pygame.draw.polygon(self.frame, (255,0,0),
                                ((i - player.getScrollCount() * 4, player.getBoundaries(2) - 60), 
                                (i - 20 - player.getScrollCount() * 4, player.getBoundaries(2) - 80), 
                                (i - 20 - player.getScrollCount() * 4, player.getBoundaries(2) - 40)))
            
            pygame.draw.polygon(self.frame, (255,0,0),
                                ((i - player.getScrollCount() * 4 + 800, player.getBoundaries(2) - 60), 
                                (i - 20 - player.getScrollCount() * 4 + 800, player.getBoundaries(2) - 80), 
                                (i - 20 - player.getScrollCount() * 4 + 800, player.getBoundaries(2) - 40)))



## -- -- -- -- -- ##
##Position Monitor## (X, Y) Coordinates, Direction, Jump Height
## -- -- -- -- -- ##


    def positionMonitor(self, player, level):

        font = pygame.font.SysFont("Courier New", 20)
        
        ##FRAMERATE
        framesMod = pygame.time.get_ticks() % 60
        framerate = font.render("Framerate % 60: " + str(framesMod),
                                True, (0,0,0))
        
        
        ##Character Hit box Coordinates
        
        
        topLXY = font.render("TopL (X,Y): " + str(player.getXY()),
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
        
        ##MOUSE XY COORDINATES
        
        mouseXY = pygame.mouse.get_pos()
        mouse = font.render("Mouse X/Y: " + str(mouseXY), 
                            True, (0,0,0))

        
        
        
        
    
        ##Booleans
        direction = font.render("Facing Right: " + str(player.getFacing()), 
                                True, (0,0,0))

        jumpCheck = font.render("Jump: " + str(player.getJump()), 
                                True, (0,0,0))

        running = font.render("Running: " + str(player.getRun()),
                              True, (0,0,0))

        
        
        ## ## ## ## ## ##
        ##Boundary tests
        
        boundaryW = player.getBoundaries(2) - player.getBoundaries(1)
        boundaryL = player.getBoundaries(3) - player.getBoundaries(0)
        
        boundaryText = font.render("BOUNDARY SPACE: " + str(boundaryL) + 
                                   "x" + str(boundaryW),
                                   True, (0,0,0))
        ##
        ##Boundary Outline
        pygame.draw.polygon(self.frame, (255,0,0),
                           ((player.getBoundaries(0), player.getBoundaries(1)), 
                            (player.getBoundaries(3), player.getBoundaries(1)), 
                            (player.getBoundaries(3), player.getBoundaries(2)),
                            (player.getBoundaries(0), player.getBoundaries(2))),
                            1)
        
        
        self.scrollBackground(player)
        
        
        ##Level tests
        ##Enemy Blits
        enemyCount = font.render("Enemy Count: " + str(level.getECount()),
                                 True, (255,255,255))
        
        
        ##Scroll test
        scrollText = font.render("Scroll Count: " + str(player.getScrollCount()), 
                                 True, (0,0,0))
        
        
        
        
        
        ## ## ## ## ## ## 
        ##Text Blits 
        
        ##Boundaries
        self.frame.blit(boundaryText, (player.getBoundaries(0), player.getBoundaries(1)))
        
        ##Top Left
        self.frame.blit(topLXY, (0,0))
        self.frame.blit(topRXY, (0,20))
        self.frame.blit(btmLXY, (0,40))
        self.frame.blit(btmRXY, (0,60))
        self.frame.blit(mouse, (0, 80))
        
        ##Top Right
        self.frame.blit(origin, (500, 0))
        self.frame.blit(jumpHeight, (500, 20))
        self.frame.blit(framerate, (500, 40))
        self.frame.blit(scrollText, (500, 60))
        self.frame.blit(direction, (500, 80))
        self.frame.blit(jumpCheck, (500, 100))
        self.frame.blit(running, (500, 120))
        
        ##Level Bar
        
        self.frame.blit(enemyCount, (self.getWidth() / 2 + 120, 500))
        
        

##!!##!!##!!##!!##!!##!!##!!##!!##
##Refresh Game Window Graphics!!##  Refreshes game window with objects
##!!##!!##!!##!!##!!##!!##!!##!!##



    def refreshWindow(self, menu, level, player):

        
        menu.pullHighScore()
        menu.drawMenu(self, level, player) 
               
        level.setLevelNo(level.getLevelNo())
        
        if(menu.getMenuValue() == 0):
           
            ##Reset Game Variables
            level.setLevelNo(0)
            level.setECount(0)
                
            player.setDeath(False)
            player.setScore(0)
            player.setHP(100)
            player.setX(player.boundaries[0])
            player.setY(player.boundaries[1])
        
        
        elif(menu.getMenuValue() == 3):
            
            ##DEBUG MENU
            if menu.getDebug():
                self.positionMonitor(player, level)    
            
            if(player.getPunch()):
                player.setAttackHitboxR()        
                player.setAttackHitboxL()
                
            else:
                player.resetAttackHitboxes()
            
            
            level.startLevel(player)
            
            
            ##Draw player last
            player.drawPlayer(self.frame)
            
        
        ## -- ## -- ## -- SCROLLING COUNT -- ## -- ## -- ##
        
        ##If Player pushes against right wall, up count by 1
        
        key = pygame.key.get_pressed()
        
        if(player.getX() == player.getBoundaries(3) - player.getWidth()
           and (key[pygame.K_RIGHT] or key[pygame.K_d])):
            
            player.setScrollCount()
            
            if(player.getScrollCount() == 200):
                
                player.resetScrollCount()

        
        ## -- ## -- ## -- EXIT KEY (ESC) -- ## -- ## -- ##
        
        if(key[pygame.K_ESCAPE]):
            pygame.quit()
            sys.exit()
        
        
        
        
        #Repaint background over old image, then player
        pygame.display.update()

    
