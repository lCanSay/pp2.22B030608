from turtle import position
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    baseLayer = pygame.Surface((640, 480))

    clock = pygame.time.Clock()
    
    prevX = -1
    prevY = -1
    currentX = -1
    currentY = -1

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (64, 128, 255)
    GREEN = (0, 200, 64)
    YELLOW = (225, 225, 0)
    PINK = (230, 50, 230)


    mode = "rectangle"   
    color = WHITE 

    screen.fill((0, 0, 0))

    isMouseDown = False

    while True:
        
        pressed = pygame.key.get_pressed()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:       #figure selection
                if event.key == pygame.K_r:
                    mode = "rectangle"
                if event.key == pygame.K_c:
                    mode = "circle"
                if event.key == pygame.K_p:
                    mode = "pen"
                if event.key == pygame.K_s:
                    mode = "square"
                if event.key == pygame.K_t:
                    mode = "r_triangle"
                if event.key == pygame.K_e:
                    mode = "e_triangle"
                if event.key == pygame.K_l:
                    mode = "rhombus"

                if event.key == pygame.K_1:         #color selection
                    color = WHITE
                if event.key == pygame.K_2:
                    color = BLACK
                if event.key == pygame.K_3:
                    color = RED
                if event.key == pygame.K_4:
                    color = GREEN
                if event.key == pygame.K_5:
                    color = BLUE
                if event.key == pygame.K_6:
                    color = YELLOW
                if event.key == pygame.K_7:
                    color = PINK

            if event.type == pygame.MOUSEBUTTONDOWN:             
                if event.button == 1: 
                    isMouseDown = True
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]    
                    prevX =  event.pos[0]
                    prevY =  event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baseLayer.blit(screen, (0, 0))


            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX =  event.pos[0]
                    currentY =  event.pos[1]
        

        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1 and mode == "rectangle":
             screen.blit(baseLayer, (0, 0))
             r = calculateRect(prevX, prevY, currentX, currentY)
             pygame.draw.rect(screen, color, pygame.Rect(r), 1)
        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1 and mode == "circle":
             screen.blit(baseLayer, (0, 0))
             r = calculateRect(prevX, prevY, currentX, currentY)
             pygame.draw.ellipse(screen, color, pygame.Rect(r), width=1)
        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1 and mode == "pen":
             pygame.draw.line(screen, color, (prevX, prevY), (currentX, currentY), 5)
             prevX = currentX
             prevY = currentY
        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1 and mode == "square":
             screen.blit(baseLayer, (0, 0))
             r = pygame.Rect(min(prevX, currentX), min(prevY, currentY), abs(prevX - currentX), abs(prevX - currentX))
             pygame.draw.rect(screen, color, pygame.Rect(r), 1) 
        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1 and mode == "r_triangle":
             screen.blit(baseLayer, (0, 0))
            #  r = calculateTrPoint(prevX, prevY, currentX, currentY)
             pygame.draw.polygon(screen, color, ((min(prevX, currentX), min(prevY, currentY)), (max(prevX, currentX), max(prevY, currentY)), (min(prevX, currentX), max(prevY, currentY))), 2)
        
        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1 and mode == "e_triangle":
             screen.blit(baseLayer, (0, 0))
             pygame.draw.polygon(screen, color, ((min(prevX, currentX), min(prevY, currentY)), (max(prevX, currentX), max(prevY, currentY)), (min(prevX, currentX), max(prevY, currentY))), 2)    
        
        if isMouseDown and prevX != -1 and prevY != -1 and currentX != -1 and currentY != -1 and mode == "rhombus":
             screen.blit(baseLayer, (0, 0))
             pygame.draw.polygon(screen, color, ((max(prevX, currentX)-abs(prevX-currentX)/2, max(prevY, currentY)),     (min(prevX, currentX), max(prevY, currentY)-abs(prevY-currentY)/2),       (max(prevX, currentX)-abs(prevX-currentX)/2, min(prevY, currentY)),     ((max(prevX, currentX), max(prevY, currentY)-abs(prevY-currentY)/2))      ), 2)    
        pygame.display.flip()
        clock.tick(60)
        
def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))
# def calculateTrPoint(x1, y1, x2, y2):
#     if(x2>x1 and y2>y1):
#         a = [(min(x1, x2), min(y1, y2)), (max(x1, x2), max(y1, y2)), (min(x1, x2), max(y1, y2))]
#         return a
#     if(x2<x1 and y2>y1):
#         a =[(max(x1, x2), min(y1, y2)), (min(x1, x2), max(y1, y2)), (max(x1, x2), max(y1, y2))]
#         return a
#     if(x2>x1 and y2<y1):
#         a = [(min(x1, x2), max(y1, y2)), (max(x1, x2), min(y1, y2)), (min(x1, x2), min(y1, y2))]
#         return a
#     if(x2<x1 and y2<y1):
#         a = [(max(x1, x2), max(y1, y2)), (min(x1, x2), min(y1, y2)), (max(x1, x2), min(y1, y2))]
#         return a
        

main()  