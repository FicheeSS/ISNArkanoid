from balle import *
from palette import *
import pygame
from globalvar import *
from brique import *
from collision import *

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
        self.murgauche = ((0,0),(screenSize(0)))
        self.murdroite = ((0,screenSize(1)),(screenSize(0),screenSize(1)))
        self.murhaut = ((0,0),(0,screenSize(1))) 
        self.murbas = ((screenSize(0),0),(screenSize(0),screenSize(1)))
        #self.affichTableaux()

    def init(self):
        # Création et affichage de la fenêtre graphique
        self.screen = pygame.display.set_mode(screenSize)
 
    def animate(self):
        #on verifie que la balle est en colision avec un des blocs
        for x in range(nbBriqueX) :
            for y in range(nbBriqueY) : 
                if len(self.balle.get_colision(self.briques[x][y])) != 0  :
                    #la balle est en colision avec le bloc
                    self.briques[x][y] = 0
        #on verifie que la balle est en colison avec un des murs
        """
        if self.balle.get_colision(self.murgauche(0),self.murgauche(1)) == true :
            #fonction de rebond 
            print("rebond mur gauche ")
        if self.balle.get_colision(self.murdroite(0),self.murdroite(1)) == true :
            #fonction de rebond 
            print("rebond mur droite ")
        if self.balle.get_colision(self.murhaut(0),self.murhaut(1)) == true :
            #fonction de rebond 
            print("rebond mur haut ")
        if self.balle.get_colision(self.murbas(0),self.murbas(1)) == true :
            #fonction de fin de jeu 
            print("rebond mur bas ") 
        """
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

 