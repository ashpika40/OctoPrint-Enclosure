import sys
import time
import board
import adafruit_dht


# Parse command line parameters.
sensor_args = { '11': DHT11,
    '22': DHT22 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    sys.exit(1)

dhtDevice = adafruit_dht.sensor(board.pin)

#humidity, temperature = Adafruit_DHT.read_retry(sensor, pin,2,0.5)

temperature = dhtDevice.temperature
humidity = dhtDevice.humidity

if humidity is not None and temperature is not None:
    print('{0:0.1f} | {1:0.1f}'.format(temperature, humidity))
else:
    print('-1 | -1')

sys.exit(1)

