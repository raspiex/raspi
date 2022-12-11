import RPi.GPIO as GPIO
#from time import sleep
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#led2=18
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)
#GPIO.setup(led2, GPIO.OUT, initial=GPIO.LOW)
while True:
    GPIO.output(21, GPIO.HIGH)
    #GPIO.output(led2, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(21, GPIO.LOW)
    #GPIO.output(led2, GPIO.LOW)
    time.sleep(3)
    
