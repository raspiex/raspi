import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import urllib.request

# Sensor should be set to Adafruit_DHT.DHT11,
sensor = Adafruit_DHT.DHT11
# Example using a Beaglebone Black with DHT sensor
# connected to pin P8_11.
#pin = 'P8_11'

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO4.
pin = 4
# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('failed')
    time.sleep(2)
    f=urllib.request.urlopen('https://api.thingspeak.com/update?api_key=27U2LIM2R9Y5KBC7&field1=%s&field2=%s'%(temperature, humidity))
    print(f.read())
    f.close
    