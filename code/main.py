#pip install RPi.GPIO
#Questo programma viene eseguito in background, e aspetta "l'input" dall'utente tramite il bottone
import RPi.GPIO as GPIO
import os

#Chiamo "speedtest.py" quando il bottone è premuto
def onButton(channel):
    if channel == 16:
        os.system("/home/root/myscripts/speedtest.py")

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(16, GPIO.FALLING, callback=onButton, bouncetime=20)
input()