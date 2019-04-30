##Ty Dawson - Python Project 2018-2019
##
##menu.py - Menu Screen/Navigation/Pause

##Imports

import pygame, sys

##Menu Class
    
class menu(object):


    def __init__(self):
        
        self.pause = False 
        self.select = False
        self.menuValue = 0
        self.levelNo = 0
        
        self.showDifficulties = False
        
        self.sound = True
        self.music = True
        self.debug = False
        
        ##Menu word variables
        self.menuNames = ["START",          ##menuValue == 0: Start Menu
                          "HIGH SCORE",     ##menuValue == 1: High Scores Menu
                          "OPTIONS",        ##menuValue == 2: Options Menu
                          "EXIT",           
                          "PAUSE",          ##menuValue == 4: Game play
                          "HUD",            ##menuValue == 5: Pause
                          "RESUME",         #6
                          "RESTART",        #7
                          "SOUND",          #8
                          "MUSIC",          #9
                          "DEBUG",          #10
                          "ON",             #11
                          "OFF",            #12
                          "RESET",          #13
                          "EASY",           #14
                          "MEDIUM",         #15
                          "HARD"]           #16
        
        
        self.hsValues = []
        self.showPressY = False
        
        self.menuTitles = [pygame.image.load('sprites/title.png'),
                           pygame.image.load('sprites/hs.png'),
                           pygame.image.load('sprites/options.png'),
                           pygame.image.load('sprites/pause.png')]
        
                        ##Start level sprites
        self.levelBG = [pygame.image.load('sprites/clouds.png'), ##(0,0)
                        pygame.image.load('sprites/grass_top.png'), ##(0,80)
                        pygame.image.load('sprites/grass.png'), ##(80,200)
                        pygame.image.load('sprites/grass_fade.png'), ##(0,200)
                        pygame.image.load('sprites/grass_fade_2.png'),
                        
                        ##Player HP, level, score
                        pygame.image.load('sprites/hud.png'),
                        
                        ##2nd level type sprites 
                        pygame.image.load('sprites/clouds2.png'), ##(0,0)
                        pygame.image.load('sprites/grass_top2.png'), ##(0,80)
                        pygame.image.load('sprites/grass2.png'), ##(80,200)
                        pygame.image.load('sprites/grass_fade2.png'), ##(0,200)
                        pygame.image.load('sprites/grass_fade_2_2.png')]##(720,200)
        
        
        ##Menu Selector Choice counter
        self.menuCounter = 0
        
        ##Menu Background
        self.menuBG = [(255,255,255), 
                       (70,70,70), 
                       (140,140,140), 
                       (210,210,0),
                       (0,0,0)]
    
    ##GET/SET Functions
    
    def getSelect(self):
        return self.select
    
    def setSelect(self, i):
        self.select = i
        if(pygame.time.get_ticks() % 2 == 0):
            self.select = False
    
    def getMenuValue(self):
        return self.menuValue
    
    def setMenuValue(self, n):
        self.menuValue = n
        
    def getMenuCounter(self):
        return self.menuCounter
    
    def setMenuCounter(self, n):
        self.menuCounter = n
    
    def getLevelNo(self):
        return self.levelNo
    
    def setLevelNo(self, n):
        self.levelNo = n
    
    def getShowDifficulties(self):
        return self.showDifficulties
    
    def setShowDifficulties(self, t):
        self.showDifficulties = t
        

    
    
    ##Debug Options/Pause
    
    def getSound(self):
        return self.sound 
    
    def setSound(self, t):
        self.sound = t

    def getMusic(self):
        return self.music

    def setMusic(self, m):
        self.music = m
    
    def getDebug(self):
        return self.debug
    
    def setDebug(self, b):
        self.debug = b
        
    def getPause(self):
        return self.pause
    
    def setPause(self, p):
        self.pause = p
    
    def getHSValue(self, n):
        return self.hsValues[n]
    
    def getHSValues(self):
        return self.hsValues
    
    ##Cycle high score list
    def setHSValue(self, n):
        
        self.hsValues.insert(0, str(n))
        
        self.hsValues.sort(key=float, reverse = True)
        
        del self.hsValues[5]
            
            
    def saveHighScore(self):
        
        with open("highscores.txt", "w") as hsFile:
        
            for i in self.getHSValues():
                
                hsFile.write(str(i))
                hsFile.write("\n")
        
        
    def pullHighScore(self):
        
        with open("highscores.txt", "r") as hsFile:
        
            self.hsValues = hsFile.read().splitlines()
        
    
    def showPressY(self, t):
        self.showPressY = t
    
    
    
    ## -- -- -- -- -- ##
    ##   menuAction   ## Key presses
    ## -- -- -- -- -- ##
    

    def menuAction(self, level):
        
        
        eventKey = pygame.key.get_pressed()
        
        ##MenuVals; 0-Start Screen, 1-High Scores, 2-Options 3-Game/HUD 4-Pause
        
        ##Menu Actions for START
        if(self.getMenuValue() == 0):
            
            if(self.getShowDifficulties() == False):
                
                if(eventKey[pygame.K_w]):
                    
                    self.setMenuCounter(self.getMenuCounter() - 1)
                    if(self.getMenuCounter() < 0): self.setMenuCounter(0)
                    
                if(eventKey[pygame.K_s]):
                    
                    self.setMenuCounter(self.getMenuCounter() + 1)
                    if(self.getMenuCounter() > 3): self.setMenuCounter(3)
            
                if((eventKey[pygame.K_e])):
                    
                    if(self.getMenuCounter() == 0):
                        
                        self.setShowDifficulties(True)
                    
                        
                    if(self.getShowDifficulties() == False):
                                
                        if(self.getMenuCounter() == 1):
                            self.setMenuValue(1)
                        elif(self.getMenuCounter() == 2):
                            self.setMenuValue(2)
                        else: sys.exit()
            
            else:
                
                if(eventKey[pygame.K_w]):
                    
                    self.setMenuCounter(self.getMenuCounter() - 1)
                    if(self.getMenuCounter() < 0): self.setMenuCounter(0)
                    
                if(eventKey[pygame.K_s]):
                    
                    self.setMenuCounter(self.getMenuCounter() + 1)
                    if(self.getMenuCounter() > 3): self.setMenuCounter(3)
            
                if(eventKey[pygame.K_e]):
                    
                    if(self.getMenuCounter() == 0):
                        level.setDifficulty(0)
                        self.setMenuValue(3)
                        self.setShowDifficulties(False)
                        
                    if(self.getMenuCounter() == 1):
                        level.setDifficulty(1)
                        self.setMenuValue(3)
                        self.setShowDifficulties(False)
                        
                    if(self.getMenuCounter() == 2):
                        level.setDifficulty(2)
                        self.setMenuValue(3)
                        self.setShowDifficulties(False)
                        
                    if(self.getMenuCounter() == 3):
                        
                        self.setShowDifficulties(False)
                        
                        
    
        ##Menu Actions for HIGH SCORE
        elif(self.getMenuValue() == 1):
            
            ##Keystrokes
            if(eventKey[pygame.K_w]):
                
                self.setMenuCounter(self.getMenuCounter() - 1)
                if(self.getMenuCounter() < 0): self.setMenuCounter(0)    
            
            if(eventKey[pygame.K_s]):
                
                self.setMenuCounter(self.getMenuCounter() + 1)
                if(self.getMenuCounter() > 1): self.setMenuCounter(1)
        
            
            
            if(eventKey[pygame.K_e]):
                
                if(self.getMenuCounter() == 0):
                    self.showPressY = True
                
                elif(self.getMenuCounter() == 1):
                    self.setMenuValue(0)
            
            
            if(eventKey[pygame.K_y]):
            
                hsFile = open("highscores.txt", "w")
                reset = [0,0,0,0,0]
                
                for i in reset:
                    
                    hsFile.write(str(i))
                    hsFile.write("\n")
                
                hsFile.close()
                
                self.showPressY = False
            
                
        ##Menu Actions for OPTIONS
        elif(self.getMenuValue() == 2):
            
            ##Keystrokes
            if(eventKey[pygame.K_w]):
                
                self.setMenuCounter(self.getMenuCounter() - 1)
                if(self.getMenuCounter() < 0): self.setMenuCounter(0)    
            
            if(eventKey[pygame.K_s]):
                
                self.setMenuCounter(self.getMenuCounter() + 1)
                if(self.getMenuCounter() > 3): self.setMenuCounter(3)
        
        
        
            if((eventKey[pygame.K_e])):
                
    
                ##Logic
                if(self.getMenuCounter() == 0):
                    
                    if(self.getSound() == True):
                        self.setSound(False)
                    elif(self.getSound() == False):
                        self.setSound(True)
                    self.setSelect(False)
                    
                if(self.getMenuCounter() == 1):
                    
                    if(self.getMusic() == True):
                        self.setMusic(False)
                    elif(self.getMusic() == False):
                        self.setMusic(True)
                    self.setSelect(False)
                
                if(self.getMenuCounter() == 2):
                    
                    if(self.getDebug() == True):
                        self.setDebug(False)
                    elif(self.getDebug() == False):
                        self.setDebug(True)
                    self.setSelect(False)
                
                if(self.getMenuCounter() == 3):
                
                    if(self.getPause()):
                        self.setMenuValue(3)
            
                    else: self.setMenuValue(0)
        
        
        ##Menu Actions for GAMEPLAY
        
        if(self.getMenuValue() == 3):
            
            if(eventKey[pygame.K_p]):
                self.setPause(True)
            elif(self.getPause() and eventKey[pygame.K_p]):
                self.setPause(False)
                
            ##Level debug key
            
            if(eventKey[pygame.K_x]):
                self.setLevelNo(self.getLevelNo() + 1)
                
            
                

        ##Menu Actions for PAUSE
        if(self.getMenuValue() == 4):
            
               
            ##Keystrokes
            if(eventKey[pygame.K_w]):
                
                self.setMenuCounter(self.getMenuCounter() - 1)
                if(self.getMenuCounter() < 0): self.setMenuCounter(0)
                
            if(eventKey[pygame.K_s]):
                
                self.setMenuCounter(self.getMenuCounter() + 1)
                if(self.getMenuCounter() > 3): self.setMenuCounter(3)
        
            if((eventKey[pygame.K_e])):
                
                if(self.getMenuCounter() == 0):
                    self.setPause(False)
                elif(self.getMenuCounter() == 1):
                    self.setMenuValue(0)
                elif(self.getMenuCounter() == 2):
                    self.setMenuValue(2)
                elif(self.getMenuCounter() == 3):    
                    sys.exit()
                    
            if(eventKey[pygame.K_p]):
                self.setPause(False)
                
        
        if(self.getMenuValue() == 5):
            
            if((eventKey[pygame.K_e])):
                
                self.setMenuValue(0) 
            
        
            
    ## -- -- -- -- -- ##
    ##   Draw Menu    ## Draws entire Menu for each screen
    ## -- -- -- -- -- ##
    
    
    def drawMenu(self, window, level, player):
        
        
        ## ## ## ## ## ## ## ## ## ##
        ##LOCATION OF OPTION LIST
        menuXY = [100,(window.getHeight() / 2),
                  ((window.getHeight() / 2) + ((self.getMenuCounter() + 1 ) * 20))]
        
        ##TITLE TEXT
        pygame.font.init()
        font  = pygame.font.SysFont("Retroville NC", 80, False, False)
        font2 = pygame.font.SysFont("Retroville NC", 20, False, False)
        font3 = pygame.font.SysFont("Retroville NC", 28, False, False)
       
        ##Cosmetics
        fader = 1
        rate = 254
        if(pygame.time.get_ticks() % rate == 0):
            fader = fader * -1
        
        fade = font2.render("P R E S S  _E_  T O  S E L E C T", 
                            True, ((pygame.time.get_ticks() % rate * fader), 
                                   (pygame.time.get_ticks() % rate * fader), 
                                   (pygame.time.get_ticks() % rate * fader)))
        
        
        ## ## ## ## ## ## ## ## ## ##
        if(self.getMenuValue() == 0): ##START MENU
            
            
            ##Reset Game Variables
            level.setLevelNo(1)
            level.enemyList.clear()
            level.setECount(1)
                
            player.setScore(0)
            player.setHP(100)
            player.setX(player.boundaries[0])
            player.setY(player.boundaries[1])
            player.setDeath(False)
            
            ##Background
            pygame.draw.rect(window.frame, self.menuBG[4], (0,0, window.getWidth(), window.getHeight()))
            
            credit = font2.render('- V.0.1 - C A P S T O N E    P R O J E C T - M M X I I X - M M X I X', False, (255,255,255))
            

            directions = font2.render('W-A-S-D TO MOVE, T TO USE KATANA', False, (255,0,0))
            
            window.frame.blit(self.menuTitles[0], (0,240))
            
            window.frame.blit(credit, (0 - (pygame.time.get_ticks() / 40) % 800,0))
            window.frame.blit(credit, (800 - (pygame.time.get_ticks() / 40) % 800,0))
            window.frame.blit(directions, (0 - (pygame.time.get_ticks() / 20) % 800, window.getHeight() - 40))
            window.frame.blit(directions, (800 - (pygame.time.get_ticks() / 20) % 800, window.getHeight() - 40))
            window.frame.blit(fade, (menuXY[0] + 120, menuXY[1] + 120))
        
            
            snek= pygame.image.load('sprites/big_snake1.png')
            snek2=pygame.image.load('sprites/big_snake2.png')
            
            ##Scroll: 800 - (pygame.time.get_ticks() / 2) % 840
            if(pygame.time.get_ticks() % 400 > 200): 
                window.frame.blit(snek,  (window.getWidth() / 2 - 20,160))
            elif(pygame.time.get_ticks() % 400 <= 200):
                window.frame.blit(snek2, (window.getWidth() / 2 - 20,160))
            
            
            self.drawMenuOptions(window)
            
            self.setPause(False)
            
            
        ## ## ## ## ## ## ## ## ## ##
        if(self.getMenuValue() == 1): ##HIGH SCORE MENU
            
            pygame.draw.rect(window.frame, self.menuBG[4], (0,0, window.getWidth(), window.getHeight()))
            
            window.frame.blit(self.menuTitles[1], (0,200))
            
            self.drawMenuOptions(window)


        ## ## ## ## ## ## ## ## ## ##
        if(self.getMenuValue() == 2): ##OPTIONS MENU
            
            pygame.draw.rect(window.frame, self.menuBG[4], (0,0, window.getWidth(), window.getHeight()))
            
            window.frame.blit(self.menuTitles[2], (0,200))
            
            self.drawMenuOptions(window)
            
             
        ## ## ## ## ## ## ## ## ## ##
        if(self.getMenuValue() == 3): ##GAMEPLAY
            
            self.setMenuCounter(0)
            
            ##DRAW BACKGROUND/LEVEL DETAILS
            
            if (level.getLevelNo() < 11):
                
                ##Regular backgrounds
                window.frame.blit(self.levelBG[0], (0 - player.getScrollCount() * 4,0)) ##Clouds (scroll)
                window.frame.blit(self.levelBG[0], (800 - player.getScrollCount() * 4,0)) ##Second cloud bg
                
                window.frame.blit(self.levelBG[1], (0,80)) ##Grass top
                
                window.frame.blit(self.levelBG[2], (80 - player.getScrollCount() * 4,160)) ##Grass center (scroll)
                window.frame.blit(self.levelBG[2], (720 - player.getScrollCount() * 4,160)) ##Grass 2nd image
                
                
                window.frame.blit(self.levelBG[3], (0,160)) ##Grass fade left
                window.frame.blit(self.levelBG[4], (720,160)) ##Grass fade right
            
            elif(level.getLevelNo() >= 11):
                
                ##Boss Level backgrounds
                window.frame.blit(self.levelBG[6], (0 - player.getScrollCount() * 4,0)) ##Clouds (scroll)
                window.frame.blit(self.levelBG[6], (800 - player.getScrollCount() * 4,0)) ##Second cloud bg
                
                window.frame.blit(self.levelBG[7], (0,80)) ##Grass top
                
                window.frame.blit(self.levelBG[8], (80 - player.getScrollCount() * 4,160)) ##Grass center (scroll)
                window.frame.blit(self.levelBG[8], (720 - player.getScrollCount() * 4,160)) ##Grass 2nd image
                
                
                window.frame.blit(self.levelBG[9], (0,160)) ##Grass fade left
                window.frame.blit(self.levelBG[10], (720,160)) ##Grass fade right
                
            
            ## ## ##
            ##HUD
            
            ##Background
            window.frame.blit(self.levelBG[5], (0, 480)) ##HUD (HP, HIGH SCORE)
            
            ##HP Bar
            pygame.draw.rect(window.frame, (250,0,0), (110,520, player.getHP() * 2, 40)) 
            HPblit = font3.render("HP: " + str(player.getHP()), True, (0,0,0))
            
            ##HIGH SCORE 
            scoreBlit = font3.render("HIGH SCORE: " + str(player.getScore()), True, (0,0,0))
            
            ##LEVEL
            levelBlit = font3.render("LVL:" + str(level.getLevelNo()), True, (255,255,255))
            
            ##BLITS
            window.frame.blit(HPblit, (50, 520))
            window.frame.blit(scoreBlit, (320,520))
            window.frame.blit(levelBlit, (window.getWidth() / 2, 480))
            
            
            ## ## ## ##
            ##PAUSE ACTION
            if(self.getPause()):
                self.setMenuValue(4)
            
            
            ## ## ## ##
            ##END AT PLAYER DEATH, SET AND SAVE HIGH SCORE
            if(player.getHP() <= 0):
                
                self.setHSValue(player.getScore())
                self.saveHighScore()
                self.setMenuValue(5)
                
                
        ## ## ## ## ## ## ## ## ## ##
        if(self.getMenuValue() == 4): ##PAUSE SCREEN
            
            
            pygame.draw.rect(window.frame, self.menuBG[4], (0,0, window.getWidth(), window.getHeight()))
            
            window.frame.blit(self.menuTitles[3], (0,200))
            
            self.drawMenuOptions(window)
            
            if(self.getPause() == False):
                self.setMenuValue(3)
            
            
        ## ## ## ## ## ## ## ## ## ##
        if(self.getMenuValue() == 5): ##GAME OVER SCREEN
            
            
            pygame.draw.rect(window.frame, self.menuBG[4], 
                                 (0,0, window.getWidth(), window.getHeight()))
            
            gameOver = font.render("GAME OVER", 
                                   False, (255,255,255))
            redo = font2.render("P R E S S  _E_  T O  R E T U R N",
                            False, (255,255,255))
        
            window.frame.blit(gameOver, (110, (-160 + pygame.time.get_ticks() % 1200)))
            window.frame.blit(redo, (window.getWidth() / 2 - 200, window.getHeight() - 100))
        
            
            self.drawMenuOptions(window)
            
        
            
            
    ## -- -- -- -- -- ##
    ##drawMenuOptions ## Draws List of Menu Options to choose from 
    ## -- -- -- -- -- ##
    
    
    def drawMenuOptions(self, window):
        
        
        font2 = pygame.font.SysFont("Retroville NC", 20, False, False)
        
        ##
        selector = font2.render(">", True, (255,0,0))
                
        
        ##MENU OPTION LIST 
            
        start = font2.render(self.menuNames[0], False, (255,255,255))
        resume = font2.render(self.menuNames[6], False, (255,255,255))
        restart = font2.render(self.menuNames[7], False, (255,255,255))
        hs = font2.render(self.menuNames[1], False, (255,255,255))
        options = font2.render(self.menuNames[2], False, (255,255,255))
        back = font2.render(self.menuNames[3], False, (255,255,255)) 
        sound = font2.render(self.menuNames[8] + ": " + str(self.getSound()), False, (255,255,255))
        music = font2.render(self.menuNames[9] + ": " + str(self.getMusic()), False, (255,255,255))
        debug = font2.render(self.menuNames[10] + ": " + str(self.getDebug()), False, (255,255,255))
        reset = font2.render(self.menuNames[13], False, (255,255,255))
        
        
         
        ##HIGH SCORE VALUES 
        hs0 = font2.render("1. " + str(self.getHSValue(0)), False,(255,255,255))
        hs1 = font2.render("2. " + str(self.getHSValue(1)), False,(255,255,255))
        hs2 = font2.render("3. " + str(self.getHSValue(2)), False,(255,255,255))
        hs3 = font2.render("4. " + str(self.getHSValue(3)), False,(255,255,255))
        hs4 = font2.render("5. " + str(self.getHSValue(4)), False,(255,255,255))
        
        
        ## ## ## ## ## ## ## ## ## ##
        ##LOCATION OF OPTION LIST
        menuXY = [100,(window.getHeight() / 2),
                  ((window.getHeight() / 2) + ((self.getMenuCounter() + 1 ) * 20))]
        
        
        
        ##START MENU
        if(self.getMenuValue() == 0):
            
            window.frame.blit(start, (menuXY[0] + 60, menuXY[1] + 20))
            window.frame.blit(hs, (menuXY[0] + 60, menuXY[1] + 40))
            window.frame.blit(options, (menuXY[0] + 60, menuXY[1] + 60))
            window.frame.blit(back, (menuXY[0] + 60, menuXY[1] + 80))
            
            if(self.getShowDifficulties() == False):
                
                ##SELECTOR
                window.frame.blit(selector, (menuXY[0] + 50, menuXY[2]))
                
            else: self.drawDifficulties(window)
            
        
        ##HIGH SCORE MENU
        elif(self.getMenuValue() == 1):
            
            window.frame.blit(reset, (menuXY[0] + 60, menuXY[1] + 20))
            window.frame.blit(back, (menuXY[0] + 60, menuXY[1] + 40))
            
            window.frame.blit(hs0, (menuXY[0] + 160, menuXY[1] + 20))
            window.frame.blit(hs1, (menuXY[0] + 160, menuXY[1] + 40))
            window.frame.blit(hs2, (menuXY[0] + 160, menuXY[1] + 60))
            window.frame.blit(hs3, (menuXY[0] + 160, menuXY[1] + 80))
            window.frame.blit(hs4, (menuXY[0] + 160, menuXY[1] + 100))
            
            ##SELECTOR
            window.frame.blit(selector, (menuXY[0] + 50, menuXY[1] + (self.getMenuCounter()+1) * 20))
        
            if(self.showPressY):
                show = font2.render("PRESS Y TO DELETE HIGH SCORES", False, (255,255,255))
                
                window.frame.blit(show, (menuXY[0] + 160, menuXY[1] + 120))
        
        ##OPTIONS MENU    
        elif(self.getMenuValue() == 2):
            
            window.frame.blit(sound, (menuXY[0] + 60, menuXY[1] + 20))
            window.frame.blit(music, (menuXY[0] + 60, menuXY[1] + 40))
            window.frame.blit(debug, (menuXY[0] + 60, menuXY[1] + 60))
            window.frame.blit(back,  (menuXY[0] + 60, menuXY[1] + 80))
            
            ##SELECTOR
            window.frame.blit(selector, (menuXY[0] + 50, menuXY[1] + ((self.getMenuCounter()+1) * 20)))
          
         
        ##PAUSE MENU 
        elif(self.getMenuValue() == 4):
                
            window.frame.blit(resume, (menuXY[0], menuXY[1]+ 20))
            window.frame.blit(restart, (menuXY[0], menuXY[1] + 40))
            window.frame.blit(options, (menuXY[0], menuXY[1] + 60))
            window.frame.blit(back, (menuXY[0], menuXY[1] + 80))
                
            ##SELECTOR
            window.frame.blit(selector, (menuXY[0] - 15, menuXY[1]+ ((self.getMenuCounter()+1) * 20)))
        
            
            
    
    
    ## -- -- -- -- -- ##
    ## drawDifficulty ## Draw difficulty options for Start in Menu 0 
    ## -- -- -- -- -- ##
    
    
    def drawDifficulties(self, window):
    
        
        font2 = pygame.font.SysFont("Retroville NC", 20, False, False)
        
        easy = font2.render(self.menuNames[14], False, (255,255,255))
        medium = font2.render(self.menuNames[15], False, (255,255,255))
        hard = font2.render(self.menuNames[16], False, (255,255,255))
        back = font2.render("BACK", False, (255,255,255)) 
        
        menuXY = [100,(window.getHeight() / 2),
                  ((window.getHeight() / 2) + ((self.getMenuCounter() + 1 ) * 20))]
        
        selector = font2.render(">", True, (255,0,0))

        
        window.frame.blit(easy,  (menuXY[0] + 300, menuXY[1] + 20))
        window.frame.blit(medium,(menuXY[0] + 300, menuXY[1] + 40))
        window.frame.blit(hard,  (menuXY[0] + 300, menuXY[1] + 60))
        window.frame.blit(back,  (menuXY[0] + 300, menuXY[1] + 80))
        
        window.frame.blit(selector, (menuXY[0] + 290, menuXY[1] + ((self.getMenuCounter()+1) * 20)))
            
   
    
       
        

            
                
            
            
       
       
       
       
            
            
        
    