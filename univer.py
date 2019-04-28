from acteur import *
import pygame
from globalvar import *
from collision import *
import time
from levels import *
class Univers:
    def __init__(self):
        self.currentLvl = "Niveau 1"
        #initialisation du timer
        self.mincount = 0
        self.lastTime = 0
        self.counter = 0
        self.startupTime = time.time()
        #creation de balle
        self.balle = []
        self.balle.append(Balle(((int(screenSize[0]/2 - RADIUS)),int((screenSize[1] - 50)))))
        
        #creation de la palette
        self.palette = Palette()
        #creation des murs
        self.murdroit = Mur(((0,screenSize[1]),(screenSize[0],screenSize[1])),MURDROITE)
        self.murgauche = Mur(((0,0),(0,screenSize[0])),MURGAUCHE)
        self.murhaut = Mur(((0,0),(0,screenSize[1])),MURHAUT)
        self.murbas = Mur(((screenSize[0],0),(screenSize[0],screenSize[1])),MURBAS)
        #creation des briques dans un array 2D
        self.briques = []
        for i in range(nbBriqueX):
            self.briques.append([0]*nbBriqueX)
        for x in range(nbBriqueX) :
            for y in range(nbBriqueY) :
                sx = (x*widthCase)+ecartcase*(x+1)
                sy = (y*heightCase)+ecartcase*(y+1)
                state = niveau1[y][x]
                brique = Brique(sx, sy,state,Univers)
                self.briques[x][y] = brique

    def init(self):
        # Création et affichage de la fenêtre graphique
        self.screen = pygame.display.set_mode(effectiveSize)

    def texteTemp(self):
        #fonction d'affichage du temps
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

    def texteLvl(self,lvl):
        #Fonction d'affichage du niveau en cour
        font = pygame.font.SysFont("verdana", 18, bold=False, italic=False)  
        text_area = font.render(lvl, 1, blanc)
        text_size = font.size(lvl)
        text_pos = [effectiveSize[0]/2+text_size[0]/2 , effectiveSize[1]-text_size[1]]
        # ancrage de la surface contenant le texte dans la fenêtre
        self.screen.blit(text_area, text_pos)
 

    def checkEnd(self):
        for x in range(nbBriqueX) :
            for y in range(nbBriqueY) :
                if self.briques[x][y].isVisible() == 1 : 
                    return False
        return True

    def animate(self):
        #verification des collisions pour chaques balles  
        for i in range(len(self.balle)):
                #on verifie que la balle est en colision avec un des blocs
            for x in range(nbBriqueX) :
                for y in range(nbBriqueY) :
                    if self.briques[x][y].isVisible() == True:
                        self.balle[i].get_colision(self.briques[x][y])
            #on verifie que la balle est en colison avec un des murs
            self.balle[i].get_colision(self.murhaut)
            self.balle[i].get_colision(self.murdroit)
            self.balle[i].get_colision(self.murgauche)
            self.balle[i].get_colision(self.palette)
            if (self.balle[i].get_colision(self.murbas) == False):
                #fin du jeu le joueur a perdu
                return False
        #passage a l'affichage des différents éléments graphiques 
        self.screen.fill(noir)
        self.palette.animate()
        self.palette.dessine(self.screen)
        #fonction pour redessiner toutes les briques 
        self.dessineBriques()
        for i in range(len(self.balle)):
            #deplacement et dessins des balles 
            self.balle[i].animate()
            self.balle[i].dessine(self.screen)

        if self.checkEnd() == True :
            #si il n'y a plus aucune brique sur le terrain le niveau est fini
            return True

        #timer         
        self.lastTime = (time.time() - self.startupTime) 
        if int(self.lastTime) >= 1 :
                self.startupTime += 1
                self.counter += 1 
        self.texteTemp()
        #affichage du niveau actuel
        self.texteLvl(self.currentLvl)
        #rafraichissement de l'affichage 
        pygame.display.flip()
        

    def dessineBriques(self):
        #fonction de dessins de toutes les briques sur le terrain  
        for x in range(nbBriqueX) :
            for y in range(nbBriqueY) :
                self.briques[x][y].dessine(self.screen) 
    
    def add_balle(self,pos):
        #ne marche pas encore 
        self.balle.append(Balle(pos))

    def add_speed(self):
        #en cour de test
        Balle.add_speed(Univers.balle[0])

    def levelChange(self, niveau):
        #fonction pour changer de niveau 
        if niveau == 2 :
            print("niveau2")
            for x in range(nbBriqueX) :
                for y in range(nbBriqueY) :
                    self.briques[x][y].setState(niveau2[y][x])
                    print(niveau2[y][x])
                    self.currentLvl = "Niveau 2"
        if niveau == 3 :
            print("niveau3")
            for x in range(nbBriqueX) :
                for y in range(nbBriqueY) :
                    self.briques[x][y].setState(niveau3[y][x])
                    self.currentLvl = "Niveau 3"
        if niveau == 4 :
            print("niveau4")
            for x in range(nbBriqueX) :
                for y in range(nbBriqueY) :
                    self.briques[x][y].setState(niveau4[y][x])
                    self.currentLvl = "Niveau 4"
        if niveau == 5 :
            print("niveau5")
            for x in range(nbBriqueX) :
                for y in range(nbBriqueY) :
                    self.briques[x][y].setState(niveau5[y][x])
                    self.currentLvl = "Niveau 5"
        
        #réinitialisation de la balle 
        self.balle = []
        self.balle.append(Balle(((int(screenSize[0]/2 - RADIUS)),int((screenSize[1] - 50)))))
        #réinitailisation des counters 
        self.mincount = 0
        self.lastTime = 0
        self.counter = 0
        self.startupTime = time.time()

