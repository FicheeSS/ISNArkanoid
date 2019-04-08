from globalvar import *
from palette import *
import pygame
import math
import random
from collision import *
from mur import *
from couleur import *
#réglage des paramètres de balle : vitesse, rebond
class Balle:
    def __init__(self):
        self.radius = 15
        self.x = int (screenSize[0]/2 - self.radius)
        self.y = screenSize[1] - 50
        self.angle = (300 * math.pi) / 180
        self.vitesse = 0.5
        self.palette = Palette()
        
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
        
# on calcul l'angle de rebond lors d'une collision de la balle avec un mur
    def rebondir(self):
        RB = 2*math.pi - (math.pi + self.angle)
        self.angle = math.pi/2 - RB + random.uniform(0.0 , 0.5)
    def rebondirgauche(self):
        RB = 2*math.pi - (math.pi + self.angle)
        self.angle = math.pi + RB + random.uniform(0.0 , 0.5)
    
    
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
            if rebond_mur((self.x,self.y),self.radius) == MURDROITE:
                self.x -= 1
                print("mur droite")
                self.rebondir()
            elif rebond_mur((self.x,self.y),self.radius) == MURGAUCHE:
                self.x += 1
                print("mur gauche")
                self.rebondirgauche()
            elif rebond_mur((self.x,self.y),self.radius) == MURHAUT:
                print("mur haut")
                self.y += 1 
                self.rebondir()
            elif  rebond_mur((self.x,self.y),self.radius) == MURBAS:
                print("fin du jeu")
                self.y -= 1
                self.rebondir()

class Brique :
    def __init__(self, x, y,state):
        self.x = x
        self.y = y
        self.state = state
        self.visible = True
        
    def dessine(self , screen):
        if self.visible == True :
            pygame.draw.rect(screen,self.stateToColor(),(self.x,self.y,widthCase,heightCase))   


    def stateToColor(self):
        n = self.state 
        if n == 0:
            return noir
        if n == 1:
            return green
        if n == 2:
            return mediumsgreen
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
        
        
class Mur:
    def __init__(self,extremites,type):
        self.extremites = extremites
        self.type = type

    def get_extremite(self):
        return self.extremites
    def get_type(self):
        return self.type