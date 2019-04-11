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
        self.balle = []
        for i in range(1):
            self.balle.append(Balle(((int(screenSize[0]/2 - RADIUS)),int((screenSize[1] - 50)))))
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
        
    
        for i in range(len(self.balle)):
            self.balle[i].get_colision(self.murhaut)
                #on verifie que la balle est en colision avec un des blocs
            for x in range(nbBriqueX) :
                for y in range(nbBriqueY) :
                    self.balle[i].get_colision(self.briques[x][y])
            #on verifie que la balle est en colison avec un des murs
            self.balle[i].get_colision(self.murdroit)
            self.balle[i].get_colision(self.murgauche)
            self.balle[i].get_colision(self.palette)
            if (self.balle[i].get_colision(self.murbas) == False):
                print("on arrete tous")
                return False
        self.screen.fill(noir)

        self.palette.animate()
        self.palette.dessine(self.screen)
        self.dessineBriques()
        for i in range(len(self.balle)):
            self.balle[i].animate()
            self.balle[i].dessine(self.screen)        
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
    
    def add_balle(self,pos):
        self.balle.append(Balle(pos))
    def add_speed(self):
        balle[0].add_speed()