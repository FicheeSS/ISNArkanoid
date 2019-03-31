import math 
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
    A=1+a
    B = -2*c[0]+2*a*b-2*a*c[1]
    C = c[0]*c[0]+c[1]*c[1]+b*b-2*b*c[1]-ray*ray
    #print(B*B-4*A*C)
    if B*B-4*A*C < 0 :
        #il se passe rien pas de point d'intersection
        return []
    else:
        #il a point d'intersection
        if appartenance(p1,p2,[((-B-math.sqrt(B*B-4*A*C)/2*A),A*(-B-math.sqrt(B*B-4*A*C)/2*A)+B),((-B+math.sqrt(B*B-4*A*C)/2*A),A*(-B+math.sqrt(B*B-4*A*C)/2*A)+B)]) == True :    
            return [((-B-math.sqrt(B*B-4*A*C)/2*A),A*(-B-math.sqrt(B*B-4*A*C)/2*A)+B),((-B+math.sqrt(B*B-4*A*C)/2*A),A*(-B+math.sqrt(B*B-4*A*C)/2*A)+B)]
        else :
            return []

def appartenance(p1,p2,intersec):
    
    if intersec[0][0] >= p1[0] and intersec[0][0] <= p2[0]:
        return True
    elif intersec[1][0] >= p1[0] and intersec[1][0] <= p2[0]:
        return True
    else :
        return False
    

