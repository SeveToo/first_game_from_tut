# first pip install pygame
import pygame

pygame.init()
window = pygame.display.set_mode((1280, 720))

# variables
image = pygame.image.load("bg.jpg") # load image to variable

class Player:
    def __init__(self):
        self.x_card = 0  
        self.y_card = 0 
        self.width = 0 
        self.height = 0 
        self.image = pygame.image.load("player.png")
    
    def tick(self): 
        pass

    def draw(self):
        window.blit(self.image, (self.x_card, self.y_card))

def main():
    # we make inifnite loop to prevent autoclose our app
    run = True
    player = Player()
    while run:
        # make a limit speed of the loop
        pygame.time.Clock().tick(60) #set game to 60 FPS
        #get events from player
        for event in pygame.event.get():
            # if player close the window
            if event.type == pygame.QUIT: 
                run = False
        
        player.tick()

        # change background
        window.fill((38, 35, 53))

        # place the image on screen 
        window.blit(image, (0,0))

        # place the player on the screen
        player.draw()

        pygame.display.update()

        keys = pygame.key.get_pressed()
   

if __name__ == "__main__":
    main()