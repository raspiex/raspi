import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 26
button = 19

GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN)
GPIO.output(led, GPIO.LOW)

while True:
	buttonRead = GPIO.input(button)
	print (buttonRead)
	GPIO.output(led, buttonRead)

