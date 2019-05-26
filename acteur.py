from globalvar import *
import pygame
import math
import sys 
import random
from collision import *
from couleur import *
from univer import *

ballPict = pygame.image.fromstring(pygame.image.tostring(pygame.image.load("ball.bmp"),"RGBX"),(BALLSIZE,BALLSIZE),"RGBX")

class Ball:
    def __init__(self,pos):
        #réglage des paramètres de balle : vitesse, rebond
        self.img = ballPict
        self.radius = RADIUS
        self.x = pos[0]
        self.y = pos[1]
        self.angle = (300 * math.pi) / 180
        self.speed = 1
        

    def addSpeed(self,add):
       self.speed+= add
         
    def draw (self , screen):
        # dessin de la balle
        screen.blit(self.img, (int(self.x - BALLSIZE/2),int(self.y - BALLSIZE/2)))

        
    def animate(self):
        # calcul de la nouvel position de la balle 
        dx = math.sin(self.angle) * self.speed
        dy = -math.cos(self.angle) * self.speed
        self.x += dx
        self.y += dy
        
# on calcul l'angle de rebond lors d'une collision de la balle avec un mur
    def bounceHor(self):
        #Voir calcul dans le schéma dans le drive
        self.angle = -self.angle - math.pi + random.uniform(-0.05, 0.05)
        if self.angle >= 2*math.pi:
            self.angle -= 2*math.pi
            
    def bounceVert(self):
        self.angle = -self.angle+ random.uniform(-0.05, 0.05)
        if self.angle >= 2*math.pi:
            self.angle -= 2*math.pi
    
    
#on chercher a detecter la collision
    def get_colision(self,acteur,univer):
        #pour chaque acteur on effectue la recherche de la colision 
        if (acteur.__class__.__name__ == "Brick") :
            """if colisionBrick(acteur.getPos(),(self.x,self.y),self.radius) == True :
                # on demande a la Brick en question de disparaitre
                self.y += 1
                brick = acteur.explode(univer) 
                self.bounceHor()
                self.sound.playBounce() 
                return brick
            else :
                return 0"""
            col = ncolisionBrick((self.x,self.y),self.radius,acteur)
            if col != NOWALL:
                if col == LEFTWALL or col == RIGHTWALL:
                    self.bounceVert()
                else : 
                    self.bounceHor()
                brick = acteur.explode(univer) 
                univer.sound.playBounce()
                return brick
            else:
                return 0

        if (acteur.__class__.__name__ == "Mur") :
            if collisionWALL((self.x,self.y),self.radius,acteur) != 0:
                if acteur.get_type() == RIGHTWALL :
                    self.x -= 1
                    self.bounceVert()
                    univer.sound.playBounce()
                    return True
                elif acteur.get_type() == LEFTWALL :
                    self.x += 1
                    self.bounceVert()
                    univer.sound.playBounce()
                    return True
                elif acteur.get_type() == TOPWALL:
                    self.y += 1 
                    self.bounceHor()
                    univer.sound.playBounce()
                    return True
                elif acteur.get_type() == BOTTOMWALL:
                    return False
        if (acteur.__class__.__name__ == "Palette"):
            if colisionPalette(acteur.getPos(),(self.x,self.y),self.radius) == True :
                self.y -= 1
                self.sound.playBounce()
                univer.bounceHor()



