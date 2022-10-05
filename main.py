# first pip install pygame
import pygame

pygame.init()
window = pygame.display.set_mode((1280, 720))

# variables

class Player:
    def __init__(self):
        self.x_cord = 0  
        self.y_cord = 0 
        self.image = pygame.image.load("manstand.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.speed = 2
    
    def tick(self, keys): 
        if keys[pygame.K_w]:
            self.y_cord -= self.speed;
        if keys[pygame.K_s]:
            self.y_cord += self.speed;
        if keys[pygame.K_a]:
            self.x_cord -= self.speed;
        if keys[pygame.K_d]:
            self.x_cord += self.speed;

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

class Cash:
    def __init__(self):
        self.x_cord = 0
        self.y_cord = 0
        self.image = pygame.image.load("coin.png")

    def tick(self):
        pass

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

def main():
    # we make inifnite loop to prevent autoclose our app
    run = True
    player = Player()
    clock = 0
    banknotes = []
    while run:
        clock += pygame.time.Clock().tick(60) / 1000
        #get events from player
        for event in pygame.event.get():
            # if player close the window
            if event.type == pygame.QUIT: 
                run = False
        keys = pygame.key.get_pressed()
        if(clock >= 3):
            clock = 0
            banknotes.append(Cash())

        player.tick(keys)
        for banknote in banknotes:
            banknote.tick()

        # change background
        window.fill((247, 248, 249))

        # place the player on the screen
        player.draw()
        for banknote in banknotes:
            banknote.draw()

        pygame.display.update()

        keys = pygame.key.get_pressed()
   

if __name__ == "__main__":
    main()