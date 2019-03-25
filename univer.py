from balle import *
from palette import *
import pygame
from globalvar import *
from brique import *
from collision import *
from mur import *

class Univers:
    def __init__(self):
        print("univers")
        self.palette = Palette()
        self.balle = Balle()
        self.briques = []
        self.murdroit = Mur(((0,screenSize[1]),(screenSize[0],screenSize[1])),MURDROITE)
        self.murgauche = Mur(((0,0),(0,screenSize[0])),MURGAUCHE)
        self.murhaut = Mur(((0,0),(0,screenSize[1])),MURHAUT)
        self.murbas = Mur(((screenSize[0],0),(screenSize[0],screenSize[1])),MURBAS)
        for i in range(nbBriqueX):
            self.briques.append([0]*nbBriqueX)
        for x in range(nbBriqueX) :
            for y in range(nbBriqueY) :
                sx = (x*widthCase)+ecartcase*(x+1)
                sy = (y*heightCase)+ecartcase*(y+1)
                brique = Brique(sx, sy)
                self.briques[x][y] = brique

    def init(self):
        # Création et affichage de la fenêtre graphique
        self.screen = pygame.display.set_mode(screenSize)
 
    def animate(self):
        
        #on verifie que la balle est en colision avec un des blocs
        for x in range(nbBriqueX) :
            for y in range(nbBriqueY) :
                self.balle.get_colision(self.briques[x][y])
        #on verifie que la balle est en colison avec un des murs
        self.balle.get_colision(MURDROITE)
        self.balle.get_colision(MURGAUCHE)
        if (self.balle.get_colision(MURBAS) == -1):
            print("on arrete tous")
            return False
        self.balle.get_colision(MURHAUT)
        
        self.screen.fill(noir)
        self.balle.animate()
        self.palette.animate()
        self.balle.dessine(self.screen)
        self.palette.dessine(self.screen)
        self.dessineBriques()
        pygame.display.flip()
        return True

    def affichTableaux(self):
        for x in range(nbBriqueX) :
            for y in range(nbBriqueY) : 
                print (" ",self.briques[x][y].x ," ", self.briques[x][y].y)

    def dessineBriques(self):
        #self.affichTableaux() 
        for x in range(nbBriqueX) :
            for y in range(nbBriqueY) :
                self.briques[x][y].dessine(self.screen) 

 