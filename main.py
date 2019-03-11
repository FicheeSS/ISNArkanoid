'''
Author : Théo Bocquet
'''
import pygame
from tools import *
from levels import *
from couleur import *
from globalvar import *
from palette import * 
#global var
palette = Palette()
level = 1
def main():
    #le programme princpal se fait apres le init 
    print("oui")


def couleur_case (x,y):
    """    
    renvoie la couleur de la case lorsqu'on envoie la position d'une case
    """
    n = niveau1[x][y] 
    if n == 0:
        return jaune  
    if n == 1:
        return jaune
    if n == 2:
        return orangerouge
    if n == 3:
        return rouge
    if n == 4:
        return magenta
    if n == 5:
        return violet
    if n == 6:
        return bleu
    if n == 7:
        return cyan
    if n == 8:
        return vertclair
        


def init ():
    #a faire au debut pour positioner les cases et la boule
    pygame.init()
    # Création et affichage de la fenêtre graphique de largeur 900 et hauteur 600
    screen = pygame.display.set_mode(screenSize)
    pygame.display.flip()
    x = 0
    y = 0
    while y < cellulesy:
        x = 0
        while x < cellulesx :
            #print(getPosFromTab([x,y]))
            dessineCarre(getPosFromTab((x,y)),couleur_case(y,x),screen)
            x += 1
        y += 1 
    palette.dessine(screen)
    palette
    pygame.display.flip()
    

init ()

pygame.time.wait(1000)
