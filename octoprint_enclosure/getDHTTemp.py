import sys
import time
from board import D17, D18
import adafruit_dht


# Parse command line parameters.
sensor_args = { '11': adafruit_dht.DHT11, '22': adafruit_dht.DHT22}
pin_args= { '11' : D17, '12' : D18 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
  sensor =sensor_args[sys.argv[1]]
  pin = pin_args[sys.argv[2]]
 # pin = sys.argv[2]
else:
  sys.exit(1)

dhtDevice = sensor(pin)


#humidity, temperature = Adafruit_DHT.read_retry(sensor, pin,2,0.5)

temperature = dhtDevice.temperature
humidity = dhtDevice.humidity

if humidity is not None and temperature is not None:
    print('{0:0.1f} | {1:0.1f}'.format(temperature, humidity))
else:
    print('-1 | -1')

sys.exit(1)

