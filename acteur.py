from globalvar import *
import pygame
import math
import random
from collision import *
from couleur import *
from univer import *
#réglage des paramètres de balle : vitesse, rebond
class Balle:
    def __init__(self,pos):
        self.radius = RADIUS
        self.x = pos[0]
        self.y = pos[1]
        self.angle = (300 * math.pi) / 180
        self.vitesse = 1
        self.palette = Palette()
        
        
    def add_speed(self):
        self.vitesse += 0.1
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
        self.angle = math.pi/2 - RB + random.uniform(-0.01 , 0.01)
    def rebondirgauche(self):
        RB = 2*math.pi - (math.pi + self.angle)
        self.angle = math.pi + RB + random.uniform(-0.01, 0.01)
    
    
#on chercher a detecter la collision
    def get_colision(self,acteur):
        if (acteur.__class__.__name__ == "Brique") :
            """
            p1 = (acteur.get_x(),acteur.get_y()+heightCase)
            p2 = (acteur.get_x()+widthCase,acteur.get_y()+heightCase)
            liste_points = DetectColisionCercleDroite(p1,p2,(self.x,self.y),self.radius)
            """
            if colisionBrique(acteur.getPos(),(self.x,self.y),self.radius) == True:
                acteur.explose()
                self.rebondir()

        if (acteur.__class__.__name__ == "Mur") :
            if rebond_mur((self.x,self.y),self.radius) == MURDROITE:
                self.x -= 1
                print("mur droite")
                self.rebondirgauche()
                return True
            elif rebond_mur((self.x,self.y),self.radius) == MURGAUCHE:
                self.x += 1
                print("mur gauche")
                self.rebondirgauche()
                return True
            elif rebond_mur((self.x,self.y),self.radius) == MURHAUT:
                print("mur haut")
                self.y += 1 
                self.rebondir()
                return True
            elif  rebond_mur((self.x,self.y),self.radius) == MURBAS:
                return False
        if (acteur.__class__.__name__ == "Palette"):
            if colisionPalette(acteur.getPos(),(self.x,self.y),self.radius) == True :
                self.y -= 1
                self.rebondir()
class Brique :
    def __init__(self, x, y,state):
        self.x = x
        self.y = y
        self.state = state
        self.visible = True
        #self.univer = Univers()
        
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

    def getPos(self):
        return(self.x,self.y)
    def explose (self):
        print("explose")
        if self.state == 1 :
            self.visible = False
        elif self.state == 2 : 
            self.state -= 1 
        elif self.state == 3 :
            self.state -= 1 
        elif self.state == 4:
            univer.add_speed()
        elif self.state == 7 :
            univer.add_balle(self,(self.x,self.y))
            self.visible = False            
    def isVisible(self):
        return self.visible
        
        
class Mur:
    def __init__(self,extremites,type):
        self.extremites = extremites
        self.type = type

    def get_extremite(self):
        return self.extremites
    def get_type(self):
        return self.type
        
class Palette:
    def __init__(self):
        self.height = PALETTEHEIGHT
        self.width = PALETTEWIDTH
        self.x = int(screenSize[0]/2 - self.width/2)
        self.y = screenSize[1]- self.height - 2 
        self.mvtdelta = 10
    def dessine(self , screen):
        pygame.draw.rect(screen,blanc,(self.x,self.y,self.width,self.height))
    def animate(self):
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if self.x + self.width < screenSize[0]:
                        self.x += self.mvtdelta
                if event.key == pygame.K_LEFT:
                    if self.x > 0 :
                        self.x -= self.mvtdelta
    def getPos(self):
        return (self.x,self.y)
