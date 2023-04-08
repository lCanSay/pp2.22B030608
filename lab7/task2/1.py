import pygame

width = 400
height = 400

pygame.init()
screen= pygame.display.set_mode((width, height))
done = False
clock = pygame.time.Clock()


_songs = ['sounds/bb.mp3', 'sounds/esaul.mp3', 'sounds/perf.mp3', 'sounds/wet.mp3']
i = 0
pygame.mixer.music.load(_songs[i])
pygame.mixer.music.play(0)
pygame.mixer.music.queue(_songs[i+1])

while not done:

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                
                elif event.type == pygame.KEYDOWN:
                       if event.key == pygame.K_w:
                              pygame.mixer.music.pause()
                       if event.key == pygame.K_s:
                              pygame.mixer.music.unpause()
                       if event.key == pygame.K_d and i!=3:
                              pygame.mixer.music.stop()
                              i += 1
                              pygame.mixer.music.load(_songs[i])
                              pygame.mixer.music.play(0)
                              pygame.mixer.music.queue(_songs[i+1])
                       if event.key == pygame.K_a and i != 0:   
                              pygame.mixer.music.stop()
                              i -= 1
                              pygame.mixer.music.load(_songs[i])
                              pygame.mixer.music.play(0)
                              pygame.mixer.music.queue(_songs[i+1])

        pygame.display.flip()
        clock.tick(60)