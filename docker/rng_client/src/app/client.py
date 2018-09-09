import paho.mqtt.client as mqtt
import time

BROKER = "test.mosquitto.org"
TOPIC = "test/rng"

def on_message(client, userdata, msg):
    time_stamp = time.time()
    print(time_stamp)
    print("Random Number:"+str(msg.payload)) 

def on_connect(client, userdata, flags, rc):
   if rc==0:
        print("connected ok")
        client.subscribe("test/rng", qos=1)


def on_disconnect(client, userdata,rc=0):
        print("DisConnected result code "+str(rc))
        client.loop_stop()


client = mqtt.Client()             
client.on_connect=on_connect 
client.on_message = on_message
client.connect(BROKER)           
client.loop_forever()
