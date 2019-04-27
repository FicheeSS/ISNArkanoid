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
    level = 1
    while 1 != 0 :
        win = univers.animate()
        if win  == False :
            print("fin")
            pygame.quit()
            sys.exit(0)
        elif win == True :
            if level == 2 :
                univers.levelChange(2)
                level += 1
            elif level == 3 :
                univers.levelChange(3)
                level += 1 
            elif level == 4 :
                univers.levelChange(4)
                level += 1
            elif level == 5 :
                univers.levelChange(5)
                level += 1


main()