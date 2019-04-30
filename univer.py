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
        self.ball = []
        self.ball.append(Ball(((int(SCREENSIZE[0]/2 - RADIUS)),int((SCREENSIZE[1] - 50)))))
        
        #creation de la palette
        self.palette = Palette()
        #creation des murs
        self.murdroit = Mur(((0,SCREENSIZE[1]),(SCREENSIZE[0],SCREENSIZE[1])),RIGHTWALL)
        self.murgauche = Mur(((0,0),(0,SCREENSIZE[0])),LEFTWALL)
        self.murhaut = Mur(((0,0),(0,SCREENSIZE[1])),TOPWALL)
        self.murbas = Mur(((SCREENSIZE[0],0),(SCREENSIZE[0],SCREENSIZE[1])),BOTTOMWALL)
        #creation des briques dans un array 2D
        self.bricks = []
        for i in range(NBRICKSX):
            self.bricks.append([0]*NBRICKSX)
        for x in range(NBRICKSX) :
            for y in range(NBRICKSY) :
                sx = (x*WCASE)+GCASE*(x+1)
                sy = (y*HCASE)+GCASE*(y+1)
                state = niveau1[y][x]
                brique = Brique(sx, sy,state,Univers)
                self.bricks[x][y] = brique

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
        for x in range(NBRICKSX) :
            for y in range(NBRICKSY) :
                if self.bricks[x][y].isVisible() == 1 : 
                    return False
        return True

    def animate(self):
        #verification des collisions pour chaques balles  
        for i in range(len(self.ball)):
                #on verifie que la balle est en colision avec un des blocs
            for x in range(NBRICKSX) :
                for y in range(NBRICKSY) :
                    if self.bricks[x][y].isVisible() == True:
                        self.ball[i].get_colision(self.bricks[x][y])
            #on verifie que la balle est en colison avec un des murs
            self.ball[i].get_colision(self.murhaut)
            self.ball[i].get_colision(self.murdroit)
            self.ball[i].get_colision(self.murgauche)
            self.ball[i].get_colision(self.palette)
            if (self.ball[i].get_colision(self.murbas) == False):
                #fin du jeu le joueur a perdu
                return False
        #passage a l'affichage des différents éléments graphiques 
        self.screen.fill(noir)
        self.palette.animate()
        self.palette.dessine(self.screen)
        #fonction pour redessiner toutes les briques 
        self.dessineBriques()
        for i in range(len(self.ball)):
            #deplacement et dessins des balles 
            self.ball[i].animate()
            self.ball[i].dessine(self.screen)

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
        for x in range(NBRICKSX) :
            for y in range(NBRICKSY) :
                self.bricks[x][y].dessine(self.screen) 
    
    def add_balle(self,pos):
        #ne marche pas encore 
        self.ball.append(Ball(pos))

    def add_speed(self):
        #en cour de test
        Ball.add_speed(Univers.ball[0])

    def levelChange(self, niveau):
        #fonction pour changer de niveau 
        if niveau == 2 :
            print("niveau2")
            for x in range(NBRICKSX) :
                for y in range(NBRICKSY) :
                    self.bricks[x][y].setState(niveau2[y][x])
                    print(niveau2[y][x])
                    self.currentLvl = "Niveau 2"
        if niveau == 3 :
            print("niveau3")
            for x in range(NBRICKSX) :
                for y in range(NBRICKSY) :
                    self.bricks[x][y].setState(niveau3[y][x])
                    self.currentLvl = "Niveau 3"
        if niveau == 4 :
            print("niveau4")
            for x in range(NBRICKSX) :
                for y in range(NBRICKSY) :
                    self.bricks[x][y].setState(niveau4[y][x])
                    self.currentLvl = "Niveau 4"
        if niveau == 5 :
            print("niveau5")
            for x in range(NBRICKSX) :
                for y in range(NBRICKSY) :
                    self.bricks[x][y].setState(niveau5[y][x])
                    self.currentLvl = "Niveau 5"
        
        #réinitialisation de la balle 
        self.ball = []
        self.ball.append(Ball(((int(SCREENSIZE[0]/2 - RADIUS)),int((SCREENSIZE[1] - 50)))))
        #réinitailisation des counters 
        self.mincount = 0
        self.lastTime = 0
        self.counter = 0
        self.startupTime = time.time()

