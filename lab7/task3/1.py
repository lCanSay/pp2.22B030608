import pygame
from datetime import datetime


width = 870
height = 870

pygame.init()
screen= pygame.display.set_mode((width, height))
done = False
clock = pygame.time.Clock()


class Ball():
       def __init__(self, screen):
              self.screen = screen
              self.x = 25
              self.y = 25
       def draw(self, a,b):
              self.ball = pygame.draw.circle(self.screen, (255, 0, 0), [self.x+a, self.y+b], 25, 0)
a = 0
b = 0
ball = Ball(screen) 
while not done:
        screen.fill((255,255,255))
        ball.draw(a,b)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                keys = pygame.key.get_pressed()  #checking pressed keys
                if(b > 0):
                    if keys[pygame.K_w]:
                        b -= 20
                if(b < height-50):
                    if keys[pygame.K_s]:
                        b += 20
                if(a < width-50):
                    if keys[pygame.K_d]:
                        a += 20
                if(a > 0):
                    if keys[pygame.K_a]:
                        a -= 20
        pygame.display.flip()
        clock.tick(30)
