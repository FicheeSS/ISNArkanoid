from globalvar import *
import pygame 

def dessineCarre(pos , couleur,screen):
    """
    dessine un carré 
    pos : tuple(x,y) la position du carré
    couleur : la couleur 
    
    """
    pygame.draw.rect(screen,couleur,(pos[0],pos[1],widthCase,heightCase))

def getPosFromTab(tab):
    """
    renvoi la position du relative par rapport en tableau
    tab : positon dans le tableau
    return : la position 
    """
    pos = ((tab[0]*widthCase)+ecartcase*(tab[0]+1),(tab[1]*heightCase)+ecartcase*(tab[1]+1))
    return pos