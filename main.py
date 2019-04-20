'''
Author : Théo Bocquet
'''
from globalvar import *
import pygame
from univer import *
import sys
         
#global var
univers = Univers()

def main():
    pygame.init()
    univers.init()
    print(screenSize)
   
    while 1 != 0 :
        end = univers.animate()
        if end == False :
            print("fin")
            pygame.quit()
            sys.exit(0 )
main()