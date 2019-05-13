from acteur import *
import pygame
from globalvar import *
from collision import *
import time
from levels import *
class Univers:
    def __init__(self):
        #Création des conteurs
        self.score = 0
        self.currentLvl = 0
        #initialisation du timer
        self.mincount = 0
        self.lastTime = 0
        self.counter = 0
        self.startupTime = time.time()
        #creation de balle
        self.ball = []
        
        #creation de la palette
        self.palette = Palette()
        #creation des murs
        self.murdroit = Mur(((0,SCREENSIZE[1]),(SCREENSIZE[0],SCREENSIZE[1])),RIGHTWALL)
        self.murgauche = Mur(((0,0),(0,SCREENSIZE[0])),LEFTWALL)
        self.murhaut = Mur(((0,0),(0,SCREENSIZE[1])),TOPWALL)
        self.murbas = Mur(((SCREENSIZE[0],0),(SCREENSIZE[0],SCREENSIZE[1])),BOTTOMWALL)
        #creation des briques dans un array 2D
        self.bricks = []

    def init(self):
        # Création et affichage de la fenêtre graphique
        self.newObject = []
        self.screen = pygame.display.set_mode(effectiveSize)
        #création de la balle 
        self.ball.append(Ball(((int(SCREENSIZE[0]/2 - RADIUS)),int((SCREENSIZE[1] - 50)))))
        #création de la liste des Bricks
        for i in range(NBRICKSX):
            self.bricks.append([0]*NBRICKSX)
        for x in range(NBRICKSX) :
            for y in range(NBRICKSY) :
                sx = (x*WCASE)+GCASE*(x+1)
                sy = (y*HCASE)+GCASE*(y+1)
                state = LLEVEL[self.currentLvl][y][x]
                brick = Brick(sx, sy,state,Univers)
                self.bricks[x][y] = brick
        #On rénitialise l'écran
        self.screen.fill(noir)
        pygame.display.flip()


        

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

    def textescore(self):
        tmp = str(self.score)
        font = pygame.font.SysFont("verdana", 18, bold=False, italic=False)  
        text_area = font.render(tmp, 1, blanc)
        text_size = font.size(tmp)
        text_pos = [effectiveSize[0]/3-text_size[0]*2, effectiveSize[1]-text_size[1]]
        # ancrage de la surface contenant le texte dans la fenêtre
        self.screen.blit(text_area, text_pos)
        
    def texteLvl(self):
        #Fonction d'affichage du niveau en cour
        lvl = "Niveau " + str(self.currentLvl+1)
        font = pygame.font.SysFont("verdana", 18, bold=False, italic=False)  
        text_area = font.render(lvl, 1, blanc)
        text_size = font.size(lvl)
        text_pos = [effectiveSize[0]/2+text_size[0]/2 , effectiveSize[1]-text_size[1]]
        # ancrage de la surface contenant le texte dans la fenêtre
        self.screen.blit(text_area, text_pos)
 

    def checkEnd(self):
        #On calcul si il reste des briques sur le terrain 
        for x in range(NBRICKSX) :
            for y in range(NBRICKSY) :
                if self.bricks[x][y].isVisible() == 1 : 
                    return False
        return True

    def animate(self):
        #verification des collisions pour chaques balles  
        for ball in self.ball:
                #on verifie que la balle est en colision avec un des blocs
            for x in range(NBRICKSX) :
                for y in range(NBRICKSY) :
                    if self.bricks[x][y].isVisible() == True:
                        self.score += ball.get_colision(self.bricks[x][y])
            #on verifie que la balle est en colison avec un des murs
            ball.get_colision(self.murhaut)
            ball.get_colision(self.murdroit)
            ball.get_colision(self.murgauche)
            ball.get_colision(self.palette)
            if (ball.get_colision(self.murbas) == False):
                #fin du jeu le joueur a perdu
                return False
        #passage a l'affichage des différents éléments graphiques 
        self.screen.fill(noir)
        self.palette.animate()
        self.palette.draw(self.screen)
        #fonction pour dessiner toutes les briques 
        self.drawBriques()
        for i in range(len(self.ball)):
            #deplacement et dessins des balles 
            self.ball[i].animate()
            self.ball[i].draw(self.screen)

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
        self.texteLvl()
        if len(self.newObject) > 0:
            self.ball.append(self.newObject[0])
            self.newObject = []
        self.textescore()
        #rafraichissement de l'affichage 
        pygame.display.flip()

    def drawBriques(self):
        #fonction de dessins de toutes les briques sur le terrain  
        for x in range(NBRICKSX) :
            for y in range(NBRICKSY) :
                self.bricks[x][y].draw(self.screen) 
    
    def add_ball(self,pos):
        #ne marche pas encore 
        print("add balle")
        #Univers().newObject.append(Ball(pos))

    def levelChange(self):
        #fonction pour changer de niveau
        if self.currentLvl + 1 < len(LLEVEL):
            self.currentLvl += 1
            for x in range(NBRICKSX) :
                for y in range(NBRICKSY) :
                    self.bricks[x][y].setState(LLEVEL[self.currentLvl][y][x])
        else :
            return False
                
        
        #réinitialisation de la balle 
        self.ball = []
        self.ball.append(Ball(((int(SCREENSIZE[0]/2 - RADIUS)),int((SCREENSIZE[1] - 50)))))
        #réinitailisation des counters 
        self.mincount = 0
        self.lastTime = 0
        self.counter = 0
        self.startupTime = time.time()
        return True

