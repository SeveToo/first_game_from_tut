# in console write:
# pip install pygame 
# in folders lvl1 and lvl2
import pygame
from random import randint 

pygame.init()

# variables
window_width = 1280
window_height = 720
window = pygame.display.set_mode((window_width, window_height))

class Phiysic:
    def __init__(self, acceleration, max_velocity):
        self.hor_velocity = 0
        self.ver_velocity = 0
        self.acc = acceleration
        self.max_velocity = max_velocity
    
    def physic_tick(self):
        self.ver_velocity += 0.7

class Player(Phiysic):
    def __init__(self):
        super().__init__(0.5, 5)
        self.image = pygame.image.load("john.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x_cord = 10
        self.y_cord = 580 
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    
    def tick(self, keys):
        self.physic_tick()
        if keys[pygame.K_a] and self.hor_velocity >= -self.max_velocity:
            self.hor_velocity -= self.acc;
        if keys[pygame.K_d] and self.hor_velocity <= self.max_velocity:
            self.hor_velocity += self.acc;
        if not (keys[pygame.K_d] or keys[pygame.K_a]):
            if self.hor_velocity > 0:
                self.hor_velocity -= self.acc
            elif self.hor_velocity < 0:
                self.hor_velocity += self.acc
        self.x_cord += self.hor_velocity
        self.y_cord += self.ver_velocity
        print(self.hor_velocity)

        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

def main():
    # main variables
    run = True
    player = Player()
    clock = 0
    background = pygame.image.load("polana.png")
    coin_resp_time = 1.5

    while run:
        clock += pygame.time.Clock().tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False
        keys = pygame.key.get_pressed()
        if(clock >= coin_resp_time):
            clock = 0
        player.tick(keys)
        
        window.blit(background,(0,0))
        player.draw()
        pygame.display.update()

if __name__ == "__main__":
    main()