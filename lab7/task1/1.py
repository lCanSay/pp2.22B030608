import pygame
from datetime import datetime


width = 870
height = 870
now = datetime.now()
angle_s = now.second
angle_m = -45 - now.minute*6

pygame.init()
screen= pygame.display.set_mode((width, height))
done = False
clock = pygame.time.Clock()


bg_image = pygame.image.load('images/mickeyclockv.png')
imgs = pygame.image.load("images/img_secondf.png")
rects = imgs.get_rect()
rects.center = (width//2, height//2)

imgm = pygame.image.load("images/img_minutef.png")
rectm = imgm.get_rect()
rectm.center = (width//2, height//2)

while not done:
        screen.blit(bg_image,(0,0))
        img1 = pygame.transform.rotate(imgs, angle_s)
        rect1 = img1.get_rect()
        rect1.center = rects.center

        img2 = pygame.transform.rotate(imgm, angle_m)
        rect2 = img2.get_rect()
        rect2.center = rectm.center

        screen.blit(img2,rect2)
        screen.blit(img1,rect1)

        angle_s -= 1
        angle_m -= 1/60
        

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True



        pygame.display.flip()
        clock.tick(6)