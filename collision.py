import math 
def DetectColisionCercleDroite (p1,p2,c,ray):

    #coefficient de la droite
    a = p2[1]-p1[1]/p2[0]-p1[0]
    b = p1[1]-a*p1[0]
    #Coefficient de l'équation
    A=1+a
    B = -2*c[0]+2*a*b-2*a*c[1]
    C = c[0]*c[0]+c[1]*c[1]+b*b-2*b*c[1]-ray*ray
    if B*B-4*A*C < 0 :
        #il se passe rien pas de point d'intersection
        return []
    else:
        #il a point d'intersection
        return [1,1]


