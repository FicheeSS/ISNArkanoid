from acteur import *
import pygame
from globalvar import *
from collision import *
from levels import *
class Univers:
    def __init__(self):
        #self.print_niveau()
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
                state = niveau1[y][x]
                brique = Brique(sx, sy,state)
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
        self.balle.get_colision(self.murdroit)
        self.balle.get_colision(self.murgauche)
        if (self.balle.get_colision(self.murbas) == -1):
            print("on arrete tous")
            return False
        self.balle.get_colision(self.murhaut)
        
        self.screen.fill(noir)
        self.balle.animate()
        self.palette.animate()
        self.palette.dessine(self.screen)
        self.dessineBriques()
        self.balle.dessine(self.screen)
        pygame.display.flip()
        return True

    def get_brique_tab(self):
        return self.brique
    def dessineBriques(self):
        #self.affichTableaux() 
        for x in range(nbBriqueX) :
            for y in range(nbBriqueY) :
                self.briques[x][y].dessine(self.screen) 

    def print_niveau(self):
        for i in range(nbBriqueX):
            print("x = " + str(i))
            for j in range(nbBriqueY):
                print("y = " + str(j))
                print(niveau1[j][i])
        