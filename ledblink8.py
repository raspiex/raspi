import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 26

GPIO.setup(led, GPIO.OUT)
GPIO.output(led, GPIO.LOW)
while True:
	GPIO.output(led, GPIO.HIGH)
	print ("the led is turning on")
	time.sleep(1)
	GPIO.output(led, GPIO.LOW)
	print ("the led is turning off")
	time.sleep(1)	