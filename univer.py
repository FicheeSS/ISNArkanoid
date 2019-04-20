from acteur import *
import pygame
from globalvar import *
from collision import *
import time
from levels import *
class Univers:
    def __init__(self):
        self.mincount = 0
        self.lastTime = 0
        self.counter = 0
        self.startupTime = time.time()
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
        self.screen = pygame.display.set_mode(effectiveSize)
    def texteTemp(self):
        if(self.counter >= 60 ):
            self.mincount+= 1
            self.counter = 0
        tmp = (str(self.mincount)+":" +str(self.counter))
        font = pygame.font.SysFont("verdana", 18, bold=False, italic=False)  
        text_area = font.render(tmp, 1, blanc)
        text_size = font.size(tmp)
        text_pos = [effectiveSize[0]/2-text_size[0]/2, effectiveSize[1]-text_size[1]]
        # ancrage de la surface contenant le texte dans la fenêtre
        self.screen.blit(text_area, text_pos)
 
    def animate(self):
    
        for i in range(len(self.balle)):
            self.balle[i].get_colision(self.murhaut)
                #on verifie que la balle est en colision avec un des blocs
            for x in range(nbBriqueX) :
                for y in range(nbBriqueY) :
                    if self.briques[x][y].isVisible() == True:
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
 
        
        self.lastTime = (time.time() - self.startupTime) 
        if int(self.lastTime) >= 1 :
                self.startupTime += 1
                self.counter += 1 
        self.texteTemp()
        pygame.display.flip()
        #print("lt " + str(self.lastTime) + " counter " + str(self.counter))
        
        
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
    