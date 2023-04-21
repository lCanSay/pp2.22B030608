import pygame, math

pygame.init()

screen = pygame.display.set_mode((900, 700))
draw_on = False
last_pos = (0, 0)

radius = 5
font_style = pygame.font.SysFont(None, 30)


def roundline(canvas, color, start, end, radius=1):
    Xaxis = end[0] - start[0]
    Yaxis = end[1] - start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist):
        x = int(start[0] + float(i) / dist * Xaxis)
        y = int(start[1] + float(i) / dist * Yaxis)
        pygame.draw.circle(canvas, color, (x, y), radius)


try:
    blue = (0, 0, 255)
    red = (255, 0, 0)
    black = (0, 0, 0)
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    green = (0, 255, 0)
    color = black
    screen.fill(white)
    shape = 1
    while True:
        e = pygame.event.wait()
        if e.type == pygame.QUIT:
            raise StopIteration
        if e.type == pygame.KEYDOWN:
            # color selection
            if e.key == pygame.K_r:
                color = red
            elif e.key == pygame.K_g:
                color = green
            elif e.key == pygame.K_b:
                color = blue
            elif e.key == pygame.K_y:
                color = yellow
            elif e.key == pygame.K_n:
                color = black
            # change radius
            elif e.key == pygame.K_1:
                radius = 5
            elif e.key == pygame.K_2:
                radius = 7
            elif e.key == pygame.K_3:
                radius = 9
            elif e.key == pygame.K_4:
                radius = 11
            elif e.key == pygame.K_5:
                radius = 13
            elif e.key == pygame.K_6:
                radius = 15
            elif e.key == pygame.K_7:
                radius = 17
            elif e.key == pygame.K_8:
                radius = 19
            elif e.key == pygame.K_9:
                radius = 21
            elif e.key == pygame.K_0:
                radius = 2
            # eraser
            elif e.key == pygame.K_z:
                color = white
            # change chape
            elif e.key == pygame.K_x:
                shape = 2
            elif e.key == pygame.K_SPACE:
                shape = 1
            elif e.key == pygame.K_c:
                shape = 3
            elif e.key == pygame.K_v:
                shape = 4
            elif e.key == pygame.K_a:
                shape = 5
            elif e.key == pygame.K_s:
                shape = 6
        if e.type == pygame.MOUSEBUTTONDOWN and shape == 1:
            pygame.draw.circle(screen, color, e.pos, radius)
            draw_on = True
        if e.type == pygame.MOUSEBUTTONDOWN:
            p = e.pos
            if shape == 2:
                pygame.draw.rect(screen, color, pygame.Rect(e.pos, (radius * 3 + (radius * 3 * 1.35), radius * 3)))
            elif shape == 3:
                pygame.draw.circle(screen, color, e.pos, radius)
            elif shape == 4:
                pygame.draw.polygon(screen, color, [p, (p[0], p[1] + radius * 3), (p[0] + radius * 3, p[1])])
            elif shape == 5:
                pygame.draw.polygon(screen, color, [p, (p[0] + radius * 3, p[1]),
                                                    (p[0] + radius * 3 / 2, p[1] - (radius * 3 * math.sqrt(3) / 2))])
            elif shape == 6:
                pygame.draw.polygon(screen, color,
                                    [p, (p[0] + radius * 2, p[1] + radius * 2), (p[0], p[1] + radius * 2 * 2),
                                     (p[0] - radius * 2, p[1] + radius * 2)])
        if e.type == pygame.MOUSEBUTTONUP:
            draw_on = False
        if e.type == pygame.MOUSEMOTION:
            if draw_on and shape == 1:
                pygame.draw.circle(screen, color, e.pos, radius)
                roundline(screen, color, e.pos, last_pos, radius)
            last_pos = e.pos
        # instructions
        i1 = font_style.render("0-9-Choose the size", True, black)
        i2 = font_style.render("R,G,B,N,Y-Red,Green,Blue,Black,Yellow", True, black)
        i3 = font_style.render("Z-Eraser", True, black)
        i4 = font_style.render("SPACE-Return to the brush mode", True, black)
        i5 = font_style.render("X-Square,C-Circle,V-Triangle#1,A-Triangle#2,S-Rhombus", True, black)
        screen.blit(i1, (0, 0))
        screen.blit(i2, (0, 30))
        screen.blit(i3, (0, 60))
        screen.blit(i4, (0, 90))
        screen.blit(i5, (0, 120))
        pygame.display.flip()

except StopIteration:
    pass
pygame.quit()