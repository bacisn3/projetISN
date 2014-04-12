# Initialisation
import pygame
import random
pygame.init()
width=800
height=600
nbNuages=5
continuer = True
white=(255,255,255)
fenetre = pygame.display.set_mode((width, height))
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([100, 200])
        self.image.fill(white)
        self.image.set_colorkey(white)
        pygame.draw.ellipse(self.image, color, [0, 0, 100, 200])
while continuer:	
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            
                continuer = False
    
    pygame.display.flip()        
