import math
import pygame

class p:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class arrow:
    def __init__(self,start,norm,phase,freq):
        self.start = start
        self.norm = norm
        self.phase = phase
        self.freq = freq

    def getEndPoint(self):
        return p(self.norm*math.cos(self.phase)+self.start.x,self.norm*math.sin(self.phase)+self.start.y)

def draw_arrow(x,y,arrow,WINDOW):
    pygame.draw.line(WINDOW,(255,0,0),(x,y),(arrow.norm*math.cos(arrow.phase)+x,arrow.norm*math.sin(arrow.phase)+y),2)
    pygame.draw.circle(WINDOW,(100,100,100),(x,y),abs(arrow.norm),1)
    