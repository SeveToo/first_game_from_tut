# first pip install pygame
import pygame

pygame.init()
window = pygame.display.set_mode((1280, 720))

# variables
speed = 2;

class Player:
    def __init__(self):
        self.x_cord = 0  
        self.y_cord = 0 
        self.width = 0 
        self.height = 0 
        self.image = pygame.image.load("manstand.png")
    
    def tick(self, keys): 
        if keys[pygame.K_w]:
            self.y_cord -= speed;
        if keys[pygame.K_s]:
            self.y_cord += speed;
        if keys[pygame.K_a]:
            self.x_cord -= speed;
        if keys[pygame.K_d]:
            self.x_cord += speed;


    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

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
        keys = pygame.key.get_pressed()
        player.tick(keys)

        # change background
        window.fill((247, 248, 249))

        # place the player on the screen
        player.draw()

        pygame.display.update()

        keys = pygame.key.get_pressed()
   

if __name__ == "__main__":
    main()