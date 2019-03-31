from globalvar import *
from palette import *
import pygame
import math
from collision import *
from mur import *
import random as rd
#réglage des paramètres de balle : vitesse, rebond
class Balle:
    def __init__(self):
        self.radius = 15
        self.x = int (screenSize[0]/2 - self.radius)
        self.y = screenSize[1] - 50
        self.angle = (300 * math.pi) / 180
        self.vitesse = 0.1
        self.palette = Palette()
        self.dernierrebond = (self.x,self.y)
        
# matérialistion de la balle         
    def dessine (self , screen):
        pygame.draw.circle(screen, blanc , (int(self.x),int(self.y)),self.radius)
    def calculnextpos(self):
        currentpos = (self.x,self.y)
        Psuiv = []
        Psuiv[0] = Psuiv[0] + 1
        Psuiv[1] = int(currentpos[1] + math.tan((theta*math.pi)/180)*(Psuiv[0]-currentpos[0]))
        return Psuiv
        
# animation de la balle
    def animate(self):
        dx = math.sin(self.angle) * self.vitesse
        dy = -math.cos(self.angle) * self.vitesse
        self.x += dx
        self.y += dy
        
# on calcul l'angle de rebond lors d'une collision de la balle avec un acteur
    def rebondir(self):
        rebondangle = 2*math.pi - (self.angle + math.pi)
        self.angle += rebondangle + math.pi

    
    
#on chercher a detecter la collision
    def get_colision(self,acteur):
        if (acteur.__class__.__name__ == "Brique") :
            p1 = (acteur.get_x(),acteur.get_y()+heightCase)
            p2 = (acteur.get_x()+widthCase,acteur.get_y()+heightCase)
            liste_points = DetectColisionCercleDroite(p1,p2,(self.x,self.y),self.radius)
            if len(liste_points) != 0:
                acteur.explose()
                self.rebondir()

        if (acteur.__class__.__name__ == "Mur") :
            liste_points = DetectColisionCercleDroite(acteur.get_extremite1(),acteur.get_extremite2(),(self.x,self.y),self.radius)
            if len(liste_points) !=0 :
                if(acteur.getType() != MURDROITE):
                    self.rebondir()
                    return 0
                else :
                    return -1
                    



        