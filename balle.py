from globalvar import *
from palette import *
import pygame
import math
from collision import *
class Balle:
    def __init__(self):
        self.radius = 15
        self.x = int (screenSize[0]/2 - self.radius)
        self.y = screenSize[1] - 50
        self.angle = (300 * math.pi) / 180
        self.vitesse = 0.5
        self.palette = Palette()

    def dessine (self , screen):
        pygame.draw.circle(screen, blanc , (int(self.x),int(self.y)),self.radius)
    def calculnextpos(self):
        currentpos = (self.x,self.y)
        Psuiv = []
        Psuiv[0] = Psuiv[0] + 1
        Psuiv[1] = int(currentpos[1] + math.tan((theta*math.pi)/180)*(Psuiv[0]-currentpos[0]))
        return Psuiv

    def animate(self):
        dx = math.sin(self.angle) * self.vitesse
        dy = -math.cos(self.angle) * self.vitesse
        self.x += dx
        self.y += dy
    def get_colision(self,classe):
        if (classe.__class__.__name__ == "Brique") :
            p1 = ((((classe.get_x()*widthCase)+ecartcase*(classe.get_x()+1))+heightCase),((classe.get_y()*heightCase)+ecartcase*(classe.get_y()+1)))
            p2 = ((((classe.get_x()*widthCase)+ecartcase*(classe.get_x()+1))+heightCase),((classe.get_y()*heightCase)+ecartcase*(classe.get_y()+1)))
            return DetectColisionCercleDroite(p1,p2,(self.x,self.y),self.radius)


        