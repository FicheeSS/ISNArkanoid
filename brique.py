import pygame
from couleur import *
from globalvar import *
class Brique :
    def __init__(self):
        self.x = 0
        self.y = 0
        self.state = 1
        
    def dessine(self , screen):
        #print("x = " , self.x , " , y =" , self.y)
        pygame.draw.rect(screen,self.stateToColor(),(self.x,self.y,widthCase,heightCase))

    def stateToColor(self):
        n = self.state 
        if n == 0:
            return noir
        if n == 1:
            return jaune
        if n == 2:
            return orangerouge
        if n == 3:
            return rouge
        if n == 4:
            return magenta
        if n == 5:
            return violet
        if n == 6:
            return bleu
        if n == 7:
            return cyan
        if n == 8:
            return vertclair
            
