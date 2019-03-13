from globalvar import *
import pygame
from couleur import * 
class Palette:
    def __init__(self):
        self.height = 10
        self.width = 30
        self.x = int(screenSize[0]/2 - self.height/2)
        self.y = screenSize[1]- self.width - 2 
    def dessine(self , screen):
        pygame.draw.rect(screen,blanc,(self.x,self.y,self.width,self.height))
    def animate (self):
        toto = 0

