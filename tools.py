from globalvar import *

def dessineCarre(pos , couleur):
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
    pos = (tab[0]*screenSize[0],tab[1]*screenSize[1])
    return pos