import time 
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led = 19

GPIO.setup(led, GPIO.OUT)

while True:
    GPIO.output(led,GPIO.LOW)
