import math  
from globalvar import *
from univer import *
def colisionWall(pos,radius):
    if pos[0]-radius <= 0 :
        return LEFTWALL
    elif pos[0]+radius >= SCREENSIZE[0]:
        return RIGHTWALL
    elif pos[1]+radius >= SCREENSIZE[1]:
        return BOTTOMWALL
    elif pos[1]-radius <= 0:
        return TOPWALL 
    
def colisionPalette(pal,pos,radius):
    if pal[0] <= pos[0]+radius  and pal[0]+PALETTEWIDTH >= pos[0]+radius and pal[1] <= pos[1]+radius+1:
        return True
    else:
        return False
        
def colisionBrick(bpos,c,radius):
    if c[0]+radius >= bpos[0] and c[0]+radius <= bpos[0]+WCASE :
        if c[1]+radius >= bpos[1] and c[1]+radius <= bpos[1]+HCASE:
            return True 
    else :
        return False