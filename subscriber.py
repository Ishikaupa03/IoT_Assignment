import paho.mqtt.client as mqtt

# MQTT settings
BROKER = 'test.mosquitto.org'  # Public MQTT broker
PORT = 1883
TOPIC = 'hotel/temperature'

def on_connect(client, userdata, flags, rc):
    """Callback function for when the client connects to the broker."""
    if rc == 0:
        print("Connected successfully to broker.")
        client.subscribe(TOPIC)
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    """Callback function for when a message is received."""
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

def main():
    """Main function to set up MQTT client and start listening."""
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    # Connect to the MQTT broker
    client.connect(BROKER, PORT, 60)
    client.loop_forever()  # Start the network loop

if __name__ == "__main__":
    main()
