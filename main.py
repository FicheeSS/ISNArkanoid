'''
Author : Théo Bocquet
'''
import pygame
from tools import *
from levels import *
from couleur import *
from globalvar import *
#global var
currentBoulePos = posBouleStartup
level = 1

def main():
    #le programme princpal se fait apres le init 
    print("oui")





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
            print((x,y))
            dessineCarre(getPosFromTab([x,y]),jaune,screen)
            x =+ 1
        y =+ 1 

init ()

pygame.quit()