import Adafruit_DHT
sensor = Adafruit_DHT.DHT11
gpio=12
while True:
	humidity, temperature = Adafruit_DHT.read_retry(sensor,gpio)
	print('Temp={0:0.1f}*C Humidity={1:0.0f}%'.format(temperature, humidity))