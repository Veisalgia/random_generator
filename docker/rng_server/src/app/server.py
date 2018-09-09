import random
import paho.mqtt.publish as publish

BROKER = "test.mosquitto.org"
TOPIC = "test/rng"

publish.single(TOPIC, str(random.randint(1,101)), hostname=BROKER)
