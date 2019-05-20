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
    #On attends qui l'utilisateur appuie sur une touche 
    while 1 != 0:
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y :
                    univers.waitingMessage()
                    return True
                else:
                    return False
def main():
    while True :
        gameState = univers.animate()
        #message pour l'utilisateur en fin de niveau ou de jeu gameState represente la victoire ou non du joueur 
        if gameState == VICTORY :
            #Si le joueuer a fini le niveau on change le niveau
            endgame = univers.levelChange()
            if  endgame:
                waitingMessage('Niveau suivant : Monde ' + str(univers.currentLvl),False)
            else:
                if waitingMessage('Bravo vous avez gagnez !',True) == True :
                    return 0
                else :
                    pygame.quit()
                    sys.exit(0)
        elif gameState == DEFEAT :
            if waitingMessage('Vous avez perdu',True) :
                return 0
            else :
                pygame.quit()
                sys.exit(0)


while True:
    univers.init()
    main()
    

    