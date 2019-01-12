##Ty Dawson - Untitled Pygame Project 2018-2019 
##Platformer/Fighter
##Version 0.0.4

   
## -- -- ## -- -- ## -- -- ## -- -- Imports -- -- ## -- -- ## -- -- ## -- -- ##


import pygame, sys, random, window, player

from pygame.locals import *

  
## -- -- ## -- -- ## -- -- ## -- -- Initializations -- -- ## -- -- ## -- -- ## -- -- ##
   

pygame.init()
pygame.font.init()
window = window.window(800, 600)
player = player.player(80, 350, 80, 80) ##Prototype Player starts at 80 run 350 rise




## -- -- ## -- -- ## -- -- ## -- -- Main loop -- -- ## -- -- ## -- -- ## -- -- ##


##Run loop
run = True
while run:

    
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()




          
    window.refreshWindow(player)
        
    


pygame.quit()