class Brick :
    def __init__(self, x, y,state,univer):
        self.img = pygame.image.fromstring(pygame.image.tostring(pygame.image.load("briqueblanche.bmp"),"RGBX"),(BRICKSIZE[0],BRICKSIZE[1]),"RGBX")
        self.x = x
        self.y = y
        # l'etat est definie par le tableau niveau
        self.state = state
        if state > 0 :
            self.visible = True
        else:
            self.visible = False

        self.walls = [
            Mur(((x,y),(x,y+HCASE)),LEFTWALL),
            Mur(((x+WCASE,y),(x+WCASE,y+HCASE)),RIGHTWALL),
            Mur(((x,y+HCASE),(x+WCASE,y+HCASE)),BOTTOMWALL),
            Mur(((x,y),(x+WCASE,y)),TOPWALL)
            ]

        #création des images de couleur dependante de state 
        if self.visible != 0 :
            for x in range(BRICKSIZE[0]):
                for y in range(BRICKSIZE[1]):
                    if self.img.get_at((x,y)) == blanc :
                        self.img.set_at((x,y),self.stateToColor())

        
    def draw(self , screen):
        if self.visible == True :
            #pygame.draw.rect(screen,self.stateToColor(),(self.x,self.y,WCASE,HCASE)) 
            screen.blit(self.img, (int(self.x ),int(self.y)))


    def stateToColor(self):
        # fait correspondre un etat à une couleur 
        n = self.state 
        if n == 0:
            return noir
        if n == 1:
            return limegreen
        if n == 2:
            return green
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

    def getWalls(self):
        return self.walls
    def getPos(self):
        #envoie un tuple de la postion en x et y 
        return(self.x,self.y)

    def changeColor(self,new):
        #permet de faire changer la couleur de l'image en mémoire de la brique d'après le nouvel état de la brique  
        oldColor = self.stateToColor()
        self.state = new
        for x in range(BRICKSIZE[0]):
            for y in range(BRICKSIZE[1]):
                if self.img.get_at((x,y)) == oldColor :
                    self.img.set_at((x,y),self.stateToColor())
        

    def explode (self,univers):
        # on effectue les actions correspondantes a l'état de la brick 
        if self.state == 1 :
            self.visible = False
            return 10
        elif self.state == 2 : 
            #la brique à un ou deux niveaux de vie
            self.changeColor(1)
            return 5
        elif self.state == 3 :
            self.changeColor(2)
            return 5
        elif self.state == 4:
            univers.add_speed()
            self.visible = False
            return 20            
        elif self.state == 5 : 
            univers.add_ball((self.x,self.y))
            self.visible = False
            return 20
        else :
            return 0

    def isVisible(self):
        # permet de savoir si la Brick est visible pour par exemple savoir si il faut calculer la colision
        return self.visible

    def setState(self,state):
        # fonction utilisé dans le changement de niveau 
        self.img = pygame.image.fromstring(pygame.image.tostring(pygame.image.load("briqueblanche.bmp"),"RGBX"),(BRICKSIZE[0],BRICKSIZE[1]),"RGBX")
        self.state = state
        if self.state == 0 :
            self.visible = 0
        else:
            self.visible = 1
        #on remplace le blanc des briques d'origine par leurs nouvelles assignations 
        for x in range(BRICKSIZE[0]):
            for y in range(BRICKSIZE[1]):
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

    def draw(self , screen):
        screen.blit(self.img, (int(self.x),int(self.y)))

    def animate(self):
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.lastKey = r_KEY
                if event.key == pygame.K_LEFT:
                    self.lastKey = l_KEY
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.lastKey = 0 
        if self.lastKey == l_KEY and self.x > 0:
            self.x -= self.mvtdelta
        elif self.lastKey == r_KEY and self.x + self.width < SCREENSIZE[0]:
            self.x += self.mvtdelta

    def getPos(self):
        # colision 
        return (self.x,self.y)

class Sound:
    def __init__(self):
        pygame.mixer.init()
        self.BackgroundMusic = pygame.mixer.Sound(BACKGROUNDMUSICLOC)
        self.BounceSound = pygame.mixer.Sound(BOUNCESOUNDLOC)

    def playMusic(self):
        pygame.mixer.Channel(1).play(self.BackgroundMusic,-1)

    def playBounce(self):
        pygame.mixer.Channel(2).play(self.BounceSound)

    def stopMusic(self):
        pygame.mixer.Channel(1).stop()

        
