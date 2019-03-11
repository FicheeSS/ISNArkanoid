from globalvar import *
import pygame 

def dessineCarre(pos , couleur,screen):
    """
    dessine un carré 
    pos : tuple(x,y) la position du carré
    couleur : la couleur 
    
    """
    pygame.draw.rect(screen,couleur,(pos[0],pos[1],widthCase-2,heightCase-2))

def getPosFromTab(tab):
    """
    renvoi la position du relative par rapport en tableau
    tab : positon dans le tableau
    return : la position 
    """
    pos = (tab[0]*cellulesx+2,tab[1]*cellulesy+2)
    return pos