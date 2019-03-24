from globalvar import * 
MURHAUT = 1
MURBAS = 0
MURGAUCHE = 2
MURDROITE = 3

class Mur:
    def __init__(self,extremites,type):
        self.extremites = extremites
        self.type = type

    def get_extremite1(self):
        return self.extremites[0]
    def get_extremite2(self):
        return self.extremites[1]