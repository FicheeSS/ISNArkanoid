import pygame
from couleur import *
from globalvar import *
class Brique :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = 1
        self.visible = True
        
    def dessine(self , screen):
        if self.visible == True :
            pygame.draw.rect(screen,self.stateToColor(),(self.x,self.y,widthCase,heightCase))


    def stateToColor(self):
        n = self.state 
        if n == 0:
            return noir
        if n == 1:
            return mediumspringgren
        if n == 2:
            return mediumseagreen
        if n == 3:
            return darkseagreen
        if n == 4:
            return indigo
        if n == 5:
            return rouge
        if n == 6:
            return cyan
        if n == 7:
            return mediumvioletred

    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def explose (self):
        self.visible = False