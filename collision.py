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

def collisionWALL(pos,radius,wall):
    if wall.get_type() == LEFTWALL or wall.get_type() == RIGHTWALL:
        xp = wall.get_extremite()[0][0]
        yp = pos[1]
    else:
        xp = pos[0]
        yp = wall.get_extremite()[0][1]
    dx = pos[0] - xp
    dy = pos[1] - yp
    d = math.sqrt((dx*dx)+(dy*dy))
    if int(d) <= radius :
        return (xp,yp)
    else:
        return 0  
          
def colisionPalette(pal,pos,radius):
    if pal[0] <= pos[0]+radius  and pal[0]+PALETTEWIDTH >= pos[0]+radius and pal[1] <= pos[1]+radius+1:
        return True
    else:
        return False
        
"""
def colisionBrick(bpos,c,radius):
    if c[0]+radius >= bpos[0] and c[0]-radius <= bpos[0]+WCASE :
        if c[1]+radius >= bpos[1] and c[1]-radius <= bpos[1]+HCASE:
            return True 
    else :
        return False
"""

def ncolisionBrick(center,radius,brick):
    xc = center[0]
    yc = center[1]
    for wall in brick.getWalls():
        proj = collisionWALL(center,radius,wall)
        if  proj == 0 :
           return NOWALL
        else:
            xb = brick.getPos()[0]
            yb = brick.getPos()[1]
            type = wall.get_type()
            if type == LEFTWALL :
                if proj[1] > yb+HCASE :
                    #en dessous de la brique
                    dx = xc-xb
                    dy = yc - (yb + HCASE)
                    if int(math.sqrt(dx*dx+dy*dy)) <= radius:
                        return LEFTWALL
                    else :
                        return NOWALL
                elif proj[1] < yb :
                    dx = xc-xb
                    dy = yc-yb
                    if int(math.sqrt(dx*dx+dy*dy)) <= radius:
                        return LEFTWALL
                    else :
                        return NOWALL
                else :
                    return LEFTWALL

            elif type == RIGHTWALL:
                if proj[1] > yb+HCASE :
                    dx = xc - (xb + WCASE)
                    dy = yc - (yb + HCASE)
                    if int(math.sqrt(dx*dx+dy*dy)) <= radius:
                        return RIGHTWALL
                    else :
                        return NOWALL
                elif proj[1] < yb :
                    dx = xc - (xb + WCASE)
                    dy = yc - yb 
                    if int(math.sqrt(dx*dx+dy*dy)) <= radius:
                        return RIGHTWALL
                    else :
                        return NOWALL
                else :
                    return RIGHTWALL

            elif type == BOTTOMWALL:
                if proj[0] > xb+WCASE :
                    dx = xc - (xb+WCASE)
                    dy = yc - (yb+HCASE)
                    if int(math.sqrt(dx*dx+dy*dy)) <= radius:
                        return BOTTOMWALL
                    else :
                        return NOWALL
                elif proj[0] < xb :
                    dx = xc - xb
                    dy = yc - (yb+HCASE)
                    if int(math.sqrt(dx*dx+dy*dy)) <= radius:
                        return BOTTOMWALL
                    else :
                        return NOWALL
                else :
                    return BOTTOMWALL


            elif type == TOPWALL :
                if proj[0] > xb+WCASE :
                    dx = xc - (xb+WCASE)
                    dy = yc - yb
                    if  int(math.sqrt(dx*dx+dy*dy)) <= radius:
                        return TOPWALL
                    else :
                        return NOWALL
                elif proj[0] < xb :
                    dx = xc - xb
                    dy = yc - yb
                    if int(math.sqrt(dx*dx+dy*dy)) <= radius:
                        return TOPWALL
                    else :
                        return NOWALL
                else :
                    return TOPWALL
