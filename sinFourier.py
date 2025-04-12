import pygame, sys, math
from pygame.locals import *
from arrowClass import *
from slider import *

BACKGROUND = (255, 255, 255)
FPS = 60

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
STARTING_LEN = 150
OFFSET = 300

pygame.init()

fpsClock = pygame.time.Clock()

def aN(n):
    return 1/(2*n+1)


WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Fourier')

arrowlist=[]

def update_arrows(n):
    for i in range(1,n):
        arrowlist[i].start.x=arrowlist[i-1].getEndPoint().x
        arrowlist[i].start.y=arrowlist[i-1].getEndPoint().y

def update_angles(time,n):
    for i in range(0,n):
        arrowlist[i].phase = arrowlist[i].freq * time

points = []

def drawPoints(shift):
    if (len(points) > 2):
        
        pygame.draw.aalines(WINDOW,(255,255,255),0,points,1)
        for i in range(len(points)):
            x,y = points[i]
            points[i] = x+shift,y
        if(points[0][0] > WINDOW_WIDTH - OFFSET / 5):
            points.pop(0)

def drawArrows(n):
    for i in range(0,n):
            draw_arrow(arrowlist[i].start.x,arrowlist[i].start.y,arrowlist[i],WINDOW)
        
def createArrows(n):
    arrowlist.clear()
    for i in range(0,n):
        arrowlist.append(arrow(p(WINDOW_WIDTH/4,WINDOW_HEIGHT/2),STARTING_LEN*aN(i),0,2*i+1))

def main () :
    looping = True
    time = 0
    s = Slider(20,20,200,5)
    n = s.val
    createArrows(n)
    
    while looping :
        shift = 1
        WINDOW.fill((0, 0, 0))

        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
           
         
        if pygame.mouse.get_pressed()[0]:
            
            drawPoints(0)
            s.handle_event(WINDOW,pygame.mouse.get_pos()[0])
            n = s.val
            createArrows(n)
            
            update_angles(time,n)
            update_arrows(n)
            
            drawArrows(n)
            
            x = arrowlist[n-1].getEndPoint().x
            y = arrowlist[n-1].getEndPoint().y
            pygame.draw.line(WINDOW,(255,255,255),(x,y),(WINDOW_WIDTH/4+OFFSET,y),2)
            
            pygame.display.update()
            continue
        else:
            s.draw(WINDOW)
            
        drawPoints(shift)
        
        drawArrows(n)
        
        update_angles(time,n)
        update_arrows(n)
        
        x = arrowlist[n-1].getEndPoint().x
        y = arrowlist[n-1].getEndPoint().y
        pygame.draw.line(WINDOW,(255,255,255),(x,y),(WINDOW_WIDTH/4+OFFSET,y),2)
        
        points.append((WINDOW_WIDTH/4+OFFSET,y))
    
        pygame.display.update()
        fpsClock.tick(FPS)
        time += 0.01
 
main()