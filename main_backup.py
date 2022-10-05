# first pip install pygame
import pygame
# variables
x = 30
y = 50
player = pygame.rect.Rect(x,y,100,100) # make rect
player_speed = 2

pygame.init()
window = pygame.display.set_mode((800, 600))

# we make inifnite loop to prevent autoclose our app
run = True
while run:
    # make a limit speed of the loop
    pygame.time.Clock().tick(60) #set game to 60 FPS
    #get events from player
    for event in pygame.event.get():
        # if player close the window
        if event.type == pygame.QUIT: 
            run = False
    
    keys = pygame.key.get_pressed()
    # moving ractangle when the button is pressed
    if keys[pygame.K_RIGHT]:
        x += player_speed
    if keys[pygame.K_LEFT]:
        x -= player_speed    
    if keys[pygame.K_UP]:
        y -= player_speed
    if keys[pygame.K_DOWN]:
        y += player_speed
    player = pygame.rect.Rect(x,y,100,100) # make rect

    # change background
    window.fill((38, 35, 53))
    #drow rect on screen
    pygame.draw.rect(window, (66, 165, 245), player)
    pygame.display.update()
