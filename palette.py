from globalvar import *
import pygame
from couleur import * 
class Palette:
    def __init__(self):
        self.height = 10
        self.width = 50
        self.x = int(screenSize[0]/2 - self.width/2)
        self.y = screenSize[1]- self.height - 2 
        self.mvtdelta = 10
    def dessine(self , screen):
        pygame.draw.rect(screen,blanc,(self.x,self.y,self.width,self.height))
    def animate(self):
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if self.x < screenSize[0]:
                        self.x += self.mvtdelta
                if event.key == pygame.K_LEFT:
                    if self.x > 0 :
                        self.x -= self.mvtdelta

