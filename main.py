'''
Author : Théo Bocquet
'''
import pygame 
from tools import *
from levels import *
from couleur import *
import numpy

#Le but ici va etre de faire tourner le coeur du programme 
#global const
posBouleStartup = (50,50)
bouleRaduis = 15
widthCase = 25
heightCase = 15
posPalletStartup = (posBouleStartup[0]-bouleRaduis,posBouleStartup[1]-bouleRaduis)
screenSize = (40*15,40*25)

#global var
currentBoulePos = posBouleStartup
level = 1

def main():
    #le programme princpal se fait apres le init 
    print("oui")




#bite

def dessineCarre(pos , couleur):
    pygame.draw.rect(screen,couleur,(pos[0],pos[1],widthCase,heightCase))
def getPosFromTab(tab):
    """
    renvoi la position du relative par rapport en tableau
    tab : positon dans le tableau
    return : la position 
    """
    pos = (tab[0]*screenSize[0],tab[1]*screenSize[1])
    return pos

def init ():
    #a faire au debut pour positioner les cases et la boule
    pygame.init()
    # Création et affichage de la fenêtre graphique de largeur 900 et hauteur 600
    screen = pygame.display.set_mode(screenSize)
    pygame.display.flip()
    x = 0
    y = 0
    while y < 15:
        while x < 20 :
            listTemp = list(niveau1[x,y])
            dessineCarre(getPosFromTab(listTemp))
            x += 1
        y+= 1 

init ()
