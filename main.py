# first pip install pygame
import pygame

# variables
x = 30
y = 50
player = pygame.rect.Rect(x,y,100,100) # make rect

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
    # change background
    window.fill((38, 35, 53))
    #drow rect on screen
    pygame.draw.rect(window, (66, 165, 245), player)
    pygame.display.update()
