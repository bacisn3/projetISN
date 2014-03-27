#! /usr/bin/env python
import pygame
import random
nbEtoiles=300
width = 640
height = 400
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
listV=[1] 
listX=[1]
listY=[1]
def deplaceDroite(liste,vitesse):
	for i in range(1,len(liste)):
		liste[i]=liste[i]+vitesse[i]
		if liste[i]>= width:
			liste[i]=0
	return liste
	
for i in range (1,nbEtoiles):
	listX.extend([random.randint(0, width-1)])
	listY.extend([random.randint(0, height-1)])
 	listV.extend([random.randint(1, 8)])

while running:

	for i in range(1,nbEtoiles):
		screen.set_at((listX[i], listY[i]), (0, 0, 0))
	
	deplaceDroite(listX,listV)

	for i in range(1,nbEtoiles):
		couleur=listV[i]*30
		screen.set_at((listX[i], listY[i]), (couleur,couleur, couleur))
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.flip()
	clock.tick(200)
