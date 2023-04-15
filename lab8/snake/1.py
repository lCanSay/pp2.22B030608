import pygame, sys
from pygame.locals import *
import random, time

from os import scandir
from select import select
import pygame

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
HEIGHT = 400
WIDTH = 400
BLOCK_SIZE = 20


font = pygame.font.SysFont("Verdana", 40)
font_small = pygame.font.SysFont("Verdana", 10)
game_over = font.render("Game Over", True, BLACK)


class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y


class Wall:
    def __init__(self, level):
        self.body = []
        f = open("snake\levels\level{}.txt".format(level), "r")
        
        for y in range(0, HEIGHT//BLOCK_SIZE + 1):
            for x in range(0, WIDTH//BLOCK_SIZE + 1):
                if f.read(1) == '#':
                    self.body.append(Point(x, y))

    def draw(self):
        for point in self.body:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (226,135,67), rect)

class Food:
    def __init__(self, snake, wall):      #random spawn based on food and snake
        a = Point(random.randint(0, 20), random.randint(0, 20))
        xpoints = []
        ypoints = []
        for i in wall.body:
            xpoints.append(i.x)
            ypoints.append(i.y)
        for i in range(len(snake.body)-1):
            xpoints.append(snake.body[i].x)
            ypoints.append(snake.body[i].y)
        while(True):
            if (a.x in xpoints or a.y in ypoints):
                a = Point(random.randint(0, 20), random.randint(0, 20))
            else:
               self.location = a 
               break

    def draw(self):
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (0, 255, 0), rect)


class Snake:
    def __init__(self):
        self.body = [Point(10, 11)]
        self.dx = 0
        self.dy = 0
        self.level = 1

    def move(self):    
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y

        self.body[0].x += self.dx 
        self.body[0].y += self.dy 


    def draw(self):
        point = self.body[0]
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (255, 0, 0), rect)


        for point in self.body[1:]:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (0, 255, 0), rect)

    def check_collision(self, food):
        if self.body[0].x == food.location.x:
            if self.body[0].y == food.location.y:
                self.body.append(Point(food.location.x, food.location.y))
                return True
    def check_wall(self, wall):               #collision check for walls, same as for the food
        for i in range(len(wall.body)-1):
            if self.body[0].x == wall.body[i].x:
                if self.body[0].y == wall.body[i].y:
                    return True
        if(self.body[0].x >= WIDTH or self.body[0].y >= HEIGHT or self.body[0].x < 0 or self.body[0].y < 0): #checking for border collision
            return True
        return False
    

def main():
    global SCREEN, CLOCK, scoref
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    # SCREEN.fill(BLACK)
    scoref = 0
    FPS = 5
    snake = Snake()
    wall = Wall(snake.level)
    food = Food(snake, wall)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    if(snake.dx != -1):
                        snake.dx = 1
                        snake.dy = 0
                if event.key == pygame.K_a:
                    if(snake.dx != 1):
                        snake.dx = -1
                        snake.dy = 0
                if event.key == pygame.K_w:
                    if(snake.dy != 1):
                        snake.dx = 0
                        snake.dy = -1
                if event.key == pygame.K_s:
                    if(snake.dy != -1):
                        snake.dx = 0
                        snake.dy = 1

        snake.move()
        if(snake.check_collision(food)):
            scoref += 1
            food = Food(snake, wall)
        if(snake.check_wall(wall)):
            time.sleep(0.5)                   
            SCREEN.fill(WHITE)
            SCREEN.blit(game_over, (80,150))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()

        SCREEN.fill(BLACK)

        
        snake.draw()
        food.draw()
        wall.draw()
        scores = font_small.render("Level: "+str(snake.level), True, WHITE)
        score1 = font_small.render("Score: "+str(scoref), True, WHITE)
        SCREEN.blit(scores, (360,20))
        SCREEN.blit(score1, (20,20))


        if len(snake.body) > 4 and len(snake.body) % 2 == 1:
            if(snake.level!=3):
                snake = Snake()
                snake.level += 1
                FPS+=5
                wall = Wall(snake.level)
            else:
                time.sleep(0.5)                   
                SCREEN.fill(RED)
                SCREEN.blit(game_over, (80,150))
                SCREEN.blit(score1, (60,180))
                pygame.display.update()
                time.sleep(2)
                pygame.quit()


        pygame.display.update()
        CLOCK.tick(FPS)

main()