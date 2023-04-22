import pygame, sys
from pygame.locals import *
import random, time
pygame.init()
width = 400
height = 600
speed = 1
SCORE = 0
COIN_SCORE = 0

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)


background = pygame.image.load("racer\AnimatedStreet.png")


screen= pygame.display.set_mode((width, height))
screen.fill(WHITE)
pygame.display.set_caption("Racer")
done = False
clock = pygame.time.Clock() 

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("racer\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,width-40),0) 
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,speed)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

class Coin(pygame.sprite.Sprite): #класс для монет
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("racer\Gold_coin.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,width-40),0)     
    def move(self):
        global COIN_SCORE
        self.rect.move_ip(0,3)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0) 
    # def draw(self, screen):
    #     screen.blit(self.image, self.rect) 
 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("racer\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[K_a]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < width:        
              if pressed_keys[K_d]:
                  self.rect.move_ip(5, 0)
    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)

P1 = Player()
E1 = Enemy()
C1 = Coin()
coin_img = C1.image
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)


value = random.randint(1,3)

INC_SPEED = pygame.USEREVENT + 1
 #speed increase
 
while not done:

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == INC_SPEED:
                     speed +=1
        
        screen.blit(background, (0,0))
        scores = font_small.render(str(SCORE), True, BLACK)
        scores1 = font_small.render("Coins"+str(COIN_SCORE), True, BLACK)
        scores11 = font_small.render(("Your Score is: "+ str(COIN_SCORE)), True, BLACK)
        screen.blit(scores, (10,10))
        screen.blit(scores1, (320,10))
        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)
            entity.move()
        screen.blit(coin_img, C1.rect) 
        C1.move()
        if P1.is_collided_with(C1):
            COIN_SCORE += value 
            value = random.randint(1,3)
            coin_img = pygame.transform.scale(C1.image,(10+10*value,10+10*value))#every time car hits a coin, value randomly changes and based on that, size changes too
            C1.rect.center = (random.randint(30, 370), 0)
        if COIN_SCORE >= 3 and COIN_SCORE != 0:   #every 3 coins increase enemy's speed by 2
            speed = COIN_SCORE/3 * 2 + 1

        if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('racer\crash.wav').play()
          time.sleep(0.5)
                    
          screen.fill(RED)
          screen.blit(game_over, (30,250))
          screen.blit(scores11, (115,400))

          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()

        pygame.display.update()
        clock.tick(60)