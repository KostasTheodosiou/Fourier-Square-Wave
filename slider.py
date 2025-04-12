import math
import pygame, sys, math
from pygame.locals import *


class Slider:
    def __init__(self, x, y, w, h):
        self.circle_x = x
        self.val = 1
        self.sliderRect = pygame.Rect(x, y, w, h)

    def draw(self, screen):
        pygame.draw.rect(screen, (100, 100, 100), self.sliderRect)
        pygame.draw.circle(screen, (240, 240, 240), (self.circle_x, (self.sliderRect.h / 2 + self.sliderRect.y)), self.sliderRect.h * 1.5)

    def get_val(self):
        return self.val

    def set_val(self, num):
        self.val = num

    def update_val(self, x):
        if x <= self.sliderRect.x:
            self.val = 1
        elif x > self.sliderRect.x + self.sliderRect.w:
            self.val = 50
        else:
            self.val = int((x - self.sliderRect.x) / 10)+1

    def on_slider(self, x, y):
        if self.on_slider_hold(x, y):
            return True
        else:
            return False

    def on_slider_hold(self, x, y):
        if ((x - self.circle_x) * (x - self.circle_x) + (y - (self.sliderRect.y + self.sliderRect.h / 2)) * (y - (self.sliderRect.y + self.sliderRect.h / 2)))\
               <= (self.sliderRect.h * 1.5) * (self.sliderRect.h * 1.5):
            return True
        else:
            return False

    def handle_event(self, screen, x):
        if x < self.sliderRect.x:
            self.circle_x = self.sliderRect.x
        elif x > self.sliderRect.x + self.sliderRect.w:
            self.circle_x = self.sliderRect.x + self.sliderRect.w
        else:
            self.circle_x = x
        self.draw(screen)
        self.update_val(x)
    
