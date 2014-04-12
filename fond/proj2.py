# Initialisation
import pygame
import random
pygame.init()
width=800
height=600
nbNuages=5
continuer = True
#init vitesse et position des nuages
listV=[1] 
listX=[1]
listY=[1]
#init vitesse et position des collines
listV2=[1] 
listX2=[1]
listY2=[1]

listV3=[1] 
listX3=[1]
listY3=[1]
# couleur du fond
BLUE = (150, 190, 230)
# Import des images
    # taille fenetre
fenetre = pygame.display.set_mode((width, height))
    # Import nuage
nuage = pygame.image.load("nuage3.png")
nuage2 = pygame.image.load("nuage32.png")
    # Import collines
colline=pygame.image.load("Colline.png")
colline2=pygame.image.load("Colline2.png")
# deplacement des colines
def deplaceDroite3(liste3,vitesse3):

	for i in range(1,len(liste3)):

		liste3[i]=liste3[i]-vitesse3[i]

		if liste3[i]<= -1300:

			liste3[i]=width
   
def deplaceDroite2(liste2,vitesse2):

	for i in range(1,len(liste2)):

		liste2[i]=liste2[i]-vitesse2[i]

		if liste2[i]<= -1300:

			liste2[i]=width
# deplacement des nuages
def deplaceDroite(liste,vitesse):

	for i in range(1,len(liste)):

		liste[i]=liste[i]-vitesse[i]

		if liste[i]<= -800:

			liste[i]=width

	return liste
# boucle
while continuer:	

    # position d'affichage des collines  
    
    for i in range (1,5):

	listX2.extend([random.randint(width-1150, width-1150)])

	listV2.extend([random.randint(8,8)])
    
    for i in range (1,5):

	listX3.extend([random.randint(width, width)])

	listV3.extend([random.randint(8,8)])
    # position d'affichage des nuages
    for i in range (1,nbNuages):

	listX.extend([random.randint(0, width)])

	listY.extend([random.randint(0, height-300)])

	listV.extend([random.randint(1,2)])
 

    #for i in range(1,nbNuages):
        
        #fenetre.set_at((listX[i], listY[i]), (0, 0, 0))
        
        #fenetre.fill(BLUE)
        
    deplaceDroite(listX,listV)
    
    deplaceDroite2(listX2,listV2)
    
    deplaceDroite3(listX3,listV3)
    
    for i in range (1,nbNuages):
        
        fenetre.blit(nuage, (listX[i],listY[i])) 
        
        fenetre.blit(nuage2, (listX[i]+400,listY[i]-50))
    
         
    fenetre.blit(colline, (listX2[i],+210))
    fenetre.blit(colline2, (listX3[i],+210))
        
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            
                continuer = False
    
    pygame.display.flip()        
