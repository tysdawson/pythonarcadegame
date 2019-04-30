##Ty Dawson - Pygame Project 2018-2019 
##Platformer/Fighter
##Version 0.1

## -- -- ## -- -- ## -- -- ## -- -- Imports -- -- ## -- -- ## -- -- ## -- -- ##

import pygame, sys, window, player, menu, level
  
## -- -- ## -- -- ## -- -- ## -- -- Initializations -- -- ## -- -- ## -- -- ## -- -- ##
   

##Title of Window
title = "BATTLESNAKES"

dimensions = [800, 600]
        
##Player Attribute Dimensions
spawnPoint = [80, 320]
playerFrame = [60, 80, 100]

window = window.window(dimensions[0], dimensions[1])
menu = menu.menu()
level = level.level(window, player)
player = player.player(spawnPoint[0], spawnPoint[1],playerFrame[1], playerFrame[1])


## -- -- ## -- -- ## -- -- ## -- -- Main loop -- -- ## -- -- ## -- -- ## -- -- ##


##Initialization
pygame.init()
pygame.font.init()

##SFX Start
#Music 
pygame.mixer.music.load('sfx/Pulsar.wav')
pygame.mixer.music.play(-1)
#Sounds
attack = pygame.mixer.Sound('sfx/sword.wav')
jump = pygame.mixer.Sound('sfx/jump.wav')


##Run loop
run = True
while run:
    
    pygame.time.delay(0)
    pygame.display.set_caption(title)
    
    for event in pygame.event.get():
        
        if event.type == pygame.quit:
            
            pygame.quit()
            sys.exit()
        
        ##If keys are pressed by User
        if event.type == pygame.KEYDOWN:
            
            menu.menuAction(level)
            player.playerAction()
            
            if(player.getPunch() and menu.getSound() and menu.getMenuValue() == 3):
                pygame.mixer.Sound.play(attack)
            #if(player.getJump()): pygame.mixer.Sound.play(jump)
           
        else: player.setRun(False)
       
        ##SFX
        if(menu.getMusic() == False):
            pygame.mixer.music.stop()
            
    window.refreshWindow(menu, level, player)
        
pygame.quit()


