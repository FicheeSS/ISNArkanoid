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
    level = 2
    i = 1
    while 1 != 0 :
        win = univers.animate()
        #debug pour forcer à changer de niveau
        if i == 1 :
            i = 2
            win = True 
        if win  == False :
            print("fin")
            pygame.quit()
            sys.exit(0)
        elif win == True :
            if level == 2 :
                univers.levelChange(level)
            elif level == 3 :
                univers.levelChange(level)
            elif level == 4 :
                univers.levelChange(level)
            elif level == 5 :
                univers.levelChange(level)
            print(level)
            level += 1


main()