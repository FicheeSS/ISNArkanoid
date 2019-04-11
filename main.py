'''
Author : Théo Bocquet
'''
from globalvar import *
import pygame
from univer import *
         
#global var
univers = Univers()

def main():
    pygame.init()
    univers.init()
    print(screenSize)
   
    for t in range (5000):
        encore = univers.animate()
        if encore == False :
            print("fin")
            t = 5000
            pygame.quit()

main()

pygame.quit()