# mqtt_sub.py - Python MQTT subscribe example 
import paho.mqtt.client as mqtt

from settings import HOST, PORT, USER, PASSWORD

def on_connect(client, userdata, flags, rc):
    print("Connected to broker")
 
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

if __name__ == "__main__":
    client = mqtt.Client()
    client.username_pw_set(USER, password=PASSWORD)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT)  

    client.subscribe("#") 
    client.loop_forever()