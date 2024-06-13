from paho.mqtt import client as mqtt_client
from paho.mqtt.enums import CallbackAPIVersion
import time

from config import *



def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, reason code %d\n", reason_code)

        
def publish(client: mqtt_client.Client):
    while True:
        time.sleep(0.01)
        msg = f"time: {time.time()}"
        status, _ = client.publish(TOPIC, msg, qos=2)
        
        if status==0:
            print(f" Message Successfully Published to {TOPIC}")
    


####### MQTT INITIALIZE ####################

# create a client object
client = mqtt_client.Client(
    callback_api_version=CallbackAPIVersion.VERSION2,
    client_id=CLIENT_ID
)
# set username & password
client.username_pw_set(USERNAME,PASSWORD)

# callbacks

client.on_connect = on_connect
client.connect(BROKER, PORT)

client.loop_start()

publish(client)

client.loop()



