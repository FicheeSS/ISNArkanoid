from balle import *
from palette import *
import pygame
from globalvar import *
from brique import *

class Univers:
    def __init__(self):
        print("univers")
        self.palette = Palette()
        self.balle = Balle()
        self.briques = []
        for i in range(nbBriqueX):
            self.briques.append([0]*nbBriqueX)
        for x in range(nbBriqueX) :
            for y in range(nbBriqueY) :
                sx = (x*widthCase)+ecartcase*(x+1)
                sy = (y*heightCase)+ecartcase*(y+1)
                brique = Brique(sx, sy)
                self.briques[x][y] = brique
        #self.affichTableaux()

    def init(self):
        # Création et affichage de la fenêtre graphique
        self.screen = pygame.display.set_mode(screenSize)
 
    def animate(self):
        self.screen.fill(noir)
        self.balle.animate()
        self.palette.animate()
        self.balle.dessine(self.screen)
        self.palette.dessine(self.screen)
        self.dessineBriques()
        pygame.display.flip()

    def affichTableaux(self):
        for x in range(nbBriqueX) :
            for y in range(nbBriqueY) : 
                print (" ",self.briques[x][y].x ," ", self.briques[x][y].y)

    def dessineBriques(self):
        #self.affichTableaux() 
        for x in range(nbBriqueX) :
            for y in range(nbBriqueY) :
                self.briques[x][y].dessine(self.screen) 

 