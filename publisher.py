import paho.mqtt.client as mqtt
import random
import time

# MQTT settings
BROKER = 'test.mosquitto.org'
PORT = 1883
TOPIC = 'hotel/temperature'

def generate_temperature():
    return round(random.uniform(18.0, 30.0), 2)  # Simulate temperature between 18.0°C and 30.0°C

def publish_temperature(client):
    while True:
        temperature = generate_temperature()
        client.publish(TOPIC, temperature)
        print(f"Published temperature: {temperature}°C")
        time.sleep(60)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(BROKER, PORT, 60)
    client.loop_start()
    publish_temperature(client)

if __name__ == "__main__":
    main()
