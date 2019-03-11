# -*- coding: utf-8 -*-

# importation du module graphique 2D pygame
import pygame
import pygame.gfxdraw
# importation du module math
import math
# importation des modules couleur et graphics
#from couleur import *
#from graphics import *

# definition de quelques constantes
"""L_CASE = 40
H_CASE = 20
L = 20
H = 16
WIDTH = L*L_CASE 
HEIGHT = H*H_CASE
SIZE = [WIDTH, HEIGHT]

VIDE = 0
BRIQUE = 1
COULEUR_BRIQUE = darkorange
COULEUR_VIDE = noir
COULEUR_BALLE = blanc"""

RAYON = 5
NB_LIGNE = 6 # nombre de lignes de briques
N = NB_LIGNE*(L-2) # nombre de briques

# Variables globales
jeu = []
P0 = [450,600]
P = [0,0]
Psuiv = [450,600]
theta = -30.0
avance = 1

def deplacement():
    Psuiv[0] = Psuiv[0] + 1
    Psuiv[1] = int(P0[1] + math.tan((theta*math.pi)/180)*(Psuiv[0]-P0[0]))
    print(Psuiv)

pygame.init()
screen = pygame.display.set_mode([900,600])

pygame.gfxdraw.pixel(screen, Psuiv[0], Psuiv[1], (255,0,0))
pygame.display.flip()
encore = 1
while encore == 1:
    deplacement()
    pygame.gfxdraw.pixel(screen, Psuiv[0], Psuiv[1], (255,0,0))
    pygame.display.flip()
    pygame.time.wait(10)

