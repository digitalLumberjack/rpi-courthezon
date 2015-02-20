# Importons le code qui nous permettra de controller les GPIO
import RPi.GPIO as GPIO
import time


print("Utilisons la nomenclature BCM pour les GPIO")
GPIO.setmode(GPIO.BCM)

print("Passons le GPIO 17 en mode input")
GPIO.setup(17, GPIO.IN)

print("Et attendons que quelqu'un appuie sur le bouton branche sur le GPIO 17")
GPIO.wait_for_edge(17, GPIO.FALLING)

print("Bouton presse !")

print("Repassons a l'etat initial")
GPIO.cleanup()
