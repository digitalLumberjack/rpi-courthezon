# Importons le code qui nous permettra de controller les GPIO
import RPi.GPIO as GPIO
import time


print("Utilisons la nomenclature BCM pour les GPIO")
GPIO.setmode(GPIO.BCM)

print("Passons le GPIO 17 en mode input")
# GPIO.xxx()

print("Et attendons que quelqu'un appuie sur le bouton branche sur le GPIO 17")
# GPIO.xxx()

print("Bouton presse !")

print("Repassons a l'etat initial")
GPIO.cleanup()
