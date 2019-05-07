'''
Author : Théo Bocquet
'''
from globalvar import *
import pygame
from univer import *    
from couleur import *
import sys
import time

univers = Univers()

def waitingMessage(txt,p):
    univers.screen.fill(noir)
    #Fonction pour afficher le texte et attendre
    font = pygame.font.SysFont("verdana", 18, bold=False, italic=False)  
    text_area = font.render(txt, 1, blanc)
    text_size = font.size(txt)
    text_pos = [effectiveSize[0]/2-text_size[0]/2 , effectiveSize[1]/2-text_size[1]]
    # ancrage de la surface contenant le texte dans la fenêtre
    univers.screen.blit(text_area, text_pos)
    if p == True:
        txt = "Appuyer sur y pour recommencer"    
    else:
        txt = "Appuyer sur une touche"
    text_area = font.render(txt, 1, blanc)
    text_size = font.size(txt)
    text_pos = [effectiveSize[0]/2-text_size[0]/2 , effectiveSize[1]/2]
    univers.screen.blit(text_area, text_pos)
    
    pygame.display.flip()
    time.sleep(.1)
    while 1 != 0:
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y :
                    return True
                else:
                    return False
def main():
    
    pygame.init()
    univers.init()
    gameOn = 1
    print("reset")
    while gameOn != 0 :
        win = univers.animate()
        #message pour l'utilisateur en fin de niveau ou de jeu win represente la victoire ou non du joueur 
        if win  == False :
            if waitingMessage('Vous avez perdu',True) == True:
                gameOn = 0
            else :
                pygame.quit()
                sys.exit(0)
        elif win == True :
            endgame = univers.levelChange()
            if  endgame == False:
                waitingMessage('Bravo vous avez gagnez !',False)
                pygame.quit()
                sys.exit(0)
            elif endgame == True:
                waitingMessage('Niveau suivant : Monde  ' + str(univers.currentLvl),False)


while 0 != 1:
    univers.__init__()
    main()
    