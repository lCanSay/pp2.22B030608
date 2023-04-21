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
    def __init__(self, snake, wall):      #random spawn based on walls and snake
        self.a = Point(random.randint(0, 19), random.randint(0, 19))
        self.value = random.randint(1,2)
        xpoints = []
        ypoints = []
        for i in wall.body:
            xpoints.append(i.x)
            ypoints.append(i.y)
        for i in snake.body:
            xpoints.append(i.x)
            ypoints.append(i.y)
        while(True):
            if (self.a.x in xpoints or self.a.y in ypoints):
                self.a = Point(random.randint(0, 19), random.randint(0, 19))
            else:
               self.location = self.a 
               break

    def draw(self):
        rect = pygame.Rect(BLOCK_SIZE * self.location.x, BLOCK_SIZE * self.location.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (0, 255, 0), rect)
    def __del__(self):
        pass

class TimeFood(Food):
    def draw(self):
        self.value = 2
        rect = pygame.Rect(BLOCK_SIZE * self.location.x, BLOCK_SIZE * self.location.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (255, 255, 0), rect)



class Snake:
    def __init__(self):
        self.body = [Point(10,11)]
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
                for i in range(1, food.value+1):
                    self.body.append(Point(food.location.x - self.dx*(i-1), food.location.y-self.dy*(i-1)))
                return True
    def check_wall(self, wall):               #collision check for walls, same as for the food
        for i in range(len(wall.body)):
            if self.body[0].x == wall.body[i].x:
                if self.body[0].y == wall.body[i].y:
                    return True
        if(self.body[0].x >= WIDTH/20 or self.body[0].y >= HEIGHT/20 or self.body[0].x < 0 or self.body[0].y < 0): #checking for border collision
            return True
        return False
    

timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)




def main():
    global SCREEN, CLOCK, scoref
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    scoref = 0
    FPS = 6
    time_counter = -1
    f_counter = 0

    snake = Snake()
    wall = Wall(snake.level)
    food = Food(snake, wall)
    tfood = TimeFood(snake,wall)

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
            if event.type == timer_event:
                if (time_counter >= 0):
                    time_counter -= 1

        snake.move()

        if(snake.check_collision(food)):
            scoref += food.value
            food = Food(snake,wall)
            if tfood.location != (-1,-1):
                f_counter+=1
            if f_counter == 2:       #spawn 1 time limited food for every 2 usual ones
                f_counter = 0
                tfood = TimeFood(snake,wall)

        if(snake.check_collision(tfood)):
            scoref += 2
            tfood.location = Point(-1,-1)

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
        tfood.draw()
        if time_counter == -1 and tfood.location != (-1,-1):    
            time_counter = 5
        if time_counter == 0:
            tfood.location = Point(-1,-1)

        scores = font_small.render("Level: "+str(snake.level), True, WHITE)
        score1 = font_small.render("Score: "+str(scoref), True, WHITE)
        SCREEN.blit(scores, (360,20))
        SCREEN.blit(score1, (20,20))


        if len(snake.body) > 6 and len(snake.body) % 2 == 1:
            if(snake.level!=3):
                snake = Snake()
                snake.level += 1
                FPS+=1  #speed
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