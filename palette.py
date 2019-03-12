from globalvar import *
import pygame
from couleur import * 
class Palette:
    def __init__(self):
        self.height = 10
        self.width = 30
        self.x = screenSize[0]/2 - self.height/2
        self.y = screenSize[1]- self.width - 2 
    def dessine(screen):
        pygame.draw.rect(screen,blanc,(self.x,self.y,self.width,self.height))
    def getX():
        return self.x

