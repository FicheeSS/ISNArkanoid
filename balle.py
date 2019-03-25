from globalvar import *
from palette import *
import pygame
import math
from collision import *
from mur import *
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

    def rebondir(self,impact,ext1,ext2):
        print (self.angle)
        self.angle = int((3.14/ 2) - self.angle)
        print (self.angle)
        self.angle = (self.angle * 2) + 3.14
        print (self.angle)
        if self.angle > (math.pi) * 2:
            self.angle = self.angle - (math.pi) * 2 
    
    

    def get_colision(self,acteur):
        if (acteur.__class__.__name__ == "Brique") :
            p1 = (acteur.get_x(),acteur.get_y()+heightCase)
            p2 = (acteur.get_x()+widthCase,acteur.get_y()+heightCase)
            liste_points = DetectColisionCercleDroite(p1,p2,(self.x,self.y),self.radius)
            if len(liste_points) != 0:
                acteur.explose()
                self.rebondir(liste_points[0],p1,p2)

        if (acteur.__class__.__name__ == "Mur") :
            liste_points = DetectColisionCercleDroite(acteur.get_extremite1(),acteur.get_extremite2(),(self.x,self.y),self.radius)
            if len(liste_points) !=0 :
                if(acteur.getType() != MURDROITE):
                    self.rebondir()
                    return 0
                else :
                    return -1



        