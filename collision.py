import math  
from globalvar import *
from univer import *
def rebond_mur(pos,radius):
    if pos[0]-radius <= 0 :
        return MURGAUCHE
    elif pos[0]+radius >= screenSize[0]:
        return MURDROITE
    elif pos[1]+radius >= screenSize[1]:
        return MURBAS
    elif pos[1]-radius <= 0:
        return MURHAUT 
    
def colisionPalette(pal,pos,radius):
    #print("palx = " + str(pal[0]) + " paly = " + str(pal[1])+" posx = " + str(pos[0]) + " posy = " + str(pos[1]) )
    if pal[0] <= pos[0]+radius  and pal[0]+PALETTEWIDTH >= pos[0]+radius and pal[1] <= pos[1]+radius+1:
        print("palette")
        return True
    else:
        return False
def colisionBrique(bpos,c,radius):
    if c[0]+radius >= bpos[0] and c[0]+radius <= bpos[0]+widthCase :
        if c[1]+radius >= bpos[1] and c[1]+radius <= bpos[1]+heightCase:
            return True 
    else :
        return False