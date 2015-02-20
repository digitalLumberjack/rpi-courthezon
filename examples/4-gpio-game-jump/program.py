import RPi.GPIO as GPIO
import pygame
from pygame.locals import*
import threading 

# Chargement des images
fond = pygame.image.load('bg.jpg')
mario_debout = pygame.image.load('mario-still.png')
mario_saut = pygame.image.load('mario-jump1.png')

# Chargement du son de saut 
pygame.mixer.init()
saut_mario_son = pygame.mixer.Sound("saut.wav")


# Definition des variables
largeur_ecran = 1280
hauteur_ecran = 720

mariox=610
mariobasey=545
marioy=mariobasey

mario_a_afficher=mario_debout

ecran_surface = pygame.display.set_mode((largeur_ecran, hauteur_ecran))

clock = pygame.time.Clock()

# Gestion du saut
jumping = False
coef=12.0
def updateMario():
    global coef,mario_a_afficher, marioy, jumping
    
    if( jumping ):
	mario_a_afficher=mario_saut
	if(coef > 0):
	    if(coef < 0.5):
		 coef = -0.5
	    else :
		marioy -= coef
		coef = coef - (coef * 4.0 / 100.0)
	else : 
		marioy -= coef
		coef = coef + (coef * 4.0 / 100.0)
		if ( marioy >= mariobasey ) :
			marioy = mariobasey
			jumping = False
    else :
	mario_a_afficher=mario_debout

ecran_surface.blit(fond,(0,0))
pygame.display.flip()	

# Observons le bouton brqnche sur le GPIO 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
def onButtonPress(channel):
        global jumping, coef
        if( not jumping):
		coef = 12
                jumping = True
                saut_mario_son.play()

GPIO.add_event_detect(17, GPIO.FALLING, callback=onButtonPress, bouncetime=300)


# Boucle principale
running = 1  
while running:    
    ecran_surface.blit(fond,(mariox,marioy), Rect(mariox, marioy, mario_a_afficher.get_width(), mario_a_afficher.get_height()))
    updateMario()
    ecran_surface.blit(mario_a_afficher,(mariox,marioy))
    pygame.display.flip()	
    clock.tick(60)    



