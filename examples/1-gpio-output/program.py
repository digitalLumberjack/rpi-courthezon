# Importons le code qui nous permettra de controller les GPIO
import RPi.GPIO as GPIO
import time


print("Utilisons la nomenclature BCM pour les GPIO")
GPIO.setmode(GPIO.BCM)

print("Passons le GPIO 04 en mode output")
GPIO.setup(4, GPIO.OUT)

print("Et envoyons le courant sur le GPIO 04 : ")
print("Dans 2")
time.sleep(1)
print("Dans 1")
time.sleep(1)

print("Maintenant")
GPIO.output(4,True)

print("LED allumee. Attendons 5 secondes")
time.sleep(5)

print("Et repassons a l'etat initial")
GPIO.output(4,False)
GPIO.cleanup()
