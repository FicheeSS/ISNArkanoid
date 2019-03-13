from globalvar import *
from palette import *
import pygame
class Balle:
    def __init__(self):
        self.radius = 15
        self.x = int (screenSize[0]/2 - self.radius)
        self.y = screenSize[1] - 50
    def dessine (self , screen):
        pygame.draw.circle(screen, blanc , (self.x,self.y),self.radius)
    def calculnextpos(self):
        currentpos = (self.x,self.y)
        Psuiv = []
        Psuiv[0] = Psuiv[0] + 1
        Psuiv[1] = int(currentpos[1] + math.tan((theta*math.pi)/180)*(Psuiv[0]-currentpos[0]))
        return Psuiv
    def animate(self):
        toto = 0

        