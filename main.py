# first pip install pygame
import pygame
from random import randint 

pygame.init()
# variables
window_width = 1280
window_height = 720
window = pygame.display.set_mode((window_width, window_height))
coin_resp_time = 1.3


class Player:
    def __init__(self):
        self.image = pygame.image.load("manstand.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x_cord = (window_width-self.width)/2  
        self.y_cord = (window_height-self.height)/2 
        self.speed = 4
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
    
    def tick(self, keys):
        if keys[pygame.K_w]:
            self.y_cord -= self.speed;
        if keys[pygame.K_s]:
            self.y_cord += self.speed;
        if keys[pygame.K_a]:
            self.x_cord -= self.speed;
        if keys[pygame.K_d]:
            self.x_cord += self.speed;
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def blockedBorders(self):
        # Rect(x,y,width,height)
        pygame.draw.rect(window, (221, 47, 38), pygame.Rect(0, 0, 4, window_height))
        pygame.draw.rect(window, (221, 47, 38), pygame.Rect(0, 0, window_width, 4))
        pygame.draw.rect(window, (221, 47, 38), pygame.Rect(window_width-4, 0, 4, window_height))
        pygame.draw.rect(window, (221, 47, 38), pygame.Rect(0, window_height-4, window_width, 4 ))
   
        if(self.x_cord<0):
            self.x_cord = 0
        if(self.y_cord<0):
            self.y_cord = 0
        if(self.y_cord>window_height-self.height):
            self.y_cord = window_height-self.height
        if(self.x_cord>window_width-self.width):
            self.x_cord = window_width-self.width

    def teleportBorders(self):
        if(self.x_cord<0):
            self.x_cord = window_width-self.width
        if(self.y_cord<0):
            self.y_cord = window_height-self.height
        if(self.y_cord>window_height-self.height):
            self.y_cord = 0
        if(self.x_cord>window_width-self.width):
            self.x_cord = 0


    def draw(self, is_open):
        if is_open:
            self.teleportBorders()
        else:
            self.blockedBorders()

        window.blit(self.image, (self.x_cord, self.y_cord))

class Cash:
    def __init__(self):
        self.image = pygame.image.load("coin.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x_cord = randint(self.width, 1280-2*self.width)
        self.y_cord = randint(self.height,720-2*self.height)
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

class Key:
    def __init__(self):
        self.image = pygame.image.load("key.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x_cord = randint(self.width, 1280-2*self.width)
        self.y_cord = randint(self.height,720-2*self.height)
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))


class Bug:
    def __init__(self):
        self.image = pygame.image.load("bug.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x_cord = randint(self.width, 1280-2*self.width)
        self.y_cord = randint(self.height,720-2*self.height)
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

def main():
    # main variables
    is_open = False
    run = True
    player = Player()
    clock = 0
    clock2 = 0
    clock3 = 15;
    score = 0
    life = 5
    life_image = pygame.image.load("heart.png")
    banknotes = []
    special_keys = []
    bugs = []
    colors = [(230,230,230), (95, 157, 247), (255, 247, 233), (255, 115, 29), (255, 202, 202)]
    color_nr = 0
    text_image = pygame.font.Font.render(pygame.font.SysFont("Poppins",48), f"Twój wynik: {score}", True, (0,0,0))

    while run:
        clock += pygame.time.Clock().tick(60) / 1000
        #get events from player
        for event in pygame.event.get():
            # if player close the window
            if event.type == pygame.QUIT: 
                run = False
        keys = pygame.key.get_pressed()
        if(clock >= coin_resp_time):
            clock2 += 1
            clock3 -= 1
            clock = 0
            # bugs.append(Bug())

            banknotes.append(Cash())

        if(clock2 >= randint(20,30)):
            special_keys.append(Key())
            bugs.append(Bug())
            clock2 = 0

        if(clock3 <= 0):
            is_open = False

        player.tick(keys)
        for banknote in banknotes:
            banknote.tick()

        for special_key in special_keys:
            special_key.tick()
        
        for bug in bugs:
            bug.tick()
        
        for banknote in banknotes:
            if player.hitbox.colliderect(banknote.hitbox):
                banknotes.remove(banknote)
                score += 1
                color_nr += 1
                text_image = pygame.font.Font.render(pygame.font.SysFont("Poppins",48), f"Twój wynik: {score}", True, (0,0,0))
                if(color_nr == len(colors)):
                    color_nr = 0
                # print(score)

        for special_key in special_keys:
            # if player get a key
            if player.hitbox.colliderect(special_key.hitbox):
                special_keys.remove(special_key)
                is_open = True
                clock3 = 15

        for bug in bugs:
            # if player get a key
            if player.hitbox.colliderect(bug.hitbox):
                bugs.remove(bug)
                life-=1


        # change background
        window.fill(colors[color_nr])
        window.blit(text_image, (20,20))

        # place the player on the screen
        for banknote in banknotes:
            banknote.draw()
        for special_key in special_keys:
            special_key.draw()
        for bug in bugs:
            bug.draw()
        player.draw(is_open)

         # draw lives
        for i in range(1,life+1):
            window.blit(life_image, [i*(life_image.get_width()+5), window_height-50])

        pygame.display.update()

    if life > 0:
        keys = pygame.key.get_pressed()
    print("Twój wynik to: "+ str(score))

if __name__ == "__main__":
    main()