from globalvar import *
from palette import *
import pygame
class Balle:
    def __init__(self):
        self.radius = 15
        self.x = screenSize[0]/2 - self.radius
        self.y = screenSize[1] - 50
    def dessine (screen):
        pygame.draw.circle(screen, blanc , (self.x,self.y),self.raduis)
    def getX():
        return self.x
    def getY():
        return self.y
    
