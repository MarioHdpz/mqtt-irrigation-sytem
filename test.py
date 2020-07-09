# mqtt_sub.py - Python MQTT subscribe example 
#
import paho.mqtt.client as mqtt
import time
import sys

from settings import HOST, PORT, USER, PASSWORD
 
if __name__ == "__main__":
    client = mqtt.Client()
    client.username_pw_set(USER, password=PASSWORD)
    client.connect(HOST, PORT)

    message = sys.argv[1]

    message = client.publish("test", str(message), 1)

