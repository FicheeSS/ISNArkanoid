'''
Author : Théo Bocquet
'''
import pygame
from levels import *
from couleur import *
from globalvar import *
from palette import * 
from univer import *

#global var
univers = Univers()


def main():
    init()
    univers.animate()





def init ():
    #a faire au debut pour positioner les cases et la boule
    pygame.init()
    univers.init()
    

main()
pygame.time.wait(1000)
