import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

clock = pygame.time.Clock()
surface = pygame.Surface((100, 100), pygame.SRCALPHA)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        screen.fill((255, 255, 255))
        
        screen.blit(pygame.image.load('test/pacman.png'), (20, 20))
        
        pygame.display.flip()
        clock.tick(60)
