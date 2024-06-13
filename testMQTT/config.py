import random 


BROKER = '192.168.105.112'
PORT = 1883
TOPIC = "wiot/sensor/stream/001"
CLIENT_ID = f'python-mqtt-{random.randint(0, 1000)}'
USERNAME = 'admin'
PASSWORD = 'admin'