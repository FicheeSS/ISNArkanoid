import math 
from globalvar import *
from univer import *
def DetectColisionCercleDroite (p1,p2,c,ray):
    """
    p1 : point de droite 
    p2 : point de droite 
    c : centre du cercle 
    ray : rayon du cercle 
    """
    #coefficient de la droite
    a = p2[1]-p1[1]/p2[0]-p1[0]
    b = p1[1]-a*p1[0]
    #Coefficient de l'équation
    A=1+a*a
    B = -2*c[0]+2*a*b-2*a*c[1]
    C = c[0]*c[0]+c[1]*c[1]+b*b-2*b*c[1]-ray*ray
    #print(B*B-4*A*C)
    delta = B*B-4*A*C
    if  delta < 0 :
        #il se passe rien pas de point d'intersection
        return []
    else:
        #il a point d'intersection
        print("intersec p1 " + str(p1) +" p2 "+ str(p2)+" c+ray " + str(c))
        if appartenance(p1,p2,[((-B-math.sqrt(delta)/2*A),A*(-B-math.sqrt(delta)/2*A)+B),((-B+math.sqrt(delta)/2*A),A*(-B+math.sqrt(delta)/2*A)+B)]) == True :    
            #return []            
            return [((-B-math.sqrt(delta)/2*A),A*(-B-math.sqrt(delta)/2*A)+B),((-B+math.sqrt(delta)/2*A),A*(-B+math.sqrt(delta)/2*A)+B)]
        else :
            return []

def appartenance(p1,p2,intersec):
    
    if intersec[0][0] >= p1[0] and intersec[0][0] <= p2[0]:
        return True
    elif intersec[1][0] >= p1[0] and intersec[1][0] <= p2[0]:
        return True
    else :
        return False

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