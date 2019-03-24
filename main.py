'''
Author : Théo Bocquet
'''
import pygame
from univer import *

#global var
univers = Univers()

def main():
    pygame.init()
    univers.init()
   
    for t in range (2000):
        encore = univers.animate()
        if encore == false :
            t = 2000

main()

