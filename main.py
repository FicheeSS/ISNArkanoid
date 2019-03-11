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
            dessineCarre(getPosFromTab(niveau1[x][y]))
            x += 1
        y+= 1 

init ()

def couleur_case (x,y):
    #renvoie la couleur de la case lorsqu'on envoie la position d'une case
    n = niveau1[x][y] 
    if n == 0:
        print (noir)  
    if n == 1:
        print (jaune)
    if n == 2:
        print (orange)
    if n == 3:
        print (rouge)
    if n == 4:
        print (magenta)
    if n == 5:
        print (violet)
    if n == 6:
        print (bleu)
    if n == 7:
        print (cyan)
    if n == 8:
        print (vert)
# boucle pour faire une pause en attente de l'appui sur la touche echap
encore = 1
while encore == 1:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT or 
           (event.type == pygame.KEYDOWN and 
            event.key == pygame.K_ESCAPE)):
            encore = 0
            
# sortie du programme
pygame.quit()