import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

clock = pygame.time.Clock()

is_blue = True
x = 30
y = 30

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    is_blue = not is_blue

        if is_blue: color = (0, 128, 255)
        else: color = (100, 50, 0)

        pressed = pygame.key.get_pressed()
        if(pressed[pygame.K_UP]): y +=-3
        if(pressed[pygame.K_DOWN]): y +=3
        if(pressed[pygame.K_RIGHT]): x +=3
        if(pressed[pygame.K_LEFT]): x +=-3
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 30, 50))


        pygame.display.flip()
        clock.tick(60)