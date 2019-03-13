from balle import *
from palette import *
import pygame
import math
from globalvar import *
from brique import *
class Univers:
    def __init__(self):
        print("univers")
        self.palette = Palette()
        self.balle = Balle()
        self.screen = 0
        self.briques = [[0] * nbBriqueY] * nbBriqueX
        x = 0 
        while x < nbBriqueX :
            y = 0 
            while y < nbBriqueY : 
                self.briques[x][y] = Brique()
                self.briques[x][y].x = (x*widthCase)+ecartcase*(x+1)
                self.briques[x][y].y = (y*heightCase)+ecartcase*(y+1)
                y += 1
            x += 1
            print("apres init")
            self.affichTableaux()

    def init(self):
        # Création et affichage de la fenêtre graphique
        self.screen = pygame.display.set_mode(screenSize)
 
    def animate(self):
        self.balle.animate()
        self.palette.animate()
        self.balle.dessine(self.screen)
        self.palette.dessine(self.screen)
        self.dessineBriques()
        pygame.display.flip()

    def affichTableaux(self):
        x = 0 
        while x < nbBriqueX :
            y = 0 
            while y < nbBriqueY : 
                print (" ",self.briques[x][y].x ," ", self.briques[x][y].y)
                y += 1
            x += 1

    def dessineBriques(self):
        print("dessin")
        self.affichTableaux()
        x = 0 
        while x < nbBriqueX :
            y = 0 
            while y < nbBriqueY :
                self.briques[x][y].dessine(self.screen) 
                y += 1
            x += 1
 