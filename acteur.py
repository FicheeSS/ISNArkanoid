from globalvar import *
import pygame
import math
import random
from collision import *
from couleur import *
from univer import *

class Ball:
    def __init__(self,pos):
        #réglage des paramètres de balle : vitesse, rebond
        self.img = pygame.image.fromstring(pygame.image.tostring(pygame.image.load("ball.bmp"),"RGBX"),(BALLSIZE,BALLSIZE),"RGBX")
        self.radius = RADIUS
        self.x = pos[0]
        self.y = pos[1]
        self.angle = (300 * math.pi) / 180
        self.speed = 1
        self.palette = Palette()
        
        
    def add_speed(self):
        #ajoute de la vitesse a la balle 
        self.speed += 0.1
         
    def dessine (self , screen):
        # dessin de la balle
        #pygame.draw.circle(screen, blanc , (int(self.x),int(self.y)),self.radius)
        screen.blit(self.img, (int(self.x - BALLSIZE/2),int(self.y - BALLSIZE/2)))

        
    def animate(self):
        # calcul de la nouvel position de la balle 
        dx = math.sin(self.angle) * self.speed
        dy = -math.cos(self.angle) * self.speed
        self.x += dx
        self.y += dy
        
# on calcul l'angle de rebond lors d'une collision de la balle avec un mur
    def rebondir(self):
        RB = math.pi - (math.pi + self.angle)
        self.angle = math.pi/2 - RB + random.uniform(-0.05 , 0.05)
            
    def rebondirgauche(self):
        RB = 2*math.pi - (math.pi + self.angle)
        self.angle = math.pi + RB + random.uniform(-0.05, 0.05)
    
    
#on chercher a detecter la collision
    def get_colision(self,acteur):
        #pour chaque acteur on effectue la recherche de la colision 
        if (acteur.__class__.__name__ == "Brique") :
            if colisionBrique(acteur.getPos(),(self.x,self.y),self.radius) == True :
                # on demande a la brique en question de disparaitre
                if acteur.explode() == True :
                    self.speed += 0.1 
                self.rebondir()

        if (acteur.__class__.__name__ == "Mur") :
            if rebond_mur((self.x,self.y),self.radius) == RIGHTWALL:
                self.x -= 1
                self.rebondirgauche()
                return True
            elif rebond_mur((self.x,self.y),self.radius) == LEFTWALL:
                self.x += 1
                self.rebondirgauche()
                return True
            elif rebond_mur((self.x,self.y),self.radius) == TOPWALL:
                self.y += 1 
                self.rebondir()
                return True
            elif  rebond_mur((self.x,self.y),self.radius) == BOTTOMWALL:
                return False
        if (acteur.__class__.__name__ == "Palette"):
            if colisionPalette(acteur.getPos(),(self.x,self.y),self.radius) == True :
                print("palette ")
                self.y -= 1
                self.rebondir()
class Brique :
    def __init__(self, x, y,state,univer):
        self.img = pygame.image.fromstring(pygame.image.tostring(pygame.image.load("briqueblanche.bmp"),"RGBX"),(BRIQUESIZE[0],BRIQUESIZE[1]),"RGBX")
        self.x = x
        self.y = y
        # l'etat est definie par le tableau niveau
        self.state = state
        if state > 0 :
            self.visible = True
        else:
            self.visible = False
        #pour debug :
        self.univer = univer
        for x in range(BRIQUESIZE[0]):
            for y in range(BRIQUESIZE[1]):
                if self.img.get_at((x,y)) == blanc :
                    self.img.set_at((x,y),self.stateToColor())

        
    def dessine(self , screen):
        if self.visible == True :
            #pygame.draw.rect(screen,self.stateToColor(),(self.x,self.y,WCASE,HCASE)) 
            screen.blit(self.img, (int(self.x ),int(self.y)))


    def stateToColor(self):
        # fait correspondre un etat à une couleur 
        n = self.state 
        if n == 0:
            return noir
        if n == 1:
            return green
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

    def getPos(self):
        #envoie un tuple de la postion en x et y 
        return(self.x,self.y)

    def explode (self):
        # on effectue les actions correspondantes a l'état de la balle 
        if self.state == 1 :
            self.visible = False
        elif self.state == 2 : 
            self.state -= 1 
        elif self.state == 3 :
            self.state -= 1 
        elif self.state == 4:
            # en test
            return True
            self.visible = False
        elif self.state == 7 :
            # ne fonctionne pas/ comme celui du dessus  
            self.univer.add_ball(self,(self.x,self.y))
            self.visible = False   

    def isVisible(self):
        # permet de savoir si la brique est visible pour par exemple savoir si il faut calculer la colision
        return self.visible

    def setState(self,state):
        # fonction utilisé dans le changement de niveau 
        self.img = pygame.image.fromstring(pygame.image.tostring(pygame.image.load("briqueblanche.bmp"),"RGBX"),(BRIQUESIZE[0],BRIQUESIZE[1]),"RGBX")
        self.state = state
        if self.state == 0 :
            self.visible = 0
        else:
            self.visible = 1
        for x in range(BRIQUESIZE[0]):
            for y in range(BRIQUESIZE[1]):
                if self.img.get_at((x,y)) == blanc :
                    self.img.set_at((x,y),self.stateToColor())

        
        
class Mur:
    def __init__(self,extremites,type):
        self.extremites = extremites
        self.type = type
        
    # utilisé pour savoir avec quel mur on a la colision
    def get_extremite(self):
        return self.extremites
    def get_type(self):
        return self.type
        
class Palette:
    def __init__(self):
        self.height = PALETTEHEIGHT
        self.width = PALETTEWIDTH
        self.img = pygame.image.fromstring(pygame.image.tostring(pygame.image.load("tram.bmp"),"RGBX"),(50,15),"RGBX")
        self.x = int(SCREENSIZE[0]/2 - self.width/2)
        self.y = SCREENSIZE[1]- self.height - 2 
        self.mvtdelta = 1
        self.lastKey = 0 

    def dessine(self , screen):
        #pygame.draw.rect(screen,blanc,(self.x,self.y,self.width,self.height))
        screen.blit(self.img, (int(self.x),int(self.y)))

    def animate(self):
        # fonction permettant de déplacer la palette avec un etat memoire pour permettre de faire un mouvement continuel
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and event.key == pygame.K_LEFT:
                    self.lastKey = 0
                if event.key == pygame.K_RIGHT:
                    self.lastKey = r_KEY
                    if self.x + self.width < SCREENSIZE[0]:
                        self.x += self.mvtdelta
                if event.key == pygame.K_LEFT:
                    self.lastKey = l_KEY
                    if self.x > 0 :
                        self.x -= self.mvtdelta
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.lastKey = 0 
        if self.lastKey == l_KEY :
            if self.x > 0 :
                self.x -= self.mvtdelta
        elif self.lastKey == r_KEY:
            if self.x + self.width < SCREENSIZE[0]:
                self.x += self.mvtdelta

    def getPos(self):
        # colision 
        return (self.x,self.y)
