import pygame, sys
from pygame.locals import *
import random, time

from os import scandir
from select import select
import pygame

import psycopg2
from config import config

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
HEIGHT = 400
WIDTH = 400
BLOCK_SIZE = 20


font = pygame.font.SysFont("Verdana", 40)                            #Fonts
font_medium = pygame.font.SysFont("Verdana", 30)
font_small = pygame.font.SysFont("Verdana", 10)
game_over = font.render("Game Over", True, BLACK)


class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y


class Wall:
    def __init__(self, level):
        self.body = []
        f = open("A:\proga\sem2\lab10\snake\levels\level{}.txt".format(level), "r")

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
        self.value = random.randint(1,2)        #random food weights
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

class TimeFood(Food):  #time limited food
    def draw(self):
        self.value = 2
        rect = pygame.Rect(BLOCK_SIZE * self.location.x, BLOCK_SIZE * self.location.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (255, 255, 0), rect)

class Snake:
    def __init__(self):
        self.body = [Point(10,11)]
        self.dx = 0
        self.dy = 0

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
                    self.body.append(Point(food.location.x - self.dx*(i-1), food.location.y-self.dy*(i-1)))  #Adding certain length to snake based on value
                return True
    def check_wall(self, wall):               #collision check for walls, same as for the food
        for i in range(len(wall.body)):
            if self.body[0].x == wall.body[i].x:
                if self.body[0].y == wall.body[i].y:
                    return True
        if(self.body[0].x >= WIDTH/20 or self.body[0].y >= HEIGHT/20 or self.body[0].x < 0 or self.body[0].y < 0): #checking for border collision
            return True
        return False
    

def fetch_user(user_name):                                                           #Checking if there is such user in db
        sql = """SELECT * from snake_scores WHERE user_nickname = '{}' """.format(user_name)
        
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()

            cur.execute(sql)
            result = cur.fetchone() 

            conn.commit()
            cur.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

def delete_user(user_name):
    sql = """ DELETE FROM snake_scores
                    WHERE user_nickname = %s"""
    sql_check = """SELECT * from snake_scores WHERE user_nickname = '{}' """.format(user_name)
    
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql_check)
        result = cur.fetchone() 
        if(result != None):
            cur.execute(sql, (user_name,))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)        #timer, ticks every 1 second




def main():
    global SCREEN, CLOCK, scoref
    pygame.init()
    user_name = str(input("Enter your name: "))
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()

    parameters = fetch_user(user_name)  
    if (parameters != None):
        scoref = parameters[2]
        level = parameters[3]
    else:
        scoref = 0
        level = 1
    FPS = 5 + level

    time_counter = -1       #timer
    f_counter = 0           #counter for usual food, to spawn time limited


    snake = Snake()
    wall = Wall(level)
    food = Food(snake, wall)
    tfood = TimeFood(snake,wall)
    pause = False
    save_c = True






    while True: 

        while pause:                                   #Pause 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        save_c = True
                        pause = False
                    if event.key == pygame.K_e:
                            parameters = fetch_user(user_name)
                            if parameters == None:
                                sql = """INSERT INTO snake_scores(user_nickname, user_score, user_level)
                                        VALUES(%s, %s, %s) 
                                        RETURNING user_id;"""
                            else:
                                sql = """ UPDATE snake_scores
                                        SET user_score = %s,
                                            user_level = %s
                                        WHERE user_nickname = %s"""
                            conn = None
                            save_c = False
                            try:
                                params = config()
                                conn = psycopg2.connect(**params)
                                cur = conn.cursor()
                                if parameters == None:
                                    values_insert = (user_name, scoref, level)   #parameters for submittion
                                    cur.execute(sql, values_insert)
                                else:
                                    cur.execute(sql, (scoref, level, user_name))

                                conn.commit()
                                cur.close()
                            except (Exception, psycopg2.DatabaseError) as error:
                                print(error)
                            finally:
                                if conn is not None:
                                    conn.close()



            SCREEN.fill(BLACK)
            pause_text = font_medium.render("Pause", True, WHITE)
            continue_text = font_small.render("Press Space to continue", True, WHITE)
            save_text = font_small.render("Press E to save your progress", True, WHITE)
            savedone_text = font_small.render("Your progress've been saved", True, WHITE)
            SCREEN.blit(pause_text, (150,160))
            SCREEN.blit(continue_text, (135,200))
            if(save_c and pause==True):
                SCREEN.blit(save_text, (120,220))
            if(not save_c):
                SCREEN.blit(savedone_text, (120,220))

            pygame.display.update()
            CLOCK.tick(FPS)  



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
                if event.key == pygame.K_SPACE:
                    pause = True
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
                time_counter = 5

        if(snake.check_collision(tfood)):
            scoref += 2
            tfood.location = Point(-1,-1)
            time_counter = -1

        if(snake.check_wall(wall)):
            delete_user(user_name)
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

        if time_counter == 0:                   #every time timer is 0, timefood moves from gamespace
            tfood.location = Point(-1,-1)

        scores = font_small.render("Level: "+str(level), True, WHITE)
        score1 = font_small.render("Score: "+str(scoref), True, WHITE)
        nick_text = font_small.render("Nickname: "+str(user_name), True, WHITE)
        SCREEN.blit(scores, (350,15))
        SCREEN.blit(score1, (10,30))
        SCREEN.blit(nick_text, (10,10))



        if len(snake.body) > 6 :   #When score is > 6, next level and speed increase
            if(level!=7):
                snake = Snake()
                level += 1
                FPS = 5 + level  #speed
                wall = Wall(level)
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