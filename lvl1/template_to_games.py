# first pip install pygame

import pygame

pygame.init()
window = pygame.display.set_mode((800, 600))

# we make inifnite loop to prevent autoclose our app
run = True
while run:
    #get events from player
    for event in pygame.event.get():
        # if player close the window
        if event.type == pygame.QUIT: 
            run = False
        