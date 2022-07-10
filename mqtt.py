# python3.6
import sys
import random
from time import sleep
from paho.mqtt import client as mqtt_client

broker = ''
port = 1883
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = ''
password = ''
global value
value = 3


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        if msg.topic == "akku":
            value = msg.payload.decode()
            print('akku: ' + value)
            f = open("transfer_akku.txt", "w")
            f.write(value)
        
        elif msg.topic == "batBezug":
            value = msg.payload.decode()
            print('batBezug: ' + value)
            f = open("transfer_batBezug.txt", "w")
            f.write(value)

        elif msg.topic == "produktion":
            value = msg.payload.decode()
            print('produktion: ' + value)
            f = open("transfer_produktion.txt", "w")
            f.write(value)

        elif msg.topic == "netzBezug":
            value = msg.payload.decode()
            print('netzBezug: ' + value)
            f = open("transfer_netzBezug.txt", "w")
            f.write(value)

    client.subscribe("akku")
    client.subscribe("batBezug")
    client.subscribe("produktion")
    client.subscribe("netzBezug")
    
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()