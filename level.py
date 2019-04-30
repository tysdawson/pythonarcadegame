##Ty Dawson - Python Project 2018-2019
##
##level.py - Level Instance

##Imports

import pygame, enemy, random

##Level Class

class level(object):
    

    def __init__(self, window, player):
        
        self.window = window
        
        self.levelNo = 1
        self.levelStart = True
        
        self.difficulties = [1, 2, 3]
        self.difficulty = 0
        
        self.enemyList = []
        self.enemyCount = 1
        
        self.playerWidth = 40
        self.playerHeight = 40
        
        self.player = player

    
    def getLevelNo(self):
        return self.levelNo
    
    def setLevelNo(self, n):
        self.levelNo = n
        
    def getLevelStart(self):
        return self.levelStart
    
    def setLevelStart(self, f):
        self.levelStart = f
        
    def getDifficulty(self):
        return self.difficulty
        
    def setDifficulty(self, n):
        self.difficulty = self.difficulties[n]
    
    def getECount(self):
        return self.enemyCount
    
    def setECount(self, e):
        self.enemyCount = e
        
    def getEnemyList(self):
        return self.enemyList
    
    def getEnemyListN(self, n):
        return self.enemyList[n]
        
    def setEnemyList(self):
        
        if(self.getLevelStart()):
            
            for i in range(0, self.getECount()):
                
                e = enemy.enemy()
                
                self.enemyList.append(e)
                
                if i == 100: break
            
            
            if(self.getLevelNo() % 5 == 0 and self.getLevelNo() > 0):
                
                if(self.getLevelNo() % 5 == 0):
                    for i in range(0, int(self.getLevelNo() / 5)):
                    
                        boss = enemy.enemy()
                        boss.setWidth(boss.enemySizes[1])
                        boss.setHeight(boss.enemySizes[1])
                        boss.setStyle(2)
                        boss.setHP(100)
                        self.enemyList.append(boss)
                        self.setECount(self.getECount() + 1)
                
                        if i == 30: break
                
            self.setLevelStart(False)
        
                
    
    ##Start Level by spawning enemies after scrolling to the right
    def startLevel(self, player):
        
    
        self.setEnemyList()
        
        for i in self.getEnemyList():
            
            i.drawEnemy(self.window)
            
        
        ##For each list entry check the collision for player/enemies
        for i in self.getEnemyList():
            
            self.checkCollision(player, i)  
        
        
        ##When all are dead
        if(self.getECount() == 0):
       
            if(player.getScrollCount() / 51 == 1 or 
               player.getScrollCount() / 101 == 1 or 
               player.getScrollCount() / 151 == 1) :
                
                self.setLevelNo(self.getLevelNo() + 1)
                
                self.enemyList.clear()
                
                self.setECount(self.getLevelNo() * 2)
                
                self.setLevelStart(True)
                
                if(player.getHP() <= 80):
                    player.setHP(player.getHP() + 5 * self.getDifficulty())
                
                if(player.getHP() > 80):
                    player.setHP(100)
                
                ##IF Player Dies First
                if(player.getHP() == 0):
                    
                    self.setECount(0)  
                    player.setDeath(True)       
    
       

    def checkCollision(self, player, enemy):
        
        if (enemy.colliderect(player) and player.getJump() == False):
            
            if(player.getFacing()):
                
                player.setHP(player.getHP() - 5 * self.getDifficulty())
                player.setX(player.getX() - 40)
            
            else:
                
                player.setHP(player.getHP() - 5 * self.getDifficulty())
                player.setX(player.getX() + 40)
            
            
        elif ((enemy.colliderect(player.getAttackHitboxR()) or 
               enemy.colliderect(player.getAttackHitboxL())) and 
               player.getJump() == False):
            
            enemy.setHP(enemy.getHP() - 50)
            
            if(enemy.getHP() == 0):
            
                enemy.setDeath(True)
                
                dead = pygame.mixer.Sound('sfx/hiss.wav')
                pygame.mixer.Sound.play(dead)
            
                self.setECount(self.getECount() - 1)
            
            player.setScore(player.getScore() + 50 * self.getDifficulty())
            
        if(enemy.getX() <= 0 - enemy.getWidth()):
            
            
            enemy.setDeath(True)
            
            self.setECount((self.getECount() - 1))
            
            
        




    

    
    
    
    
    
    